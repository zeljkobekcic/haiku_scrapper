from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import os


DATA_PATH = 'data/'
HAIKU_PATH = DATA_PATH + '{haiku_id}.txt'


def haiku_available_offline(haiku_id: int) -> bool:
    """
    This function checks if the haiku with the given ID has already been downloaded.

    :param haiku_id: An integer which represents the haiku ID
    :return: True if the haiku has been downloaded and False otherwise.
    """
    return os.path.exists(HAIKU_PATH.format(haiku_id=haiku_id))


def download_haiku_raw(haiku_id: int) -> str:
    """
    Downloads the HTML with the haiku from \'http://haiku.somebullshit.net/haiku\'.

    :param haiku_id: An integer which represents the haiku ID
    :return: A string which holds the HTML content.
    """
    base_url = 'http://haiku.somebullshit.net/haiku/{id}.html'
    with urlopen(base_url.format(id=haiku_id)) as r:
        html_content = str(r.read())
        soup = BeautifulSoup(html_content, 'html.parser')
        haiku = soup.find_all('p')[-1].get_text()
        return haiku


def clean_haiku(haiku: str) -> str:
    """
    Takes the raw data and parses the haiku.

    :param haiku: The HTML file from \'http://haiku.somebullshit.net/haiku\'.
    :return: The actual haiku.
    """
    lines = [x.strip() for x in haiku.split('\\n')]
    clean_joined_lines = '\n'.join(lines)
    other_cleaning = clean_joined_lines.replace('\\\'', '\'').strip()
    return other_cleaning


def download_haiku(haiku_id: int) -> str:
    """
    Downloads the haiku with the provided ID.

    :param haiku_id: An integer which represents the haiku ID at \'http://haiku.somebullshit.net/haiku\'.
    :return: The haiku
    """
    haiku_raw = download_haiku_raw(haiku_id)
    haiku = clean_haiku(haiku_raw)
    return haiku


def save_haiku_to_file(haiku_id: int, haiku: str):
    """
    Saves the haiku to a file in the form of \'{path}/{haiku_id}.txt\'.

    :param haiku_id: An integer which represents the haiku ID at \'http://haiku.somebullshit.net/haiku\'.
    :param haiku: The haiku as a string
    """
    with open(HAIKU_PATH.format(haiku_id=haiku_id), 'w') as outfile:
        outfile.write(haiku)


def download_and_save_haiku(haiku_id: int):
    """
    Downloads and saves the haiku from \'http://haiku.somebullshit.net/haiku\'. This function prints some stuff to the
    stdout too.

    :param haiku_id: An integer which represents the haiku ID at \'http://haiku.somebullshit.net/haiku\'.
    :raises HTTPError and URLError if something goes wrong.
    """
    print(f'Downloading haiku: {haiku_id}')

    try:
        haiku = download_haiku(haiku_id)
        save_haiku_to_file(haiku_id, haiku)
        print(f'Finished download haiku: {haiku_id}')
    except HTTPError:
        print(f'HTTPError for haiku: {haiku_id}')
    except URLError:
        print(f'URLError for haiku: {haiku_id}')

