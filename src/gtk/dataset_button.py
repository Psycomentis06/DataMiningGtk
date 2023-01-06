from gi.repository import Gtk
from .dataset_window import *

@Gtk.Template(resource_path = '/com/github/psycomentis/DataMiningGtk/gtk/dataset-button.ui')
class DatasetButton(Gtk.Frame):
    __gtype_name__ = 'DatasetButton'

    label_widget: Gtk.Label = Gtk.Template.Child('label')
    image_widget: Gtk.Image = Gtk.Template.Child('image')
    button_widget: Gtk.Button = Gtk.Template.Child('button')

    def __init__(self,context, **kwargs):
        super().__init__(**kwargs)
        self.context = context
        self.window = ''
        self.name = '' 
        self.label_name = ''
        self.description = ''
        self.image_resource = None

    def init_widget(self, name: str, label_name: str, description: str , image_resource: str):
        self.label_widget.set_text(label_name)
        self.button_widget.set_name(name)
        self.image_widget.set_from_resource(image_resource)
        self.set_child(self.button_widget)

    @Gtk.Template.Callback('dataset_button_click_handler')
    def button_handler(self, widget: Gtk.Button):
        dataset_entry_name = widget.get_name() 
        win = create_dataset_window_factory(application=self.context, dataset_name=dataset_entry_name)
        win.present()



def create_dataset_button_factory(application: Gtk.Application, name: str, label_name: str, description: str , image_resource: str):
    dataset_button = DatasetButton(context=application)
    dataset_button.init_widget(image_resource=image_resource, description=description, label_name=label_name, name=name)
    return dataset_button
