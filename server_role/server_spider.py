# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import server_url_manager
import server_downloader
import server_parser
import add_role
import traceback
from threading import Timer

class ServerSpider(object):
    def __init__(self):
        self.urls = server_url_manager.UrlManager()
        self.downloader = server_downloader.HtmlDownloader()
        self.parser = server_parser.HtmlParser()
        self.store = add_role.Role()

    def craw(self):
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw :' + new_url)
                html_cont = self.downloader.download(new_url)
                new_data = self.parser.parse(html_cont)
                self.store.addRoles(new_data)
            except Exception as e:
                print(e, traceback.print_exc())

if __name__ == "__main__":
    obj_spider = ServerSpider()
    for sch in range(10):
        for page in range(10):
            url = "http://tx3.cbg.163.com/cgi-bin/overall_search.py?act=overall_search_role&level_min=69" \
                  "&level_max=80&price_min=100000&price_max=30000000&" \
                  "school=" + str(sch + 1) + "&page=" + str(page+1) + "&order_by=price DESC"
            obj_spider.urls.add_new_url(url)

    obj_spider.craw()