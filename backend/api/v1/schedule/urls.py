from rest_framework.routers import DefaultRouter
 
from .views import (
    BuildingViewSet, RoomViewSet, GroupViewSet, TeacherViewSet,
    SubjectViewSet, TimeSlotViewSet, LessonTypeViewSet, LessonViewSet,
)

router = DefaultRouter()
router.register("buildings", BuildingViewSet, basename="building")
router.register("rooms", RoomViewSet, basename="room")
router.register("groups", GroupViewSet, basename="group")
router.register("teachers", TeacherViewSet, basename="teacher")
router.register("subjects", SubjectViewSet, basename="subject")
router.register("timeslots", TimeSlotViewSet, basename="timeslot")
router.register("lesson-types", LessonTypeViewSet, basename="lessontype")
router.register("lessons", LessonViewSet, basename="lesson")
 
urlpatterns = router.urls
 