from django.db import models
from django.contrib.auth.models import User

# Create your models here.


'''
Table Question {
  id int [PK]
  title varchar
  text_body varchar
  answer_id int
  like_id int
}


Table Answer {
  id int [PK]
  text_body varchar
  like_id int
}

Table Tag {
  id int [PK]
  name varchar
}



Table Question_Tag {
  tag_id int
  question_id int
 
  
}



Table Profile {
  id int [PK] 
  avatar image
  
}

Table User {
  id int [PK]
  login varchar
  email varchar
  password varchar
  profile_id int [ref: - Profile.id]

  question_id int
  answer_id int
}



Table QuestionLike {
  id int [PK]
  value int
  user_id int [ref: - User.id]
}

Table AnswerLike {
  id int [PK]
  value int
  user_id int [ref: - User.id]
}


'''

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    avatar = models.ImageField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class AnswerLike(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.IntegerField()
    user = models.OneToOneField(Profile, on_delete=models.PROTECT)

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    text_body = models.CharField(max_length=1000)
    like = models.ForeignKey(AnswerLike, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['id', 'like']]



class QuestionLike(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.IntegerField()
    user = models.OneToOneField(Profile, on_delete=models.PROTECT)

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    text_body = models.CharField(max_length=1000)
    answer = models.ForeignKey(Answer, on_delete = models.CASCADE)
    like = models.ForeignKey(QuestionLike, on_delete = models.PROTECT)

    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        unique_together = [['id', 'like']]