#!/usr/bin/env python
from subprocess import call
import sys,os,re,getpass,requests,json,pickle
directory = '~/.imgscrapy'
if len(sys.argv) == 2:
    if not os.path.exists(os.path.expanduser(directory)):
        os.makedirs(os.path.expanduser(directory))
    os.chdir(os.path.expanduser(directory))
    try:
        filehandler = open('default_dir.pkl','r')
        dir = pickle.load(filehandler)
    except:
        print "[!] Default Download Location not set."
        dir = raw_input('[!] Input the default location: ').strip("\'\" ")
        pickle_file = open('default_dir.pkl','w')
        pickle.dump(dir,pickle_file)
elif len(sys.argv) == 3:
    if sys.argv[1] == '-d':
        pickle_file = open('default_dir.pkl','w')
        pickle.dump(sys.argv[2],pickle_file)
        print '\n\n[+] Default download location set to "%s"' % sys.argv[2]
        sys.exit()
    dir = sys.argv[2]

dir = os.path.expanduser(dir)

if len(sys.argv) == 1:
    print "\n[-] ERROR: Not enough parameters supplied"
    sys.exit()

try:
    html = requests.get(sys.argv[1]).text
except:
    print "\n[-] ERROR: Invalid URL"
    sys.exit()
title=re.search('<title>\s+(.*) - (?:Album on )?Imgur</title>',html).group(1)
album_code = sys.argv[1].split('/')[4]
downloads = 'http://imgur.com/ajaxalbums/getimages/%s/hit.json?all=true' % album_code

dir = os.path.join(dir,title) 

if not os.path.exists(dir):
       os.makedirs(dir)
os.chdir(dir)
print '\n\n[+] Downloading to %s\n\n' % dir
data = json.loads(requests.get(downloads).text)
try:
    images = data['data']['images']
except:
    print "[-] ERROR: No Images Found"
    sys.exit()
img_url = ''
with open( 'list.txt', 'w') as file:
    for img in images:
        if img['ext'] == '.gif':
            img['ext'] = '.mp4'
        filename = img['hash'] + img['ext']
        img_url += 'http://i.imgur.com/%s\n' % filename
    file.write(img_url)
os.system("wget -ci list.txt -nv; rm list.txt")
print "[+] Completed Downloading"
