'''
This class is the representation for the json datasets extensions 
'''
from gi.repository import Gio 
import json
from .file_system import *

class EntryFile:

    def __init__(self):
        self.load_json()

    def load_json(self):
        entry_path = get_entry_path()
        file = Gio.file_new_for_path(entry_path)
        f_input_stream = file.read()
        json_bytes = f_input_stream.read_bytes(8192).get_data()
        self.bytes_data = json_bytes
        self.json_data = json.loads(json_bytes)

    def get_item_by_name(self, name: int):
        for item in self.json_data['datasets']:
            if item['name'] == name:
                return item
        return None

    def get_json_data(self):
        return self.json_data

    def get_bytes_data(self):
        return self.bytes_data
