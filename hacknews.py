#!/usr/bin/env python2
__author__ = 'David Mitchell'

import glib
import gtk
import appindicator
from hn import HN
import sys
import webbrowser

basedir = sys.path[0]




#c = Config()

#set defaults
#config.setConfig(10, 5)
num_stories = 10
refresh_interval = 5


class HackerNewsIndicator:
    def __init__(self):
        self.wbhandle = webbrowser.get()
        self.load_settings()
        self.menu = gtk.Menu()
        self.indie = appindicator.Indicator("hacker-news-applet", basedir + "/art/hack-news-icon.svg",
                                 appindicator.CATEGORY_APPLICATION_STATUS)
        self.indie.set_status(appindicator.STATUS_ACTIVE)
        self.indie.set_attention_icon("connect_creating")

        # create a menu
        self.populate_menu(self.menu)

        #Set refresh
        glib.timeout_add(300000, self.handler_timeout)

    def handler_timeout(self):

        self.menu = gtk.Menu()
        self.populate_menu(self.menu)
        return True

    def load_settings(self):
        pass

    def menuitem_response(self, m, story):
        self.wbhandle.open_new(story["link"])
        return True

    def populate_menu(self, m):
        # create and populate menu
        hn = None
        hn = HN()
        for story in hn.get_stories()[:num_stories]:
            story_item = bytes.decode(story["title"])

            #point_item = Gtk.button(Label=story["points"])

            menu_item = gtk.MenuItem(story_item)

            m.append(menu_item)

            # this is where you would connect your menu item up with a function:

            menu_item.connect("activate", self.menuitem_response, story)

            # show the items
            menu_item.show()

        sep_item = gtk.SeparatorMenuItem()
        sep_item.show()
        m.append(sep_item)
        quit_item = gtk.MenuItem("Quit")
        quit_item.connect("activate", gtk.main_quit)
        quit_item.show()
        m.append(quit_item)

        self.indie.set_menu(m)

    def main(self):
        gtk.main()

if __name__ == "__main__":
    indie = HackerNewsIndicator()
    indie.main()
