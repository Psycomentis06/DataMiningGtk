from gi.repository import Gtk, Adw, GLib, GObject
from .entry_file import *

@Gtk.Template(resource_path = '/com/github/psycomentis/DataMiningGtk/gtk/dataset-window.ui')
class DatasetWindow(Adw.ApplicationWindow):

    __gtype_name__ = 'DatasetWindow'
    revealer_widget: Gtk.Revealer = Gtk.Template.Child('revealer')
    sidebar_toggle_btn_widget: Gtk.Button = Gtk.Template.Child('sidebar_toggle_btn')
    container: Gtk.Box = Gtk.Template.Child()
    # dataset_tree_view_widget: Gtk.TreeView = Gtk.Template.Child('dataset_tree_view')
    support_spin_button_widget: Gtk.SpinButton = Gtk.Template.Child('support_spin_button')
    tree_view_containe_widget: Gtk.Box = Gtk.Template.Child('tree_view_container')

    def __init__(self, dataset_name, **kwargs) -> None:
        super().__init__(**kwargs)
        self.dataset_name = dataset_name
        entry_file = EntryFile()
        dataset_config = entry_file.get_item_by_name(dataset_name)
        if dataset_config is None:
            # self.close()
            # super().close()
            self.destory()

    def init_widgets(self):
        self.revealer_widget.set_reveal_child(True)
        self.support_spin_button_widget.set_range(0.0, 100.0)
        self.support_spin_button_widget.set_increments(5.0, 5.0)
        # data = [
        #         {'id': '1', 'name': 'hello'},
        #         {'id': '2', 'name': 'hello'},
        #         {'id': '3', 'name': 'hello'},
        #         {'id': '4', 'name': 'hello'},
        #         {'id': '5', 'name': 'hello'},
        #         {'id': '6', 'name': 'hello'},
        #         {'id': '7', 'name': 'hello'}
        #         ]
        # store = Gtk.ListStore.new([GObject.TYPE_STRING, GObject.TYPE_STRING])
        # for i in range(len(data)):
        #     iterator = store.append()
        #     store.set(iterator, ['id', 'name'], [data[i]['id'], data[i]['name']])
        #
        # self.dataset_tree_view_widget.set_model(store)

        ''' 
           Steps to create a Gtk List View
           1- Create a GtkListStore
           2- Create a GtkTreeView
           3- Create a      GtkTreeViewColumn using GtkTreeView.append_column
           4- Create a          GtkCellRendererText using GtkTreeViewColumn.add_attribute

        data = {'id': [1,2,3,4,5], 'name': ['ali', 'penn', 'gayth', 'abc', 'def']}
        df = pd.DataFrame(data=data)
        store = Gtk.ListStore.new(df.dtypes)
        '''


    def update_required_properties(self):
        if (self.revealer_widget.get_reveal_child()):
        # Update icon
            self.sidebar_toggle_btn_widget.set_icon_name('pan-start-symbolic')
            self.container.set_spacing(20)
        else:
            self.sidebar_toggle_btn_widget.set_icon_name('pan-end-symbolic')
            GLib.timeout_add(self.revealer_widget.get_transition_duration(), self._update_revealer_spacing)

    def _update_revealer_spacing(self):
        self.container.set_spacing(0)
        # returns false to stop it from going in infinite loop
        return False

    @Gtk.Template.Callback()
    def dataset_sidebar_toggle(self, widget: Gtk.Button):
        self.revealer_widget.set_reveal_child(not self.revealer_widget.get_reveal_child())
        self.update_required_properties()


def create_dataset_window_factory(application: Gtk.Application, dataset_name):
    win = DatasetWindow(application=application, dataset_name=dataset_name)
    win.init_widgets()
    return win
