### DataMiningGtk

Simple Gtk4 app with python bindings for representing some pre stored datasets with the ability to play with the **Apriori** 
Algorithm's params.

##### Goals of this project

* Learn Gtk4 and libadwita
* Learn Apriori algorithm

This app is for learning purposes. nothing serious :)

##### How to build and install

###### Requirements 

**Python Packages**

- mlxtend

- PyGObject

- PyGObject-stubs

- pandas

- scikit-learn

- numpy

- matplotlib

- seaborn

- ipykernel

- openpyxl

**Gtk Sdk**

To download the SDK please refer to [Gtk's official download page](https://www.gtk.org/)

###### 1- Linux

Using *Flatpack*:

    $ flatpak-builder flatpak-build-dir com.github.psycomentis.DataMiningGtk.json --force-clean --user --install

build with:

    $ flatpak run com.github.psycomentis.DataMiningGtk//master

Using *Meson*:

    $ meson setup builddir
    $ cd builddir
    $ ninja
    $ ninja install


###### 2- Windows 

[Installing GTK4 apps on Windows](https://stdin.top/posts/gtk4-on-windows/) 

[Helpful link](https://test.www.collabora.com/news-and-blog/blog/2021/04/29/build-your-own-application-with-gtk4-as-a-meson-subproject/)