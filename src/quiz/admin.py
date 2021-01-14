from django.contrib import admin

from quiz.models import Answer, Category, Question, Quiz
from .models import Category, Quiz, Question, Answer

admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)

# Register your models here.
