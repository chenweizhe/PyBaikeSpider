#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-20 16:23:27 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-20 16:23:27 
 * @Desc: 
'''


class UrlManager(object):


    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()


    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for url in new_urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0


    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return  new_url
