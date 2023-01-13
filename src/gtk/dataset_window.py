from gi.repository import Gtk, Adw, GLib, GObject, Gio
import importlib
from importlib.machinery import SourceFileLoader
import sys
from .utils import *
from .file_system import *
from .entry_file import *
from time import sleep

@Gtk.Template(resource_path = '/com/github/psycomentis/DataMiningGtk/gtk/dataset-window.ui')
class DatasetWindow(Adw.ApplicationWindow):

    __gtype_name__ = 'DatasetWindow'
    revealer_widget: Gtk.Revealer = Gtk.Template.Child('revealer')
    sidebar_toggle_btn_widget: Gtk.Button = Gtk.Template.Child('sidebar_toggle_btn')
    container: Gtk.Box = Gtk.Template.Child()
    min_support_spin_button_widget: Gtk.SpinButton = Gtk.Template.Child('min_support_spin_button')
    min_conf_spin_button_widget = Gtk.Template.Child('min_conf_spin_button')
    tree_view_container_widget: Gtk.Box = Gtk.Template.Child('tree_view_container')
    selectable_dropdown_widget: Gtk.DropDown = Gtk.Template.Child('selectable_dropdown')
    set_subject_value_button_widget = Gtk.Template.Child('set_subject_value_btn')
    get_frequent_items_btn_widget = Gtk.Template.Child('get_frequent_items_btn')
    get_rules_btn_widget = Gtk.Template.Child('get_rules_btn')
    max_length_spin_button_widget = Gtk.Template.Child('max_length_spin_button')
    low_memory_switch_widget = Gtk.Template.Child('low_memory_switch')


    def __init__(self, dataset_name, **kwargs) -> None:
        super().__init__(**kwargs)
        self.tree_view = None
        self.dataset_name = dataset_name
        entry_file = EntryFile()
        dataset_config = entry_file.get_item_by_name(dataset_name)
        if dataset_config is not None:
            self.close()
        # should append the path of python packages folder in a flatpak app
        # todo: check system installed python versoin automatically
        sys.path.append('/home/psycomentis06/.local/lib/python3.10/site-packages/')
        # import dataset extension class
        module_path = dataset_config['module_path']
        file_name = get_filename_from_path(module_path)
        dataset_module = import_module_from_abs_path(file_name, module_path)
        # dataset_module = SourceFileLoader(file_name, module_path).load_module()
        dataset_class = getattr(dataset_module, dataset_config['class_name'])
        self.dataset_obj = dataset_class()


    def init_widgets(self):
        self.revealer_widget.set_reveal_child(True)
        self.set_subject_value_button_widget.hide()
        self.get_frequent_items_btn_widget.hide()
        self.get_rules_btn_widget.hide()
        # self.selectable_dropdown_widget.set_enable_search(True)
        # self.support_spin_button_widget.set_range(0.0, 100.0)
        # self.support_spin_button_widget.set_increments(5.0, 5.0)

    def render_dataset_table(self, df):
        ''' 
           Steps to create a Gtk List View
           1- Create a GtkListStore
           2- Create a GtkTreeView
           3- Create a      GtkTreeViewColumn using GtkTreeView.append_column
           4- Create a          GtkCellRendererText using GtkTreeViewColumn.add_attribute
        '''
        list_store_cols = list_store_col_types(df)
        store = Gtk.ListStore.new(list_store_cols)
        df = dataframe_stringify_cols(df)
        data = df.to_records(index=True)
        for row in data:
            store.append(list(row))
        tree_view = Gtk.TreeView.new_with_model(store)
        renderer = Gtk.CellRendererText.new()
        index_col_name = 'Index'
        if not df.index.name is None:
            index_col_name = df.index.name
        tree_view.append_column(self._create_column(index_col_name, 0, renderer))
        index = 1
        for col in df.columns:
            column = self._create_column(col, index, renderer)
            tree_view.append_column(column)
            index = index + 1
        self.tree_view_container_widget.append(tree_view)
        self.tree_view = tree_view

    def _create_column(self, title, index, renderer):
        column = Gtk.TreeViewColumn.new()
        column.set_title(title)
        column.pack_start(renderer, True)
        column.add_attribute(renderer, 'text', index)
        return column


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

    def render_selectable_widget(self):
        choices = self.dataset_obj.get_selectable_values()
        string_list = Gtk.StringList.new(choices)
        self.selectable_dropdown_widget.set_model(string_list)

    def clear_tree_view(self):
        self.tree_view_container_widget.remove(self.tree_view)
        self.tree_view = None


    @Gtk.Template.Callback()
    def dataset_sidebar_toggle(self, widget: Gtk.Button):
        self.revealer_widget.set_reveal_child(not self.revealer_widget.get_reveal_child())
        self.update_required_properties()

    @Gtk.Template.Callback()
    def load_dataset_handler(self, widget: Gtk.Button):
        self.dataset_obj.load_dataset()
        self.render_dataset_table(self.dataset_obj.get_dataframe())
        self.render_selectable_widget()
        self.tree_view_container_widget.remove(widget)
        self.set_subject_value_button_widget.show()

    @Gtk.Template.Callback()
    def set_subject_value_handler(self, widget):
        selectable_index = self.selectable_dropdown_widget.get_selected()
        self.clear_tree_view()
        choices = self.dataset_obj.get_selectable_values()
        selectable_value = choices[selectable_index]
        self.dataset_obj.set_subject(selectable_value)
        self.render_dataset_table(self.dataset_obj.get_subject_data())
        self.get_frequent_items_btn_widget.show()
        self.get_rules_btn_widget.show()


    @Gtk.Template.Callback()
    def get_frequent_items_handler(self, widget):
        min_support = self.min_support_spin_button_widget.get_value() / 100.0
        max_length = self.max_length_spin_button_widget.get_value()
        low_memory = self.low_memory_switch_widget.get_active()

        if max_length == -1:
            max_length = None
        
        for col in self.dataset_obj.get_subject_data().columns:
            self.dataset_obj.get_subject_data()[col]= self.dataset_obj.get_subject_data()[col].astype(int)
        # train_df = self.dataset_obj.get_frequent_items(min_support, min_conf, low_memory, max_length)
        self.dataset_obj.extract_frequent_items(min_support = min_support, low_memory=low_memory, max_len=max_length)
        self.clear_tree_view()
        self.render_dataset_table(self.dataset_obj.get_frequent_items())



    @Gtk.Template.Callback()
    def get_rules_handler(self, widget):
        min_conf = self.min_conf_spin_button_widget.get_value() / 100.0
        self.dataset_obj.get_frequent_items()['support'] = self.dataset_obj.get_frequent_items()['support'].astype(float)
        self.dataset_obj.extract_rules(min_confidence=min_conf)
        self.clear_tree_view()
        self.render_dataset_table(self.dataset_obj.get_rules())


def create_dataset_window_factory(application: Gtk.Application, dataset_name):
    win = DatasetWindow(application=application, dataset_name=dataset_name)
    win.init_widgets()
    return win
