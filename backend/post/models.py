from django.db import models
from django.contrib.auth import get_user_model
from accountdata.models import appuser

User = get_user_model()

class Post(models.Model):
    NUMBER_CHOICES = [ # 인원수 1~5까지
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    post_id = models.BigAutoField(primary_key=True, null=False, blank=False) # 게시글 고유 번호
    title = models.CharField(max_length=200) # title 컬럼
    content = models.TextField()           # content 컬럼
    personnel = models.IntegerField(choices=NUMBER_CHOICES, default=1) # 인원수
    match = models.IntegerField(default=0,null=True)
    postuser=models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='posts_sent',blank=True) #작성자
    reciveuser=models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='posts_received',blank=True) #참여자
    reciverphone = models.CharField(max_length=30, null=True,blank=True)
    postphone = models.CharField(max_length=30,null=True,blank=True)
    recivertext = models.TextField(null=True,blank=True)
    lat = models.FloatField(default=0,null=True,blank=True)#위도
    lan = models.FloatField(default=0,null=True,blank=True)#경도
    def __str__(self):
        return self.title