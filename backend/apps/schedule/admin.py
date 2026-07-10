from django.contrib import admin
from .models import Building, Room, Group, Teacher, Subject, TimeSlot, LessonType, Lesson

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'building', 'capacity')
    list_filter = ('building',)
    search_fields = ('number',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')
    list_filter = ('course',)
    search_fields = ('name',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'academic_title')
    search_fields = ('last_name', 'first_name')
    list_filter = ('academic_title',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('number', 'start_time', 'end_time')
    ordering = ('number',)

@admin.register(LessonType)
class LessonTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'group', 
        'subgroup', 
        'subject', 
        'lesson_type', 
        'teacher', 
        'room', 
        'day_of_week', 
        'time_slot', 
        'week_parity'
    )
    
    list_filter = (
        'day_of_week', 
        'week_parity', 
        'group', 
        'teacher', 
        'lesson_type'
    )
    
    search_fields = (
        'group__name', 
        'subject__name', 
        'teacher__last_name'
    )
    
    autocomplete_fields = ('group', 'teacher', 'room', 'subject')