'''
Model for images and price for the gallery so that the user can buy them
'''
from django.db import models
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField


class ImageEntry(models.Model):
    """
    Gallery entry model.
    @title is the title of the image,.
    @slug is autogenerated from the title.
    @date_posted is taken from when the product/image
     is posted in the database.
    @image is a image container using the externall CDN: Cloudinary images.
    @price is the price that is going to be referenced from the shopping cart.
    @hidden is to prevent image being shown without completly
     removing the image.
    """
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    date_posted = models.DateTimeField(auto_now=True, editable=False)
    image = CloudinaryField('image')
    water_marked_image = CloudinaryField('image')
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    hidden = models.BooleanField(default=False)

    class Meta:
        '''
        Meta class to order and change verbose naming inside the admin panel
        '''
        ordering = ["-date_posted"]
        verbose_name = 'Product'
        verbose_name_plural = 'Product entries'

    def __str__(self):
        string_title = str(self.title)
        return string_title

    def save(self):
        self.slug = slugify(self.title)
        super(ImageEntry, self).save()
