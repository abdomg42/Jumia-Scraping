# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JumiatvPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # name without extra information
        name  = adapter.get("name")
        names = name.split('-')
        adapter['name'] = names[0]

        # number of stars 
        nStars = adapter.get("n_stars")
        if '(' in nStars :
            temp1 = nStars.split("(")
            nStars = temp1[1].split(' ')[0]
            adapter['n_stars'] = int(nStars)
        else : 
            adapter['n_stars'] = 0

        # price float without Dhs
        
        price_non_modifiyable = adapter.get("price")
        if ',' in price_non_modifiyable : 
            price_non_modifiyable = price_non_modifiyable.replace(',','')
        price_updated = price_non_modifiyable.split(' ')[0]
        adapter["price"] = float(price_updated)


        return item

#import mysql.connector
import sqlite3

class SavetoMysql : 
    def __init__(self):
        self.create_connection()
        self.create_table()


    def create_connection(self):
        self.conn = sqlite3.connect("myArticle.db")
            # host = 'localhost',
            # user = 'root',
            # database = 'jumia'
        
        #create cursor to execute command
        self.curr = self.conn.cursor()

    def create_table(self):
            self.curr.execute("create table if not exists jumia_db(id integer auto_increment primary key, name text,marque text, price decimal,n_stars integer,sku text)")

    def process_item(self, item, spider) :
        #insert into table 
        self.store_db(item)
        return item
           
    def store_db(self,item):
            self.curr.execute(""" 
                          insert into jumia_db(
                          name,
                          marque,
                          price,
                          n_stars,
                          sku
                          ) values (
                            ?,
                            ?,
                            ?,
                            ?,
                            ?)""",(
                                item["name"],
                                item["marque"],
                                item["price"],
                                item["n_stars"],
                                item["sku"],
                            ))   
            self.conn.commit()
#def close_spider(self, spider):
        
        # self.curr.close()
        # self.conn.close()