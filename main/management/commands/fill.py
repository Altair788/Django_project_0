from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):
    """
    Представляет класс кастомная команда
    """
    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'Petrov', 'first_name': 'Ivan'},
            {'last_name': 'Ivanov', 'first_name': 'Petr'},
            {'last_name': 'Sidorov', 'first_name': 'Oleg'},
            {'last_name': 'Somonov', 'first_name': 'Mihail'},
            {'last_name': 'Mirolubov', 'first_name': 'Igor'},
            {'last_name': 'Nurmagomedov', 'first_name': 'Habib'},
            {'last_name': 'Mahachev', 'first_name': 'Ismail'},
            {'last_name': 'Abdullaev', 'first_name': 'Timur'},
            {'last_name': 'Pozdishev', 'first_name': 'Eric'},
        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        #  соединение с БД идет один раз через пакетное добаление bulk_create
        students_for_create = []
        for student_item in student_list:
            students_for_create.append(
                Student(**student_item)
            )

        print(students_for_create)

        Student.objects.bulk_create(students_for_create)