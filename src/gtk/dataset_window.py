from gi.repository import Gtk, Adw, GLib 

@Gtk.Template(resource_path = '/com/github/psycomentis/DataMiningGtk/gtk/dataset-window.ui')
class DatasetWindow(Adw.ApplicationWindow):

    __gtype_name__ = 'DatasetWindow'
    revealer_widget: Gtk.Revealer = Gtk.Template.Child('revealer')
    sidebar_toggle_btn_widget: Gtk.Button = Gtk.Template.Child('sidebar_toggle_btn')
    container: Gtk.Box = Gtk.Template.Child()

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def init_widgets(self):
        self.revealer_widget.set_reveal_child(True)

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


def create_dataset_window_factory(application: Gtk.Application):
    win = DatasetWindow(application=application)
    win.init_widgets()
    return win