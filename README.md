=====================================
imgscrapy - CLI Imgur Album Scraper
=====================================

How to install
------------
You would need to enter the following commands on Unix based  OSes:
```
sudo curl https://raw.githubusercontent.com/finix14/imgscrapy/master/img.py -o /usr/local/bin/img
sudo chmod a+r /usr/local/bin/img
```
Usage
------------
- Just copy the url of the imgur album and enter it in the terminal as:
```
 img http://imgur.com/gallery/5LHPAuk
```
- To change the default download location to say, "~/Imgur Dumps":
```
img -d "~/Imgur Dumps" 
```
  
Note:
------------
- Requests module needs to be installed for python. it can be installed by `pip install requests`.

- Scraper by default, downloads the pictures to `'~/{Default Download Location}/{Album Title}/'`.


