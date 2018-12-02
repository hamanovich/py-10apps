import os
import platform
import subprocess

import cat_service


def main():
    print_header()
    folder = get_or_create_output_folder()
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('CAT FACTORY APP')
    print('===============')


def get_or_create_output_folder():
    full_path = os.path.join(os.path.dirname(__file__), 'cats')

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating a new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    cat_count = 8

    print('Contacting server to download cats…')

    for i in range(1, cat_count+1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat ' + name)
        cat_service.get_cat(folder, name)


def display_cats(folder):
    print('Displaying cats in OS window.')

    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your os: " + platform.system())


if __name__ == "__main__":
    main()
