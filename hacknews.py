#!/usr/bin/env python3
__author__ = 'David Mitchell'

from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator
from hn import HN
import sys
#from apscheduler.scheduler import Scheduler
import webbrowser

basedir = sys.path[0]




#c = Config()

#set defaults
#config.setConfig(10, 5)
num_stories = 10
refresh_interval = 5


class HackerNewsIndicator:
    def __init__(self):
        wbhandle = webbrowser.get()
        self.load_settings()
        self.menu = Gtk.Menu()
        self.indie = appindicator.Indicator.new(
            "hacker-news-applet",
            basedir + "/art/hack-news-icon.svg",
            appindicator.IndicatorCategory.APPLICATION_STATUS)
        self.indie.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.indie.set_attention_icon("connect_creating")

        # create a menu
        self.populate_menu(self.menu)


        #GLib.timeout_add(300000, self.handler_timeout)
#Setup refresh schedule
#sched = Scheduler()

#@sched.interval_schedule(minutes=refresh_interval)
    def handler_timeout(self):
        self.populate_menu(menu)

#sched.configure(options_from_ini_file)
#sched.start()

    def load_settings(self):
        pass

    def menuitem_response(self, story):
        self.wbhandle.open_new(story["link"])
        #print(story["link"])

    def populate_menu(self, m):
        # create and populate menu
        hn = None
        hn = HN()
        for story in hn.get_stories()[:num_stories]:
            story_item = bytes.decode(story["title"])

            #point_item = Gtk.button(Label=story["points"])

            menu_item = Gtk.MenuItem(story_item)

            m.append(menu_item)

            # this is where you would connect your menu item up with a function:

            menu_item.connect("activate", self.menuitem_response, story)

            # show the items
            menu_item.show()

        sep_item = Gtk.SeparatorMenuItem()
        sep_item.show()
        m.append(sep_item)
        quit_item = Gtk.MenuItem("Quit")
        quit_item.connect("activate", Gtk.main_quit)
        quit_item.show()
        m.append(quit_item)

        self.indie.set_menu(m)

    def main(self):
        Gtk.main()

if __name__ == "__main__":
    indie = HackerNewsIndicator()
    indie.main()
    #load_settings()
    #menu = Gtk.Menu()
    #indie = appindicator.Indicator.new(
    #    "hacker-news-applet",
    #    basedir + "/art/hack-news-icon.svg",
    #    appindicator.IndicatorCategory.APPLICATION_STATUS)
    #indie.set_status(appindicator.IndicatorStatus.ACTIVE)
    #indie.set_attention_icon("connect_creating")

    # create a menu
    #populate_menu(menu)


    #Gtk.main()