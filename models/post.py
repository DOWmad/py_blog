__author__ = "DOW"

#from the database file import the class Database
from database import Database
import uuid
import pytz
import datetime
time = pytz.timezone('Europe/London').localize(datetime.datetime.now())
#fmt = '%m-%d %H:%M %Z%z'


class Post(object):

    #fuction that is first called.
    #only set default value at end.
    def __init__(self,blog_id,title,content,author,date=time,id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        #generates unique id if no id is passed
        self.id = uuid.uuid4().hex if id is None else id

 #Connect to db and add data
    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json())

#return json format data
    def json(self):
        return {
            'id':self.id,
            'blog_id':self.blog_id,
            'author':self.author,
            'content':self.content,
            'title':self.title,
            'created_date': self.created_date
        }

#function to pull specific post from db
    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='blogs', query={'id': id})
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['created_date'],
                   id=post_data['id'])

#function to pull all posts of given blog_id and store in list.
    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts',query={'blog_id':id})]