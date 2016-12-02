# -*- coding: utf-8 -*-

import os
import requests
import json
import textwrap

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin
from urllib.error import HTTPError

THUMBNAILS_DIR = os.path.join(os.path.dirname(
    os.path.abspath('__file__')), '../thumbnails')


def download_thumbnails(movie_list):
    """
    映画の諸情報が入ったディクショナリを複数リストに追加したものを利用して、
    title(映画のタイトル)とimage(サムネイル画像のURL)から画像をダウンロードする。
    :param list movie_list:
    """

    # thumbnailsディレクトリが存在しない場合は作成する
    if not os.path.isdir(THUMBNAILS_DIR):
        os.makedirs(THUMBNAILS_DIR)

    for movie in movie_list:
        movie_title = movie['title']
        movie_title = movie_title.replace(' ', '_')
        movie_title = movie_title.replace('/', '_')

        # URLから拡張子を取得する
        _, ext = os.path.splitext(movie['image'])

        # 保存するサムネイル画像のファイル名を定義する
        image_file = movie_title + ext
        print('[ DOWNLOAD ] Download thumbnail {}'.format(image_file))

        # サムネイル画像のデータを書き込む
        with open(os.path.join(THUMBNAILS_DIR, image_file), 'wb') as f:
            raw_image = requests.get(movie['image']).content
            f.write(raw_image)


if __name__ == '__main__':

    # IMDb Top Rated Movies URLを指定
    url = 'http://www.imdb.com/chart/top?ref_=nv_mv_250_6'

    try:
        with urlopen(url) as res:
            html = res.read()
    except HTTPError as e:
        print(e)

    soup = BeautifulSoup(html, 'lxml')
    table = soup.find("tbody", {"class": "lister-list"})

    tr_list = [tr for tr in table.find_all('tr')]

    # 映画の諸情報を取得する
    movie_list = []
    for tr in tr_list:
        movie_dict = {}
        movie_image = tr.find('a').find('img')
        movie_dict['image'] = movie_image['src']  # サムネイル画像のURL

        title_column = tr.find('td', {'class': 'titleColumn'}).find('a')
        movie_dict['title'] = title_column.get_text()  # 映画のタイトル

        abs_movie_url = title_column['href']
        real_movie_url = urljoin(url, abs_movie_url)
        movie_dict['url'] = real_movie_url  # 映画の詳細情報へのURL
        movie_list.append(movie_dict)

    # サムネイル画像を保存する
    download_thumbnails(movie_list)

    # 必要な映画データを収集し、jsonファイルにdumpする
    movie_num = len(movie_list)
    for i, movie in enumerate(movie_list):

        print('[ PROCESS  ] {:3}/{} Now processing: {}'.format(i + 1,
                                                               movie_num, movie['title']))

        movie_url = movie['url']
        with urlopen(movie_url) as res:
            html = res.read()

        m_soup = BeautifulSoup(html, 'lxml')

        # People who liked this also liked情報を取得する
        try:
            recom_movies = m_soup.find('div', {'class': 'rec_page'})
            recom_movie_titles = [movie['alt']
                                  for movie in recom_movies.find_all('img')]
            recom_movie_images = [movie['loadlate']
                                  for movie in recom_movies.find_all('img')]

            # サムネイル画像を取得する
            _movie_list = []
            for title, image in zip(recom_movie_titles, recom_movie_images):
                _movie_dict = {}
                _movie_dict['title'] = title
                _movie_dict['image'] = image
                _movie_list.append(_movie_dict)

            download_thumbnails(_movie_list)

        except AttributeError as e:
            print('[  ERROR   ] {}.'.format(e))
            recom_movie_images = []
            recom_movie_images = []

        movie['recommended'] = recom_movie_titles
        movie['recom_image'] = recom_movie_images
        print('{:12} Recommended: {}'.format('', movie['recommended']))

        # Cast情報を取得する
        title_cast = m_soup.find('div', {'id': 'titleCast'})
        casts = [td.find('span').get_text()
                 for td in title_cast.find_all('td', {'class': 'itemprop'})]
        movie['cast'] = casts
        print('{:12} Casts: {}'.format(
            '', textwrap.shorten(str(movie['cast']), 100)))

        # Story Line情報を取得する
        story_line = m_soup.find('div', {'id': 'titleStoryLine'})
        description = story_line.find(
            'div', {'itemprop': 'description'}).find('p')
        movie['story'] = description.get_text().replace('\n', '')
        print('{:12} Description {}'.format(
            '', textwrap.shorten(str(movie['story']), 100)))

        # Plot Keywords情報を取得する
        keywords = m_soup.find(
            'div', {'itemprop': 'keywords'}).find_all('a')
        plot_keywords = [keyword.get_text().replace(' ', '')
                         for keyword in keywords]
        movie['keyword'] = plot_keywords
        print('{:12} Keywords {}'.format('', movie['keyword']))

        # Genre情報を取得する
        genres = m_soup.find('div', {'itemprop': 'genre'})
        genre = [genre.get_text().replace(' ', '')
                 for genre in genres.find_all('a')]
        movie['genre'] = genre
        print('{:12} Genres {}'.format('', movie['genre']))

        # Release Date情報を取得する
        release_date = m_soup.find('meta', {'itemprop': 'datePublished'})
        movie['release_date'] = release_date['content']
        print('{:12} Release Date {}.'.format('', movie['release_date']))

        # Runtime情報を取得する
        runtime = m_soup.find('time', {'itemprop': 'duration'})
        movie['runtime'] = runtime['datetime']
        print('{:12} Runtime {}.'.format('', movie['runtime']))

    with open('movie_data.json', 'w') as f:
        json.dump(movie_list, f, indent=4)
    print('[   DUMP   ] Dump movie_date.json')
