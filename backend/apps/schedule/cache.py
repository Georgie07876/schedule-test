from django.core.cache import cache

LESSONS_CACHE_VERSION_KEY = "lessons:version"
LESSONS_LIST_CACHE_TIMEOUT = 60 * 15


def get_lessons_cache_version() -> int:
    version = cache.get(LESSONS_CACHE_VERSION_KEY)
    if version is None:
        version = 1
        cache.set(LESSONS_CACHE_VERSION_KEY, version, timeout=None)
    return version


def build_lessons_list_cache_key(request_path: str) -> str:
    return f"lessons_list:v{get_lessons_cache_version()}:{request_path}"


def invalidate_lessons_cache() -> None:
    try:
        cache.incr(LESSONS_CACHE_VERSION_KEY)
    except ValueError:
        cache.set(LESSONS_CACHE_VERSION_KEY, 1, timeout=None)
