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
The script won't work if imgur does not send the zip file (which is the case with huge albums). The script however works well for albums containing ~100 pics. It fetches the zip file for the album and extracts it to '~/Imgur Dumps/{Album Title}/'


