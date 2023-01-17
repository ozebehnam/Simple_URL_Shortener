from django.utils import timezone
from django.db import models
from . import utils

random = utils.create_random_code()
# Create your models here.
class Route(models.Model):

    original_url = models.URLField(help_text="Add the original URL that you want to shorten.", name="original_url")
    key = models.TextField(unique=True, help_text="Use generated short link or add any random characters of your choice to shorten it.", default=random, name="key")
    user = models.CharField(default='admin', max_length=100, name="user")
    req_time = models.DateTimeField(auto_now_add=True, name="req_time")
    res_time = models.DateTimeField(auto_now_add=True, name="res_time")
    #req_time_stamp = models.PositiveBigIntegerField(default=timezone.time, name="req_time")
    clicked = models.PositiveBigIntegerField(default=0, name="clicked")
    device = models.CharField(max_length=100, default='Unkown', name="device")
    bench = models.PositiveBigIntegerField(default=0, name="bench")


    def __str__(self):
        return f"{self.key}"