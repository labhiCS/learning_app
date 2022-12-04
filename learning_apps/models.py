from django.db import models

# Create your models here.
class Topic(models.Model):
    """Creat topic class."""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        """Return string stored in text argument."""
        return self.text