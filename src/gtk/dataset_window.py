from gi.repository import Gtk, Adw 

@Gtk.Template(resource_path = '/com/github/psycomentis/DataMiningGtk/gtk/dataset-window.ui')
class DatasetWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'DatasetWindow'
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)