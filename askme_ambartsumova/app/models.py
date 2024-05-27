from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class UserManager(models.Manager):
    pass
    '''
    def get_by_username(self, username):
        return self.filter(user__username=username)
    '''

class ProfileManager(models.Manager):
    def get_by_username(self, username):
        return self.filter(user__username=username)


class Profile(models.Model):
    avatar = models.ImageField(null=True, blank=True)
    login = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ProfileManager()

    def __str__(self):
        return self.login





class TagManager(models.Manager):
    pass

class Tag(models.Model):
    name = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = TagManager()
    def __str__(self):
        return self.name



class QuestionManager(models.Manager):
    def hot_questions(self):
        return self.order_by('-likes_count')
    def new_questions(self):
        return self.order_by('-created_at')
    def get_by_tag(self, tag_slug):
        return self.filter(tags__name=tag_slug)

    def get_by_pk(self, question_id):
        return self.get(id=question_id)


class Question(models.Model):
    title = models.CharField(max_length=255)
    text_body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    likes_count = models.IntegerField()



    tags = models.ManyToManyField(Tag, blank=True)

    objects = QuestionManager()





    def __str__(self):
        return self.title


class QuestionLikeManager(models.Manager):
    pass

class QuestionLike(models.Model):
    value = models.IntegerField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    objects = QuestionLikeManager()

    class Meta:
        unique_together = ['user', 'question']

    def __str__(self):
        return self.question.title + " "+ self.user.login





class AnswerManager(models.Manager):
    def get_by_question(self, question_id):
        return self.filter(question__id=question_id).order_by('-created_at')

    #return self.filter(tags__name=tag_slug)

class Answer(models.Model):
    text_body = models.CharField(max_length=1000)
    likes_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


    objects = AnswerManager()

    def __str__(self):
        return self.text_body





class AnswerLikeManager(models.Manager):
    pass


class AnswerLike(models.Model):
    value = models.IntegerField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = AnswerLikeManager()

    class Meta:
        unique_together = ['user', 'answer']

    def __str__(self):
        return "answer_like" + " "+ self.user.login


