# blog_project
A simple website for a blog.

Main Technologies: Python + Django

Functionalities: <br/>
-Allow a user to create a draft of a post <br/>
--Allow user to either delete it or publish it (Posts will not be shown unless published by the author <br/>

-On a published post, visitors can comment on it, login is needed to post <br/>
--Comments will need to be approved by the author of the post before being open to viewing <br/>
---Comment that isn't approved can also be removed by the author <br/>

Still in Work: <br/>
-Removal of Post by the author is still in progress. <br/>
--Current Issue: Trying to remove a post, create an error of: <br/>
  TypeError at /post/4/remove/ <br/>
    'str' object is not callable <br/>
