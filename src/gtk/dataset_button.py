from gi.repository import Gtk

@Gtk.Template(resource_path = '/com/github/psycomentis/DataMiningGtk/gtk/dataset-button.ui')
class DatasetButton(Gtk.Frame):
    __gtype_name__ = 'DatasetButton'

    label_widget: Gtk.Label = Gtk.Template.Child('label')
    image_widget: Gtk.Image = Gtk.Template.Child('image')
    button_widget: Gtk.Button = Gtk.Template.Child('button')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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


def create_dataset_button_factory(name: str, label_name: str, description: str , image_resource: str):
    dataset_button = DatasetButton()
    dataset_button.init_widget(image_resource=image_resource, description=description, label_name=label_name, name=name)
    return dataset_button