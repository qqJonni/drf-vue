import requests
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import json


class Test(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    def clean(self):
        # Проверка на числа при создании экземпляра класса
        if not isinstance(self.x, (int, float)) or not isinstance(self.y, (int, float)):
            raise ValidationError("x and y must be numbers")

    @staticmethod
    def get_questions_from_api():
        # Метод для получения вопросов с https://jservice.io/
        response = requests.get('https://jservice.io/api/random?count=10')
        questions = response.json()
        return questions

    def save_questions_to_db(self):
        # Метод для записи вопросов в базу данных с проверкой на уникальность и разложением по категориям
        questions = self.get_questions_from_api()
        for question in questions:
            category = question.get('category', '')
            if not Test.objects.filter(x=question['id'], y=category).exists():
                Test.objects.create(x=question['id'], y=category)

    @staticmethod
    def get_record_count_in_category(category):
        # Метод для получения количества записей в указанной категории
        return Test.objects.filter(y=category).count()

    @staticmethod
    def get_and_save_records_to_json(y):
        # Метод для получения y записей из базы данных и сохранения в JSON с текущей датой
        records = Test.objects.all()[:y]
        data = [{'x': record.x, 'y': record.y} for record in records]
        filename = f"records_{timezone.now().strftime('%Y-%m-%d')}.json"
        with open(filename, 'w') as json_file:
            json_file.write(json.dumps(data))


# Пример использования
# test_instance = Test(x=1, y=2)
# test_instance.clean()  # Вызов метода clean для проверки аргументов
# test_instance.save_questions_to_db()  # Получение вопросов и сохранение в базу данных
# record_count = test_instance.get_record_count_in_category('CategoryName')  # Получение количества записей в категории
# test_instance.get_and_save_records_to_json(5)  # Получение и сохранение записей в JSON



class Image(models.Model):
    description = models.TextField()
    image_data = models.TextField()

