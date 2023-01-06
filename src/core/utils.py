import requests
from gi.repository import GLib, Gtk, Gdk, GdkPixbuf

def load_image_from_url(url: str):
    response = requests.get(url)
    content = response.content

    loader = GdkPixbuf.PixbufLoader()
    loader.write_bytes(GLib.Bytes.new(content))
    loader.close()

    Gtk.Image.new_from_pixbuf(loader.get_pixbuf())

    
