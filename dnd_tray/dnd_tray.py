#!/usr/bin/env python3

import sys
import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class App:
    def __init__(self):
        self._state = "on"
        self.app = QApplication(sys.argv)
        notif_on_icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "noti_on.png")
        notif_off_icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "noti_off.png")
        self._icons = {"on": notif_on_icon_path, "off": notif_off_icon_path}
        icon = QIcon(self._icons.get(self._state))
        menu = QMenu()
        exitAction = menu.addAction("exit")
        exitAction.triggered.connect(sys.exit)

        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.show()
        self.tray.activated.connect(self._toggle_dnd)


    def _toggle_dnd(self, reason):
        off_message = "DUNST_COMMAND_PAUSE"
        on_message = "DUNST_COMMAND_RESUME"
        if reason == QSystemTrayIcon.Trigger:
            if self._state == "on":
                os.system('notify-send "{}"'.format(off_message))
                self._state = "off"
            else:
                os.system('notify-send "{}"'.format(on_message))
                self._state = "on"

            icon_path = self._icons.get(self._state)
            icon = QIcon(icon_path)
            self.tray.setIcon(icon)

    def run(self):
        # Enter Qt application main loop
        self.app.exec_()
        sys.exit()


if __name__ == "__main__":
    app = App()
    app.run()
