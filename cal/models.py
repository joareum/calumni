from django.db import models


class Cal(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True)
    apply = models.TextField(null=True)
    score = models.TextField(null=True)
    write = models.TextField(null=True)
    act = models.TextField(null=True)
    schoolact = models.TextField(null=True)
    cer = models.TextField(null=True)
    pub_date = models.DateTimeField("data published")
    image = models.ImageField(upload_to='images/', blank=True)
    category1 = models.CharField(max_length=10,null=True)
    category2 = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]

# 댓글
class Comment(models.Model):
    post = models.ForeignKey(Cal, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField("data published")
    
    def __str__(self):
        return self.body
