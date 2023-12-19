from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField(max_length = 600)
    user = models.CharField(max_length = 200)
    date_time = models.DateTimeField(auto_now_add = True)
    
    def __str__(self) -> str:
        return str(self.user) + "ning vazifalari."

