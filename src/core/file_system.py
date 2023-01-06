"""
This module contains all functions for managing the extensions
directory
"""

import os
from gi.repository import Gio, GLib

def get_extensions_dir_name():
    return get_home_dir_path() + '/.datasets'

def get_entry_name():
    return 'entry.json'

def get_entry_path():
    return get_extensions_dir_name() + '/' + get_entry_name()

def check_entry_exists():
    return os.path.exists(get_entry_path()) and os.path.isfile(get_entry_path())

def get_home_dir_path():
    return os.path.expanduser('~')

def check_dir_exists():
    return os.path.exists(get_extensions_dir_name())


def create_dir(): 
    if check_dir_exists():
        print('datasets forlder exists')
    else:
        os.mkdir(get_extensions_dir_name())
        print('Folder created: ')

def remove_dir():
    if check_dir_exists():
        os.rmdir(get_extensions_dir_name())
        print('datasets folder removed')
    else:
        print('folder not found')

def copy_extension_sample():
    file: Gio.File = Gio.file_new_for_uri('resource:///com/github/psycomentis/DataMiningGtk/assets/samples/entry.json')
    file.copy(Gio.file_new_for_path(get_extensions_dir_name() + '/entry.json'), Gio.FileCopyFlags.NONE)
    sample_file = Gio.file_new_for_uri('resource:///com/github/psycomentis/DataMiningGtk/assets/samples/sample.py')
    sample_dir_path = get_extensions_dir_name() + '/sample'
    os.mkdir(sample_dir_path)
    sample_file.copy(Gio.file_new_for_path(sample_dir_path + '/sample.py'), Gio.FileCopyFlags.NONE)

def create_default_extensions_dir():
    if check_dir_exists():
        if not check_entry_exists():
            copy_extension_sample()
    else:
        create_dir()
        copy_extension_sample()




if __name__ == "__main__":
    # create_dir()
    # print(check_entry_exists())
    create_default_extensions_dir()

