from django.db import models

# Create your models here.
class Topic(models.Model):
    """Creat topic class."""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        """Return string stored in text argument."""
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    Date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def _str_(self):
        return self.text [ :50] + "..."