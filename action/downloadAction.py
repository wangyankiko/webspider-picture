from testdata import page_data
import urllib
import re
import os

#method of get the page of html

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#method of download the imglist
def downloadImg(html,img_pattern):

    imgre = re.compile(img_pattern,re.I)
    imglist = re.findall(imgre, html)
    if not imglist:
        print 'not found'
    else:
        return imglist

#method of define the filepath
def defineFilePath():

    file_path = os.getcwd() + '/picture'

    if not os.path.exists(file_path):
        os.mkdir(file_path)

    return file_path

#define the download process
def schedule(a,b,c):
    per=100.0*a*b/c
    if per>100:
        per=100
    print '%0.2f%%'%per

#method of doenloading picture to local dir

def saveImgLocal(imglist,file_path,x):

    count = x
    if not imglist:
        exit(0)
    for imgUrl in imglist:
        target_dir = file_path+'/%s.jpg' % count
        print "Downing the image to "+target_dir
        image = urllib.urlretrieve(imgUrl, target_dir, schedule)

        count += 1

    return count



