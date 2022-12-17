from gi.repository import Gtk, Adw

@Gtk.Template(resource_path = '/com/github/psycomentis/DataMiningGtk/gtk/dataset-picker.ui')
class DatasetPicker(Adw.ApplicationWindow):
    __gtype_name__ = 'DatasetPicker'
    label = Gtk.Template.Child()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)