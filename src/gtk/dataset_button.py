from gi.repository import Gtk

@Gtk.Template(resource_path = '/com/github/psycomentis/DataMiningGtk/gtk/dataset-button.ui')
class DatasetButton(Gtk.Button):
    __gtype_name__ = 'DatasetButton'

    label = Gtk.Template.Child()
    image = Gtk.Template.Child()
    button = Gtk.Template.Child()

    def __init__(self, window: Gtk.ApplicationWindow , name: str, label_name: str, description: str , image_resource: str, **kwargs):
        super().__init__(**kwargs)

    def init_template(self):
        print('after init')