from django.db import models
from django.contrib.auth.models import User
from mainapp.helpers import get_book_title
from django.utils.timezone import now

import BookRecSystem.settings as settings
import pandas as pd
import os

book_path = os.path.join(settings.STATICFILES_DIRS[0] + '/mainapp/dataset/books.csv')
df_book = pd.read_csv(book_path)


class UserRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rating')
    bookid = models.IntegerField()
    bookrating = models.IntegerField()

    def __str__(self):
        return self.user.username.capitalize() + '- ' + get_book_title(self.bookid) + '  - ' + str(self.bookrating)


class SaveForLater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookid = models.IntegerField()

    def __str__(self):
        return self.user.username.capitalize() + '- ' + get_book_title(self.bookid)


# for the Reviews Section
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_id = models.AutoField
    post_content = models.CharField(max_length=5000)
    timestamp= models.DateTimeField(default=now)
    # image = models.ImageField(upload_to="images",default="")
    
# class Replie(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
#     reply_id = models.AutoField
#     reply_content = models.CharField(max_length=5000) 
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
#     timestamp= models.DateTimeField(default=now)
#     image = models.ImageField(upload_to="images",default="")
