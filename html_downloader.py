#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-20 16:25:19 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-20 16:25:19 
 * @Desc: html下载器
'''
import urllib2


class HtmlDownloader(object):


    def download(self, url):
        if url is None:
            return  None

        # 超时检测
        if url is not None:
            try:
                response = urllib2.urlopen(url,timeout=10)
                if response.getcode() == 200:
                    return response.read()
                else:
                    return  None
            finally:
                pass







