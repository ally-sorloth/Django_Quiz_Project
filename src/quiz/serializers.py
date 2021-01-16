from django.db.models import fields
from rest_framework import serializers
from .models import Answer, Category, Question, Quiz


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "quiz_count"
        )


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            "title",
            "question_count",
        )
        
class AnswerSerializer(serializers.ModelSerializer):  
    class Meta:
        moedel = Answer
        fields = (
            "answer_text",
            "is_right",
        )
class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    difficulty = serializers.SerialiserMethodField()
    
    class Meta:
        moedel = Question
        fields = (
            "title",
            "answer",
            "difficulty"
        )
        
    def get_diffi