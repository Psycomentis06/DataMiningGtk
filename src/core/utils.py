# import requests
from gi.repository import GLib, Gtk, Gdk, GdkPixbuf
import importlib

def load_image_from_url(url: str):
    response = requests.get(url)
    content = response.content

    loader = GdkPixbuf.PixbufLoader()
    loader.write_bytes(GLib.Bytes.new(content))
    loader.close()

    Gtk.Image.new_from_pixbuf(loader.get_pixbuf())

def get_filename_from_path(path: str):
    return path.split('/')[-1]

def remove_extention(filename: str):
    return filename.split('.')[0]

def import_module_from_abs_path(module_name: str, module_path: str):
    module_spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module

