import pymongo

class Database(object):

    #set mongodb connection
    uri = "mongodb://127.0.0.1:27017"

    #initialise db variable
    DATABASE = None


    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.uri)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
       return Database.DATABASE[collection].find_one(query)
