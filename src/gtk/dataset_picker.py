from gi.repository import Gtk, Adw, Gio, GLib 
import json
from .dataset_button import create_dataset_button_factory 

@Gtk.Template(resource_path = '/com/github/psycomentis/DataMiningGtk/gtk/dataset-picker.ui')
class DatasetPicker(Adw.ApplicationWindow):
    __gtype_name__ = 'DatasetPicker'
    buttons_container: Gtk.Box = Gtk.Template.Child()

    
    def __init__(self, entry_data, **kwargs):
        super().__init__(**kwargs)
        self.entry_data = entry_data
        self.application = kwargs['application']


    def load_json_conf(self):
        #file = resource.open_stream('/com/github/psycomentis/DataMiningGtk/assets/data/datasets.json', Gio.ResourceLookupFlags.NONE)
        file: Gio.File = Gio.file_new_for_uri('resource:///com/github/psycomentis/DataMiningGtk/assets/data/datasets.json')
        f_input_stream: Gio.FileInputStream = file.read()
        # Why 8192
        # https://amolenaar.github.io/pgi-docgen/Gio-2.0/classes/InputStream.html#Gio.InputStream.read_bytes
        # At least for now
        json_bytes_data = f_input_stream.read_bytes(8192).get_data()
        return json.loads(json_bytes_data)

    def render_buttons(self):
        # json_obj = self.load_json_conf()
        json_obj = self.entry_data
        for item in json_obj['datasets']:
            if not item['name'] == 'sample':
                name = item['name']
                label_name = item['label_name']
                description = item['description']
                image_resource = item['image_resource']
                image_path = None
                if 'image_path' in item:
                    image_path = item['image_path']
                button_widget = create_dataset_button_factory(application=self.application, name=name, label_name=label_name, description=description, image_resource=image_resource, image_path=image_path)
                self.buttons_container.append(button_widget)


    #@Gtk.Template.Callback('dataset_button_click_handler')
    def button_handler(self, widget: Gtk.Button):
        print(widget.get_name())
