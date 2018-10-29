# blog_project
A simple website for a blog.

Main Technologies: Python + Django

Functionalities:
-Allow a user to create a draft of a post
--Allow user to either delete it or publish it (Posts will not be shown unless published by the author

-On a published post, visitors can comment on it, login is needed to post
--Comments will need to be approved by the author of the post before being open to viewing
---Comment that isn't approved can also be removed by the author

Still in Work:
-Removal of Post by the author is still in progress.
--Current Issue: Trying to remove a post, create an error of:
  TypeError at /post/4/remove/
    'str' object is not callable
