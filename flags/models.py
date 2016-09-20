from django.db import models
from django.core.files.uploadedfile import SimpleUploadedFile
from random import randint
from PIL import Image
from cStringIO import StringIO
import os.path

class Flag(models.Model):
    name = models.CharField(max_length = 50, blank=True)
    location = models.CharField(max_length = 50, blank=True)
    email = models.EmailField(max_length = 50, blank=True)
    tagline = models.CharField(max_length = 50, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    original = models.ImageField(upload_to = 'flags/%Y/%B/%d', blank=True)
    image = models.ImageField(upload_to = 'flags/%Y/%B/%d', blank=True)
    thumbnail = models.ImageField(upload_to = 'flags/%Y/%B/%d', blank=True)
    state = models.CharField(max_length = 10, default = 'new')
    flagReason = models.CharField(max_length=100, blank=True)
    
    def random_number(self):
        return randint(1, 6)

    def admin_thumb(self):
        if self.thumbnail:
            return u'<img style="max-width:180px;max-length:200px;" src="%s" />' % (self.thumbnail.url)
        else:
            return 'No Image'
    admin_thumb.short_description = "Image"
    admin_thumb.allow_tags = True
    
    def save(self, *args, **kwargs):
        super(Flag, self).save(*args, **kwargs)
        if not self.thumbnail and self.original:
            self.make_thumbnail()
    
    def make_thumbnail(self):
        image = Image.open(self.original)
        
        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')
        
        image.thumbnail((800, 800), Image.ANTIALIAS)
        thumb = image.copy()
        thumb.thumbnail((300, 300), Image.ANTIALIAS)
        
        imageHandle = StringIO()
        thumbHandle = StringIO()
        
        image.save(imageHandle, 'png')
        thumb.save(thumbHandle, 'png')
        imageHandle.seek(0)
        thumbHandle.seek(0)
        img = SimpleUploadedFile(str(self.id) + '.png', imageHandle.read(), content_type='image/png')
        thu = SimpleUploadedFile(str(self.id) + '.png', thumbHandle.read(), content_type='image/png')
        
        self.image.save(str(self.id) + '.png', img, False)
        self.thumbnail.save(str(self.id) + '.png.thumb', thu, False)
        self.save()
    
    def as_json(self):
        response = {}
        if self.state == 'flagged':
            return { 
                'state': self.state,
                'id': self.id,
                'random': self.random_number(),
            }
        else:
            if self.image:
                image = self.image.url
                thumbnail = self.thumbnail.url
            else:
                image = ''
                thumbnail = ''
            return {
                'image': image,
                'thumbnail': thumbnail,
                'name': self.name,
                'location': self.location,
                'tagline': self.tagline,
                'state': self.state,
                'id': self.id,
                'state': self.state,
                'random': self.random_number(),
            }