Hacker-News-Applet
==================

A Python based [Hacker Bar][hacker-bar] clone for Ubuntu/GTK

Requires
-----

Python 3

PyGObject

      #In Ubuntu
      apt-get install python3-gi
     
AP Scheduler

     pip install apscheduler

[hacker-bar]: https://github.com/MohawkApps/Hacker-Bar
[hacker-news-api]: https://github.com/karan/HackerNewsAPI


###__Note:__ 
Due to [limitations in the GTK Indicator](http://askubuntu.com/questions/16431/putting-an-arbitrary-gtk-widget-into-an-appindicator-indicator) I am unable to implement this in the way I had planned using Python. If I ever do Qt I might be able to in C++ similar to Empathy menu. But for now, I am stuck with the current implementation. 
