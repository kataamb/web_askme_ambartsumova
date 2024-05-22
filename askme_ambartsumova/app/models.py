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
    avatar = models.ImageField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)



class Answer(models.Model):
    text_body = models.CharField(max_length=1000)
    likes_count = models.IntegerField()



class AnswerLike(models.Model):
    value = models.IntegerField()
    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.PROTECT)

    class Meta:
        unique_together = ['user', 'answer']

class Tag(models.Model):
    name = models.CharField(max_length=15)

class Question(models.Model):
    title = models.CharField(max_length=255)
    text_body = models.CharField(max_length=1000)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag, blank=True)

class QuestionLike(models.Model):
    value = models.IntegerField()
    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    likes_count = models.IntegerField()

    class Meta:
        unique_together = ['user', 'question']





