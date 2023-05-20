from django.db import models

class WebsiteSettingsManager(models.Manager):
    def get_queryset(self):
        # Only retrieve the first instance or create one if it doesn't exist
        if super().get_queryset().count() == 0:
            self.model.objects.create()
        return super().get_queryset().first()

class WebsiteSettings(models.Model):
    logo = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    # Other fields for social media links, text, etc.

    objects = WebsiteSettingsManager()

    def clean(self):
        # Ensure only a single instance of WebsiteSettings is allowed
        if WebsiteSettings.objects.exclude(id=self.id).exists():
            raise ValidationError("Only one instance of WebsiteSettings is allowed")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    # Additional fields for price, availability, etc.

