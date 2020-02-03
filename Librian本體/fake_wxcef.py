# -*- coding: utf-8 -*-

import logging
import platform
import urllib

from PySide2 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, QtWebChannel


def group(url, icon, title, size):
    app = QtApp(url, icon, title, size)
    return app, app.frame.browser


def main():
    check_versions()


def check_versions():
    logging.debug("[PySide2.py] Python {ver} {arch}".format(
        ver=platform.python_version(), arch=platform.architecture()[0]))


class CefBrowser:
    def __init__(self, webPage: QtWebEngineWidgets.QWebEnginePage):
        self._webPage = webPage

    def ExecuteJavascript(self, source):
        self._webPage.runJavaScript(source)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, url, icon, title, size):
        super().__init__()

        logging.debug("[PySide2.py] MainWindow DPI scaled size: %s" %
                      str(size))
        width, height = tuple(size)
        self.resize(width, height)

        ic = QtGui.QIcon(icon)
        self.setWindowIcon(ic)

        self.setWindowTitle(title)

        self._webView = QtWebEngineWidgets.QWebEngineView(parent=self)
        self._webChannel = QtWebChannel.QWebChannel(parent=self._webView)
        self._webPage = self._webView.page()
        self._webPage.setWebChannel(self._webChannel)
        self.setCentralWidget(self._webView)
        self.embed_browser(url)

        self.browser = CefBrowser(self._webPage)

    def embed_browser(self, url: str):
        self._webView.load(QtCore.QUrl(url))

    def set_browser_object(self, name: str, obj: QtCore.QObject):
        self._webChannel.registerObject(name, obj)

    def setFocus(self):
        self._webView.setFocus()

    def toggleFullScreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()


class QtApp(QtWidgets.QApplication):
    def __init__(self, url, icon, title, size):
        super().__init__([])
        self.url, self.icon, self.title, self.size = url, icon, title, size
        self.frame = MainWindow(self.url, self.icon, self.title, self.size)
        self.frame.show()

    def MainLoop(self):
        self.exec_()


if __name__ == '__main__':
    main()
