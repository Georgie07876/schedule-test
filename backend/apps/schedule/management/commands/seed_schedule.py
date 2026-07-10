import random
from datetime import time
from django.core.management.base import BaseCommand
from django.db import transaction
from apps.schedule.models import (
    Building, Room, Group, Teacher, Subject, 
    TimeSlot, LessonType, Lesson
)

class Command(BaseCommand):
    help = 'Наполняет базу данных тестовым расписанием для РГЭУ (РИНХ)'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Очистка старых занятий...")
        Lesson.objects.all().delete()

        # --- 1. КОРПУСА И АУДИТОРИИ ---
        b_main, _ = Building.objects.get_or_create(name="Главный корпус")
        b_tur, _ = Building.objects.get_or_create(name="Корпус на Тургеневской")

        rooms_data = [
            (b_main, "212", 60), 
            (b_main, "214", 30),
            (b_main, "415", 100),
            (b_tur, "512", 40),
            (b_tur, "513", 40),
        ]
        rooms = {}
        for building, number, capacity in rooms_data:
            room, _ = Room.objects.get_or_create(
                number=number, building=building, defaults={"capacity": capacity}
            )
            rooms[number] = room

        # --- 2. ГРУППЫ ---
        groups_data = [
            ("ИСТ-311", 1), # Из ТЗ
            ("ПРИ-331", 3),
            ("ПМИ-321", 2),
            ("БИН-322", 2),
            ("ПИ-341", 4),
        ]
        groups = {}
        for name, course in groups_data:
            group, _ = Group.objects.get_or_create(name=name, defaults={"course": course})
            groups[name] = group

        # --- 3. ПРЕПОДАВАТЕЛИ ---
        teachers_data = [
            ("Долженко", "Алексей", "Иванович", "доц"), # Из ТЗ
            ("Авдеева", "Анна", "Александровна", "асс"),
            ("Лозина", "Елена", "Николаевна", "доц"),
            ("Полуднев", "Виктор", "Дмитриевич", "проф"),
        ]
        teachers = {}
        for last, first, middle, title in teachers_data:
            teacher, _ = Teacher.objects.get_or_create(
                last_name=last, first_name=first, middle_name=middle, defaults={"academic_title": title}
            )
            teachers[last] = teacher

        # --- 4. ПРЕДМЕТЫ ---
        subjects_data = [
            "Программирование на Python", "Базы данных (PostgreSQL)", 
            "Проектный практикум", "Управление корпоративными ИС", 
            "Высшая математика", "Web-технологии (Vue.js)"
        ]
        subjects = {}
        for name in subjects_data:
            sub, _ = Subject.objects.get_or_create(name=name)
            subjects[name] = sub

        # --- 5. ТИПЫ ЗАНЯТИЙ ---
        lesson_types_data = [
            ("Лекция", "#3498db"),
            ("Практика", "#2ecc71"),
            ("Лабораторная", "#9b59b6"),
            ("Экзамен", "#e74c3c")
        ]
        lesson_types = {}
        for name, color in lesson_types_data:
            lt, _ = LessonType.objects.get_or_create(name=name, defaults={"color": color})
            lesson_types[name] = lt

        # --- 6. ПАРЫ (ВРЕМЯ) ---
        time_slots_data = [
            (1, time(8, 30), time(10, 0)),
            (2, time(10, 10), time(11, 40)),
            (3, time(11, 50), time(13, 20)),
            (4, time(13, 50), time(15, 20)),
        ]
        time_slots = {}
        for num, start, end in time_slots_data:
            ts, _ = TimeSlot.objects.get_or_create(
                number=num, defaults={"start_time": start, "end_time": end}
            )
            time_slots[num] = ts

        # --- 7. СОЗДАНИЕ ЗАНЯТИЙ ---
        lessons_to_create = []

        lessons_to_create.append(Lesson(
            group=groups["ИСТ-311"], teacher=teachers["Долженко"], room=rooms["214"],
            subject=subjects["Высшая математика"], lesson_type=lesson_types["Лекция"],
            time_slot=time_slots[1], day_of_week=Lesson.DayOfWeek.MONDAY, week_parity=Lesson.WeekParity.ODD
        ))
        
        lessons_to_create.append(Lesson(
            group=groups["ПИ-341"], teacher=teachers["Лозина"], room=rooms["212"],
            subject=subjects["Управление корпоративными ИС"], lesson_type=lesson_types["Практика"],
            time_slot=time_slots[2], day_of_week=Lesson.DayOfWeek.WEDNESDAY, week_parity=Lesson.WeekParity.EVERY
        ))

        lessons_to_create.append(Lesson(
            group=groups["ПМИ-321"], teacher=teachers["Долженко"], room=rooms["415"],
            subject=subjects["Программирование на Python"], lesson_type=lesson_types["Лекция"],
            time_slot=time_slots[3], day_of_week=Lesson.DayOfWeek.THURSDAY, week_parity=Lesson.WeekParity.EVEN
        ))

        group_list = list(groups.values())
        teacher_list = list(teachers.values())
        room_list = list(rooms.values())
        subject_list = list(subjects.values())
        type_list = [lesson_types["Лекция"], lesson_types["Практика"], lesson_types["Лабораторная"]]
        parity_choices = [Lesson.WeekParity.EVERY, Lesson.WeekParity.ODD, Lesson.WeekParity.EVEN]
        
        for _ in range(35):
            group = random.choice(group_list)
            subgroup = random.choice([None, None, None, None, 1, 2]) 
            
            lessons_to_create.append(Lesson(
                group=group,
                subgroup=subgroup,
                teacher=random.choice(teacher_list),
                room=random.choice(room_list),
                subject=random.choice(subject_list),
                lesson_type=random.choice(type_list),
                time_slot=time_slots[random.randint(1, 4)],
                day_of_week=random.randint(1, 6),
                week_parity=random.choice(parity_choices)
            ))

        Lesson.objects.bulk_create(lessons_to_create)

        self.stdout.write(self.style.SUCCESS(f"Успешно создано {len(lessons_to_create)} занятий!"))