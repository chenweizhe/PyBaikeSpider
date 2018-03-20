#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-20 16:25:02 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-20 16:25:02 
 * @Desc:html解析器 
'''
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_cout):
        if page_url is None or html_cout is None:
            return
        soup = BeautifulSoup(html_cout,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)

        new_data = self._get_new_data(page_url,soup)

        return  new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # 格式 /item/xxx
        links = soup.find_all('a',href=re.compile(r"/item/(.*)"))
        for link in links:
            new_url = link['href']
            # 按照page_url的格式拼接全的url
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return  new_urls
    # 解析数据
    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        # //dd[@class='lemmaWgt-lemmaTitle-title']
        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        # //div[@class='lemma-summary']
        summary_node = soup.find('div',class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
        return  res_data
