from models.post import Post

__author__ = "DOW"

post = Post("post1 title", "post1 content", "post1 author")
post2 = Post("post2 title", "post2 content", "post2 author")

print(post.content)
print(post2.content)