#!/usr/bin/env python3
__author__ = 'David Mitchell'

from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator
from hn import HN
from apscheduler.scheduler import Scheduler
import webbrowser


hn = HN()
wbhandle = webbrowser.get()

#Setup refresh schedule
sched = Scheduler()

@sched.interval_schedule(minutes=5)
def refresh_list():
    populate_menu()

#sched.configure(options_from_ini_file)
sched.start()

def menuitem_response(w, story):
    wbhandle.open_new(story["link"])
    #print(story["link"])


def populate_menu():
    menu = Gtk.Menu()

    # create some
    for story in hn.get_stories()[:10]:
        item = bytes.decode(story["title"])

        menu_items = Gtk.MenuItem(item)

        menu.append(menu_items)

        # this is where you would connect your menu item up with a function:

        menu_items.connect("activate", menuitem_response, story)

        # show the items
        menu_items.show()

    ind.set_menu(menu)

if __name__ == "__main__":
    ind = appindicator.Indicator.new (
                        "hacker-news-applet",
                        "empathy-available",
                        appindicator.IndicatorCategory.APPLICATION_STATUS)
    ind.set_status (appindicator.IndicatorStatus.ACTIVE)
    ind.set_attention_icon ("account-logged-in")

    # create a menu
    populate_menu()


    Gtk.main()