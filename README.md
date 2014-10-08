Hacker-News-Applet
==================

A Python based [Hacker Bar][hacker-bar] clone for Ubuntu/GTK

Requires
-----

Python 3

PyGObject

      #In Ubuntu
      apt-get install python3-gi
      
Install python requirements

      pip install -r requirements.txt


[hacker-bar]: https://github.com/MohawkApps/Hacker-Bar
[hacker-news-api]: https://github.com/karan/HackerNewsAPI


###__Note:__ 
If you want a Python 2.7+ version, I have a [separate branch for Python 2](https://github.com/digital-shokunin/Hacker-News-Applet/tree/python2)

Due to [limitations in the GTK Indicator](http://askubuntu.com/questions/16431/putting-an-arbitrary-gtk-widget-into-an-appindicator-indicator) I am unable to implement this in the way I had planned using GTK library. However, I have a Qt implementation I am working on, it is located in the [Qt branch](https://github.com/digital-shokunin/Hacker-News-Applet/tree/qt), once I have it to about the same point of functionality I may merge it into the main branch and replace the GTK version.
