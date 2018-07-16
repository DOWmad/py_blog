import pymongo

class Database(object):
    uri = "mongodb://127.0.0.1:27017"
    DATABASE = None


    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.uri)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
       Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, data):
        Database.DATABASE[collection].find(data)

    @staticmethod
    def find_one(collection, data):
       Database.DATABASE[collection].find_one(data)
