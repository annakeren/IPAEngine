'''
Created on 28 Jun 2015

@author: annakeren
'''
from pymongo import MongoClient

class MongoPersistence(object):
    '''
    classdocs
    '''

@staticmethod 
    def connect(params):
        host = params[0]
        port = params[1]
        client = MongoClient(host, port)
        db = client.ipa_engine
        return db
    
@staticmethod
    def insert(db, post):
        posts = db.posts
        posts.insert_one(post)
        return posts
