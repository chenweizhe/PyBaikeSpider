#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''
 * @Author: PythonZhe 
 * @Date: 2018-03-20 16:26:11 
 * @Last Modified by:   PythonZhe 
 * @Last Modified time: 2018-03-20 16:26:11 
 * @Desc: 将抓取的结果保存到这里
'''


class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)




    def output_html(self):
        fout = open('output.html','w')
        fout.write("<html>")
        fout.write("<meta charest='utf-8'>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s<td>" % data['url'])
            fout.write("<td>%s<td>" % data['title'].encode('utf-8'))

            fout.write("<td>%s<td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
