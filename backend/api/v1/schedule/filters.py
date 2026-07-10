import django_filters
from apps.schedule.models import Lesson

class LessonFilter(django_filters.FilterSet):
    group = django_filters.NumberFilter(field_name='group_id')
    teacher = django_filters.NumberFilter(field_name='teacher_id')
    room = django_filters.NumberFilter(field_name='room_id')
    building = django_filters.NumberFilter(field_name='room__building_id')
    day_of_week = django_filters.NumberFilter(field_name='day_of_week')
    week_parity = django_filters.CharFilter(field_name='week_parity')

    class Meta: 
        model = Lesson
        fields = ["group", "teacher", "room", "building", "day_of_week", "week_parity"]
