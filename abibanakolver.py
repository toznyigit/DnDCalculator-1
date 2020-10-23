from __future__ import print_function
import os
import sys
import random
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
import urllib2, sys
from HTMLParser import HTMLParser
#import requests
appendlist = []

class MyHTMLParser(HTMLParser):
    global count
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        attr = dict(attrs)
        if "galleries" in attr.get("href"):
            appendlist.append(attr.get("href"))

def rebuildExtract(link,tag):
    del appendlist[:]
    newlist = []

    p = urllib2.urlopen(link)
    html = p.read()
    p.close()

    parser = MyHTMLParser()
    parser.feed(html)
    
    for item in appendlist:
        if item in newlist: continue
        newlist.append(item)

    f = open("/media/Delta/XFile/ReBuild/"+tag,"a+")
    for item in newlist:
        f.write(item+"\n")
    f.close()

def listGrabber(rank,main):
    master = main+"/pornstar/"
    exceptions = []
    exceptList = []
    output = ""

    sourceFile = open("/media/Delta/XFile/ReBuild/fav.txt","r")

    for line in sourceFile:
        exceptFlag = False
        if int(rank) == line.count("#"):
            source = line.split('#')[0]
            for excepts in exceptions:
                if excepts in line:
                    exceptFlag = True
                    exceptList.append(source)
            
            if exceptFlag == False:
                output = master
                i = 1
                parse = source.split(" ")
                for part in parse:
                    output = output + part.lower()
                    if i<len(parse):
                        output = output + "-"
                        i += 1
                output = output + "/"

                print(source+" :: "+output)
                for i in range(1):
                    #rebuildExtract(output+str(i+1)+"/",source)
                    rebuildExtract(output,source)
                    if len(appendlist) == 0:
                        break
                        
rank = input("Choose rank between 1 to 4: ")
listGrabber(rank,'http://www.'+sys.argv[1])
