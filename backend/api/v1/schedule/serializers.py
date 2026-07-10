from rest_framework import serializers

from apps.schedule.models import (
    Building, Room, Group, Teacher, Subject,
    TimeSlot, LessonType, Lesson,
)


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ["id", "name"]


class RoomSerializer(serializers.ModelSerializer):
    building = BuildingSerializer(read_only=True)
    building_id = serializers.PrimaryKeyRelatedField(
        queryset=Building.objects.all(), source="building", write_only=True
    )

    class Meta:
        model = Room
        fields = ["id", "number", "building", "building_id", "capacity"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name", "course"]


class TeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = [
            "id", "last_name", "first_name", "middle_name",
            "academic_title", "full_name",
        ]

    def get_full_name(self, obj):
        
        return str(obj)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "name"]


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ["id", "number", "start_time", "end_time"]


class LessonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonType
        fields = ["id", "name", "color"]


class LessonSerializer(serializers.ModelSerializer):
    #Для ЧТЕНИЯ отдаём вложенные объекты — фронту не придётся делать доп. запросы, чтобы узнать имя группы или ФИО препода.
    group = GroupSerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)
    room = RoomSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)
    lesson_type = LessonTypeSerializer(read_only=True)
    time_slot = TimeSlotSerializer(read_only=True)

    group_id = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), source="group", write_only=True
    )
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source="teacher", write_only=True
    )
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), source="room", write_only=True
    )
    subject_id = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(), source="subject", write_only=True
    )
    lesson_type_id = serializers.PrimaryKeyRelatedField(
        queryset=LessonType.objects.all(), source="lesson_type", write_only=True
    )
    time_slot_id = serializers.PrimaryKeyRelatedField(
        queryset=TimeSlot.objects.all(), source="time_slot", write_only=True
    )

    day_of_week_display = serializers.CharField(
        source="get_day_of_week_display", read_only=True
    )
    week_parity_display = serializers.CharField(
        source="get_week_parity_display", read_only=True
    )

    class Meta:
        model = Lesson
        fields = [
            "id",
            "group", "group_id",
            "subgroup",
            "teacher", "teacher_id",
            "room", "room_id",
            "subject", "subject_id",
            "lesson_type", "lesson_type_id",
            "time_slot", "time_slot_id",
            "day_of_week", "day_of_week_display",
            "week_parity", "week_parity_display",
        ]