from django.db import models
import random
import string


#Generates random code to create a new Room
def generate_unique_code():
    lenght = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=lenght))
        if Room.objects.filter(code.code).count() == 0:
            break

    return code






# Create your models here.
#Room model returns a music party room 
class Room(models.Model):
    code = models.CharField(max_length=8, unique=True, default="")
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)






    