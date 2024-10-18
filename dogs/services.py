from django.core.cache import cache

from config.settings import CACHE_ENABLED
from dogs.models import Dog


def get_dogs_from_cache():
    """
    Получает данные по собакам. Если кеш пуст, получает данные из БД.
    """
    if CACHE_ENABLED:
        key = f"dogs_list"
        dogs_list = cache.get(key)
        if dogs_list is None:
            dogs_list = Dog.objects.all()
            cache.set(key, dogs_list)
    else:
        dogs_list = Dog.objects.all()
    return dogs_list