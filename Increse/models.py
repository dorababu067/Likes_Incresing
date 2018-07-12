from django.db import models

# Create your models here.
class Posts(models.Model):
    title       = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title


class Like(models.Model):
    posts = models.ForeignKey(Posts,on_delete = models.CASCADE)

#accessig the set of model attributes
# when ever we call the set attributes we call the model with  small letters
# Eg:
# ------
# for Like calling is (like_set.all().count()

# p = Posts.objects.filter(id=1).get()
# p.like_set.all().count()