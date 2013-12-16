__author__ = 'David Mitchell'


import sys
from PyQt4 import QtGui
from hn import HN
import webbrowser

basedir = sys.path[0]

wbhandle = webbrowser.get()

num_stories = 10
refresh_interval = 5

def menuitem_response(story):
    wbhandle.open_new(story["link"])

def populate_menu(m):
    # create and populate menu
    hn = HN()
    for story in hn.get_stories()[:num_stories]:
        story_item = bytes.decode(story["title"])
        m.addAction(story_item)

app = QtGui.QApplication([])
icon = QtGui.QSystemTrayIcon(QtGui.QIcon(basedir + "/art/hack-news-icon.svg"), app)
menu = QtGui.QMenu()
populate_menu(menu)
menu.addAction("Quit", QtGui.qApp.quit)
icon.setContextMenu(menu)
icon.show()
app.exec_()
