from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response

from apps.schedule.cache import (
    LESSONS_LIST_CACHE_TIMEOUT,
    build_lessons_list_cache_key,
)
from apps.schedule.models import (
    Building,
    Group,
    Lesson,
    LessonType,
    Room,
    Subject,
    Teacher,
    TimeSlot,
)
from .filters import LessonFilter
from .serializers import (
    BuildingSerializer,
    GroupSerializer,
    LessonSerializer,
    LessonTypeSerializer,
    RoomSerializer,
    SubjectSerializer,
    TeacherSerializer,
    TimeSlotSerializer,
)


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.select_related("building").all()
    serializer_class = RoomSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer


class LessonTypeViewSet(viewsets.ModelViewSet):
    queryset = LessonType.objects.all()
    serializer_class = LessonTypeSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.select_related(
        "group",
        "teacher",
        "room",
        "room__building",
        "subject",
        "lesson_type",
        "time_slot",
    ).all()
    serializer_class = LessonSerializer
    filterset_class = LessonFilter

    def list(self, request, *args, **kwargs):
        cache_key = build_lessons_list_cache_key(request.get_full_path())
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        if response.status_code == 200:
            cache.set(cache_key, response.data, LESSONS_LIST_CACHE_TIMEOUT)
        return response
