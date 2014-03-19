# -*- coding: utf-8 -*-
__author__ = 'Dazdingo'

from common.dao.book_dao import book_dao
from common.model.book import Book
#import pymongo

class Pipeline(object):
    #con = pymongo.Connection("localhost", 27017)
    #db = con.bestbuyer
    def process_item(self, item, spider):
        if(len(item['ISBN']) == 0):
            return item
        newbook = Book()
        newbook.title = item["name"][0]
        newbook.price = item["instant"][0]
        newbook.isbn = item["ISBN"][0]
        newbook.author = item["author"][0]
        newbook.press = item["press"][0]
        newbook.instant_price = item["price"][0]
        newbook.link = item["url"]
        newbook.cover = item["img"][0]
        if len(item["description"]) != 0 :
            newbook.description = item["description"][0]
        newbook.platform = item['platform']
        #newbook.time = ?
        book_dao.insert(newbook)
    #def process_item(self, item, spider):
    #    if(len(item['ISBN']) == 0):
    #    	return item
    #    dbdata = {"name":"","price":"","ISBN":"","author":"","press":"","img":"","description":""}
    #    dbdata["name"] = item["name"][0]
    #    dbdata["price"] = item["price"][0]
    #    dbdata["ISBN"] = item["ISBN"][0]
    #    dbdata["author"] = item["author"][0]
    #    dbdata["press"] = item["press"][0]
    #    dbdata["img"] = item["img"][0]
    #    dbdata["description"] = item["description"]
    #    self.db.bookInfo.insert(dbdata)
    #    return item