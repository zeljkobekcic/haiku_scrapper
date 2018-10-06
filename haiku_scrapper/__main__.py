import argparse
import os
import util as u

from multiprocessing import Pool
from util import haiku_available_offline, download_and_save_haiku


if __name__ == '__main__':
    haiku_ids = filter(lambda x: not haiku_available_offline(x), range(350_000))

    args = argparse.ArgumentParser()
    args.add_argument('-path', type=str, required=True,
                      help="This argument sets the directory in which you want the files to be downloaded. The "
                           "directory will not be created if it is missing")

    path = args.parse_args().path

    if not os.path.exists(path):
        print(os.listdir())

        msg = f'The provided path does not exist \'{path}\''
        raise AttributeError(msg)

    u.DATA_PATH = path

    with Pool(processes=8) as pool:
        pool.map(download_and_save_haiku, haiku_ids)
