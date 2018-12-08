# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql as db
class Taobao1Pipeline(object):
	def __init__(self):
		self.con=db.connect(user="root",passwd="misxsol11",host="localhost",db="python",charset="utf8")
        self.cur=self.con.cursor()
        self.cur.execute('drop table taobao')
        self.cur.execute("create table taobao(id int auto_increment primary key,title varchar(200),price varchar(244),link varchar(244),deal_cnt varchar(200),location varchar(200))")

    def process_item(self, item, spider):
        self.cur.execute("insert into taobao(id,title,price,link,deal_cnt,location) values(NULL,%s,%s,%s,%s,%s)",(item['title'],item['price'],item['link'],item['deal_cnt'],item['location']))
        self.con.commit()
        return item

