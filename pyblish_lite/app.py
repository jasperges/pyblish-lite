import os
import sys
import contextlib

from Qt import QtWidgets, QtGui

from . import control


@contextlib.contextmanager
def application():
    app = QtWidgets.qApp.instance()

    if not app:
        app = QtWidgets.QApplication(sys.argv)
        yield
        app.exec_()
    else:
        yield


def install_fonts():
    fontdir = os.path.join(os.getcwd(), "font", "opensans")

    database = QtGui.QFontDatabase()
    for font in ("OpenSans-Regular.ttf",
                 "OpenSans-SemiBold.ttf"):
        database.addApplicationFont(
            os.path.join(fontdir, font))


def show(parent=None):
    os.chdir(os.path.dirname(__file__))

    with open("app.css") as f:
        css = f.read()

    with application():
        install_fonts()

        window = control.Window(parent)
        window.resize(400, 600)
        window.setStyleSheet(css)
        window.show()

        window.prepare_reset()

        return window