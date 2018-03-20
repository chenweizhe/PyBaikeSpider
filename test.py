#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-20 00:50:34 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-20 00:50:34 
 * @Desc: 
'''

import urllib2, cookielib
url='http://www.baidu.com'
print('第一种方法')
response1 = urllib2.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print('第二种方法')
request = urllib2.Request(url)
request.add_header('user-agent','Mozilla/5.0')
response2 = urllib2.urlopen(url)
print(response2.getcode())
print(len(response2.read()))


print('第三种方法')
sj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(sj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print(response3.getcode())
print(sj)
print(response3.read())
