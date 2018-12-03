
'''
This is a journal module.
'''

import os


def load(name):
    '''
    This method creates and loads a new journal.
    :param name: This base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    '''

    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = get_full_pathname(name)
    print("... saving to: {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_or_create_output_folder():
    full_path = os.path.join(os.path.dirname(__file__), 'journals')
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def get_full_pathname(name):
    return os.path.join(get_or_create_output_folder(), name + '.txt')


def add_entry(text, journal_data):
    journal_data.append(text)
