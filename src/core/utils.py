# import requests
from gi.repository import GLib, Gtk, Gdk, GdkPixbuf, GObject
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

def pandas_columns_types(df):
    types_list = []
    for col_name in df.columns:
        col_type = df.dtypes[col_name]
        if col_type == 'int64':
            types_list.append(GObject.TYPE_INT64)
        elif col_type == 'object':
            types_list.append(GObject.TYPE_STRING)
        elif col_type == 'float':
            types_list.append(GObject.TYPE_FLOAT)
    return types_list

def list_store_col_types(df):
    # 1 for the index column
    cols_number = df.shape[1] + 1
    return [GObject.TYPE_STRING for x in range(cols_number)]

def dataframe_stringify_cols(df):
    for col in df.columns:
        if not df.dtypes[col] == 'string':
            df[col] = df[col].astype(str)
    df.index = df.index.astype(str)
    return df

