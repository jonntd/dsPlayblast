import os
import logging
from PySide2 import QtWidgets
import qdarkstyle
from dsPlayblast import playblastUI
from dsPlayblast import loggingFn


def main():
    # Init application
    app = QtWidgets.QApplication(os.sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyside2"))

    # Logging
    loggingFn.setup_logging()
    LOGGER = logging.getLogger(__name__)

    # Init interface
    mainWindow = playblastUI.PlayblastWindow()
    mainWindow.show()

    os.sys.exit(app.exec_())


main()
