=====================================
imgscrapy - Linux CLI Imgur Album Scraper
=====================================

How to install
------------
You would need to enter the following commands on Unix based  OSes:
```
 $ sudo curl https://raw.githubusercontent.com/finix14/imgscrapy/master/img -o /usr/local/bin/img
 $ sudo chmod a+rx /usr/local/bin/img
```
Usage
------------
Just copy the url of the imgur album and enter it in the terminal as:
```
 $ img http://imgur.com/gallery/5LHPAuk
```
  
Note:
------------
-requests module needs to be installed for python. it can be installed by `pip install requests`.

-Scraper downloads the pictures to '~/Imgur Dumps/{Album Title}/'


