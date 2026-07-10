from django.db import models

# Корпус 
class Building(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'
    def __str__(self):
        return self.name

# Аудитория
class Room(models.Model):
    number = models.CharField(max_length=20)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='rooms')
    capacity = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Аудитория"
        verbose_name_plural = "Аудитории"
        unique_together = ("number", "building")
 
    def __str__(self):
        return f"{self.number} ({self.building.name})"

# Студенческая группа
class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)
    course = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name

# Преподаватель
class Teacher(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    academic_title = models.CharField(max_length=100, blank=True, help_text="доц., проф., асс.")
    
    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        title = f"{self.academic_title}." if self.academic_title else ""
        initials = f"{self.first_name[:1]}.{self.middle_name[:1]}." if self.middle_name else f"{self.first_name[:1]}."
        return f"{title}{self.last_name} {initials}"

# Учебная дисциплина
class Subject(models.Model):
    name = models.CharField(max_length=200, unique=True)
 
    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"
 
    def __str__(self):
        return self.name

# Пара
class TimeSlot(models.Model):
    number = models.PositiveSmallIntegerField(unique=True)  
    start_time = models.TimeField()
    end_time = models.TimeField()
 
    class Meta:
        verbose_name = "Пара"
        verbose_name_plural = "Пары"
        ordering = ["number"]
 
    def __str__(self):
        return f"{self.number} пара ({self.start_time.strftime('%H:%M')}-{self.end_time.strftime('%H:%M')})"

# Тип занятия
class LessonType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7, default="#3498db", help_text="HEX-код цвета (например, #ff0000)")
 
    class Meta:
        verbose_name = "Тип занятия"
        verbose_name_plural = "Типы занятий"
 
    def __str__(self):
        return self.name

class Lesson(models.Model):
    class DayOfWeek(models.IntegerChoices):
        MONDAY = 1, "Понедельник"
        TUESDAY = 2, "Вторник"
        WEDNESDAY = 3, "Среда"
        THURSDAY = 4, "Четверг"
        FRIDAY = 5, "Пятница"
        SATURDAY = 6, "Суббота"
 
    class WeekParity(models.TextChoices):
        ODD = "odd", "Нечётная неделя"
        EVEN = "even", "Чётная неделя"
        EVERY = "every", "Каждую неделю"
 
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="lessons")
    subgroup = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Подгруппа")
    
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="lessons")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="lessons")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="lessons")
    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE, related_name="lessons")
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, related_name="lessons")
 
    day_of_week = models.PositiveSmallIntegerField(choices=DayOfWeek.choices)
    week_parity = models.CharField(max_length=5, choices=WeekParity.choices, default=WeekParity.EVERY)
 
    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"
        indexes = [
            models.Index(fields=["group", "day_of_week", "week_parity"]),
            models.Index(fields=["teacher", "day_of_week"]),
            models.Index(fields=["room", "day_of_week"]),
        ]
        ordering = ["day_of_week", "time_slot__number"]
        
    def __str__(self):
        sub = f", п/г {self.subgroup}" if self.subgroup else ""
        return f"{self.group}{sub} — {self.subject} ({self.get_day_of_week_display()}, {self.time_slot})"