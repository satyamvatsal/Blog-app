from django.db import models

# Create your models here.
class post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=300)
    pub_date = models.DateField("Published Date")
    content = models.TextField(default="Content")
    def __str__(self):
        return self.title

class comment(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    comment_text = models.TextField(default="This is a comment")
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.username}: {self.comment_text[:20]}"