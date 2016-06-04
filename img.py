#!/usr/bin/env python
from subprocess import call
import sys,os, re, getpass, requests
call(['rm', '-f' , 'zip'])
html=requests.get(sys.argv[1]).text
rex=re.compile('<title>\s+(.*) - Album on Imgur</title>')
title=rex.search(html).group(1)
u=sys.argv[1][-5:]
dwn='http://s.imgur.com/a/' + u + '/zip'
dir= '/home/' + getpass.getuser() + '/Imgur Dumps/' + title
print dir
print dwn
call(["wget", dwn])
call(["mkdir",'-p',dir])
call(['mv', 'zip', dir])
os.chdir(dir)
#call(['cd', dir])
call(["unzip", "zip"])
call(['rm', 'zip'])
