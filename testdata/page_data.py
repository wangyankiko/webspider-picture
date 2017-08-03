#!usr/bin/python
#coding = utf-8

#from a url that we can download picture
picture_url = 'https://book.douban.com/'

#the pattern of picture
img_pattern = r'src="(http.+?\.jpg)"'
#count
count = 0