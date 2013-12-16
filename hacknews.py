#!/usr/bin/env python3
__author__ = 'David Mitchell'
__version__ = "0.1.5"

from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator
from hn import HN
from apscheduler.scheduler import Scheduler
import webbrowser
import sys

hn = HN()
basedir = sys.path[0]
print(basedir)
wbhandle = webbrowser.get()

#set defaults
num_stories = 10
refresh_interval = 5

#Setup refresh schedule
sched = Scheduler()

#sched.configure(options_from_ini_file)
sched.start()

@sched.interval_schedule(minutes=refresh_interval)
def refresh_list():
    m = Gtk.Menu()
    populate_menu(m)


def load_settings():
    pass


def menuitem_response(w, story):
    wbhandle.open_new(story["link"])


def populate_menu(m):
    # create and populate menu
    for story in hn.get_stories()[:num_stories]:
        story_item = bytes.decode(story["title"])

        #point_item = Gtk.button(Label=story["points"])

        menu_item = Gtk.MenuItem(story_item)

        m.append(menu_item)

        # this is where you would connect your menu item up with a function:

        menu_item.connect("activate", menuitem_response, story)

        # show the items
        menu_item.show()

    indie.set_menu(m)

if __name__ == "__main__":
    load_settings()
    menu = Gtk.Menu()
    indie = appindicator.Indicator.new(
        "hacker-news-applet",
        basedir + "/art/hack-news-icon.svg",
        appindicator.IndicatorCategory.APPLICATION_STATUS)
    indie.set_status(appindicator.IndicatorStatus.ACTIVE)
    indie.set_attention_icon("connect_creating")

    # create a menu
    populate_menu(menu)

    Gtk.main()