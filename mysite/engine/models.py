from django.db import models
import numpy as np
from django.contrib.auth.models import User
from collections import Counter  # calculate individual movie ratingstar time


class MyUser(models.Model):
    #id = models.AutoField(primary_key=True)
    #id = models.IntegerField(primary_key=True)
    username = models.CharField('姓名', max_length = 20)
    def __str__(self):
        return self.username


class Movie(models.Model):
    #id = models.AutoField(primary_key=True)
    #id = models.IntegerField(primary_key=True)
    name = models.CharField('電影', max_length = 100)
    detail = models.CharField(max_length = 6000, blank=True)
    photo_url = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name
    def average_rating(self):
        all_rating = self.rating_set.all()
        '''
        total=0
        for r in all_rating:
            total += r.rating
        avg = total/all_rating.count()
        '''
        all_ratings = list( map(lambda x: x.get_rate(), self.rating_set.all()) )

        ratingCounter = Counter(all_ratings) #Counter({4.0: 4, 2.0: 3, 3.0: 2, 5.0: 2})
        avg = np.mean(all_ratings)        
        return avg
    def ratingstar_counter(self):
        all_rating = self.rating_set.all()
        all_ratings = list( map(lambda x: x.get_rate(), self.rating_set.all()) )

        ratingCounter = Counter(all_ratings) #Counter({4.0: 4, 2.0: 3, 3.0: 2, 5.0: 2})
        return ratingCounter


class Rating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    user = models.ForeignKey(User, verbose_name='評分者', null=True)
    
    movie = models.ForeignKey(Movie, verbose_name='電影')
    rating = models.FloatField('給個評分吧!', choices=RATING_CHOICES)
    pub_date = models.DateTimeField('評分時間')
    comment = models.CharField('給個留言',max_length=200, blank =True)
    def get_rate(self):
        return self.rating
    def __str__(self):
        return self.user.username+","+self.movie.name+":"+str(self.rating)
