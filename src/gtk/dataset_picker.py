from gi.repository import Gtk, Adw, Gio, GLib 
import json

@Gtk.Template(resource_path = '/com/github/psycomentis/DataMiningGtk/gtk/dataset-picker.ui')
class DatasetPicker(Adw.ApplicationWindow):
    __gtype_name__ = 'DatasetPicker'
    dataset_btn_1 = Gtk.Template.Child()
    dataset_btn_2 = Gtk.Template.Child()
    buttons_container = Gtk.Template.Child()

    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #file = resource.open_stream('/com/github/psycomentis/DataMiningGtk/assets/data/datasets.json', Gio.ResourceLookupFlags.NONE)
        file: Gio.File = Gio.file_new_for_uri('resource:///com/github/psycomentis/DataMiningGtk/assets/data/datasets.json')
        f_input_stream: Gio.FileInputStream = file.read()
        json_bytes_data = f_input_stream.read_bytes(8192).get_data()
        json_obj = json.loads(json_bytes_data)
        for item in json_obj['datasets']:
            print(item['name'])


    def render_buttons():
        pass

    def button_handler():
        pass
