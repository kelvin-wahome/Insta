from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name

class Category(models.Model):
    name = models.CharField(max_length = 60)
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.category_name

class Images(models.Model):

    title = models.CharField(max_length = 60)
    description = models.CharField(max_length = 60)
    image = models.ImageField(upload_to = 'articles/')
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_image(cls,category):
        result_search = cls.objects.filter(category__name__icontains=search_term)
        return images

    @classmethod
    def filter_by_location(cls,id):
        images = cls.objects.filter(location_id=id)
        return images

     @classmethod
    def filter_by_category(cls, id):
        images = cls.objects.filter(category_id=id)
        return images

    @classmethod
    def get_all_images(cls):
        images = cls.objects.order_by()
        return images
