import os

from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebView , QWebPage

from qtpyvcp.plugins import getPlugin

from probe_basic.probe_basic import ProbeBasic

STATUS = getPlugin('status')

class CustomProbeBasic(ProbeBasic):
    """Main window class for the ProbeBasic VCP."""
    def __init__(self, *args, **kwargs):
        super(CustomProbeBasic, self).__init__(*args, **kwargs)

        self.web_view = QWebView()
        self.web_view.setHtml('No setup sheet loaded.')
        self.web_view.setUrl(QUrl('file:////home/igor/totempole/NC-Files/1001.html'))
        self.tabWidget.insertTab(2, self.web_view, 'Setup Sheet')

        STATUS.file.notify(self.onFileLoaded)

    def onFileLoaded(self, fpath):
        root, ext = os.path.splitext(fpath)
        path = os.path.abspath(root) + '.html'

        if os.path.isfile(path):
            self.web_view.setUrl(QUrl('file://' + path))

        else:
            self.web_view.setHtml('No setup sheet found for: {}'.format(path))
