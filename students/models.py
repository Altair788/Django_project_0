# from django.db import models
#
#
# # Create your models here.
# class Group(models.Model):
#     """
#     Представляет класс Группа
#     """
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class Student(models.Model):
#     """
#     Представляет класс Студент
#     """
#     first_name = models.CharField(max_length=150, verbose_name='имя')
#     last_name = models.CharField(max_length=150, verbose_name='фамилия')
#     group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
#
#     def __str__(self):
#         """
#         Строковое представление объекта
#         """
#         return f'{self.first_name} {self.last_name}'
#
#     class Meta:
#         verbose_name = 'студент'
#         verbose_name_plural = 'студенты'
#
#
# class Book(models.Model):
#     """
#     Представляет класс Книга
#     """
#     OLD_BOOK = 'old'
#     NEW_BOOK = 'new'
#
#     BOOK_TYPES = (
#         (OLD_BOOK, 'Старые книги'),
#         (NEW_BOOK, 'Новые книги'),
#     )
#
#     book_type = models.CharField(
#         max_length=3,
#         default=OLD_BOOK,
#         choices=BOOK_TYPES
#     )
#
#
# #
# # group = Group.objects.get(name='Group Name')
# # students = group.students.all()
#
# class Book(models.Model):
#     """
#     Представляет класс Книга
#     """
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=50)
#     publication_year = models.IntegerField()
