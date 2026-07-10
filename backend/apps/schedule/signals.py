from django.db.models.signals import post_delete, post_save

from .cache import invalidate_lessons_cache
from .models import (
    Building,
    Group,
    Lesson,
    LessonType,
    Room,
    Subject,
    Teacher,
    TimeSlot,
)

INVALIDATION_MODELS = (
    Building,
    Room,
    Group,
    Teacher,
    Subject,
    TimeSlot,
    LessonType,
    Lesson,
)


def _invalidate_lessons_cache(sender, **kwargs):
    invalidate_lessons_cache()


def connect_cache_invalidation_signals():
    for model in INVALIDATION_MODELS:
        label = model._meta.label_lower.replace(".", "_")
        post_save.connect(
            _invalidate_lessons_cache,
            sender=model,
            dispatch_uid=f"invalidate_lessons_cache_on_save_{label}",
        )
        post_delete.connect(
            _invalidate_lessons_cache,
            sender=model,
            dispatch_uid=f"invalidate_lessons_cache_on_delete_{label}",
        )
