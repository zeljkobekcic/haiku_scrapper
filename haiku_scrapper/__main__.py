import argparse
import os
import util as u

from multiprocessing import Pool
from util import haiku_available_offline, download_and_save_haiku


if __name__ == '__main__':
    haiku_ids = filter(lambda x: not haiku_available_offline(x), range(350_000))

    args = argparse.ArgumentParser()
    args.add_argument('-path', type=str, required=True,
                      help='This argument sets the directory in which you '
                           'want the files to be downloaded. The directory '
                           'will not be created if it is missing')

    args.add_argument('-n_process', type=int, default=4,
                      help='This argument sets the number of processes for'
                           'multiprocessing to get this task done faster.')

    parser = args.parse_args()
    path = parser.path
    n_process = parser.n_process

    if not os.path.exists(path):
        msg = f'The provided path does not exist \'{path}\'.'
        raise AttributeError(msg)

    if n_process < 1:
        msg = f'The requested number of processes is invalid \'{n_process}\'.'
        raise AttributeError(msg)

    u.DATA_PATH = path

    with Pool(processes=n_process) as pool:
        pool.map(download_and_save_haiku, haiku_ids)
