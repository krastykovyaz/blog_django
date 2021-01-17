from django.db import models
from django.contrib.auth.models import User
from PIL import Image # from pillow

class Profile(models.Model): # https://youtu.be/CQ90L5jfldw (info about classes)
    user = models.OneToOneField(User, on_delete=models.CASCADE) # if user delete also delete profile means cascade
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # for resize pics
    def save(self):
        # inherit from the parent class
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:                
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)