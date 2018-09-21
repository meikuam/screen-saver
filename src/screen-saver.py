import os
import sys
sys.path.insert(1, os.path.abspath(".."))
from src.utils.cam import cam_caputre

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib


def get_root_dir():
    return os.path.abspath('..')

def handler(sender=None):
    path = get_root_dir() + '/data/photos/'
    if sender == 0:
        cam_caputre(path)
        print('agaaaa')


def __main():


    dbus_loop = DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()

    session_bus = dbus.SessionBus(mainloop=dbus_loop)
    session_bus.add_signal_receiver(handler, 'ActiveChanged', 'org.gnome.ScreenSaver', path='/org/gnome/ScreenSaver')
    session_bus.add_signal_receiver(handler, 'ActiveChanged', 'com.canonical.Unity.Session', path='/com/canonical/Unity/Session')

    loop.run()

if __name__ == '__main__':
    __main()
