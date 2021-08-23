from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe
from accounts.models import User
import random


class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')
    
    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)


class Quiz(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    name = models.TextField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField('Question', max_length=500)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField('Answer', max_length=500)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    interests = models.ManyToManyField(Subject, related_name='interested_students')
    name = models.CharField(max_length=200)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    status = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='student-photos/')
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    email = models.EmailField(blank=True, null=True)
    registration_no = models.IntegerField(unique=True, default=random.randint(000000, 999999))

    def get_unanswered_questions(self, quiz):
        answered_questions = self.quiz_answers \
            .filter(answer__question__quiz=quiz) \
            .values_list('answer__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions

    def __str__(self):
        return self.user.username


class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)


class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')


class Collection(models.Model):
    subject = models.CharField(max_length=300, blank=True)
    owner = models.CharField(max_length=300, blank=True)
    note = models.TextField(blank=True)
    created_by = models.ForeignKey(User,related_name="collections", blank=True, null=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)


class CollectionTitle(models.Model):
    """
    A Class for Collection titles.

    """
    collection = models.ForeignKey(Collection,
                                   related_name="has_titles", on_delete=models.CASCADE)
    name = models.CharField(max_length=500, verbose_name="Title")
    language = models.CharField(max_length=3)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    status = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='teacher-photos/')
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    email = models.EmailField(blank=True, null=True)
    religion_choice = (
        ('Catholic', 'Catholic'),
        ('Angelican', 'Angelican'),
        ('Islam', 'Islam'),
        ('Hinduism', 'Hinduism'),
        ('Buddhism', 'Buddhism'),
        ('Christianity', 'Christianity'),
        ('Others', 'Others')
    )
    religion = models.CharField(choices=religion_choice, max_length=45)
    nationality_choice = (
        ('Uganda', 'Uganda'),
        ('Others', 'Others')
    )
    nationality = models.CharField(choices=nationality_choice, max_length=45)

    def __str__(self):
        return self.user.username






class  Grade(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Classroom(models.Model):
    year = models.DateField()
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE)
    section = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    remarks  = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)



class  Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ClassroomStudent(models.Model):
    classroom = models.ForeignKey(Classroom,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)


class Attendance(models.Model):
    date = models.DateTimeField()
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    remarks = models.TextField()


    def __str__(self):
        return str(self.student)


class  ExamType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class  Exam(models.Model):
    name = models.CharField(max_length=100)
    exam_type = models.ForeignKey(ExamType,on_delete=models.CASCADE)
    start_date = models.DateField()

    def __str__(self):
        return self.name


class  ExamResult(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    marks = models.CharField(max_length=45)

    def __str__(self):
        return self.marks