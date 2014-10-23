from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Level(models.Model):
    level_number = models.IntegerField(unique=True)
    image = models.ImageField(upload_to='media/levels')
    answer = models.CharField(max_length=60)

    def __str__(self):
        return 'Level: %d' % self.level_number


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    current_level = models.IntegerField(default=1)

    def __str__(self):
        return '%s at Level-%d' % (self.user.username, self.current_level)


#Automatically create a user profile for every user
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)