# from django.core.cache import cache
# from django_redis import get_redis_connection
# import logging
# from .models import Property

# def get_all_properties():
#     """
#     Retrieves all properties from Redis cache if available,
#     otherwise fetches from DB and caches for 1 hour.
#     """
#     properties = cache.get('all_properties')

#     if properties is None:
#         properties = list(Property.objects.all().values(
#             "id", "title", "description", "price", "location", "created_at"
#         ))
#         cache.set('all_properties', properties, 3600)  # cache for 1 hour

#     return properties



# logger = logging.getLogger(__name__)

# def get_all_properties():
#     """
#     Retrieve all properties, using Redis cache for 1 hour.
#     """
#     properties = cache.get('all_properties')
#     if properties is None:
#         properties = Property.objects.all()
#         cache.set('all_properties', properties, 3600)
#     return properties


# def get_redis_cache_metrics():
#     """
#     Retrieve Redis cache metrics: keyspace hits, misses, and hit ratio.
#     """
#     try:
#         # Get a Redis connection (default Django cache alias)
#         redis_conn = get_redis_connection("default")
#         info = redis_conn.info("stats")

#         hits = info.get("keyspace_hits", 0)
#         misses = info.get("keyspace_misses", 0)

#         total = hits + misses
#         hit_ratio = (hits / total) if total > 0 else 0.0

#         metrics = {
#             "hits": hits,
#             "misses": misses,
#             "hit_ratio": round(hit_ratio, 4),  # e.g., 0.875
#         }

#         logger.info(f"Redis Cache Metrics: {metrics}")
#         return metrics

#     except Exception as e:
#         logger.error(f"Error retrieving Redis cache metrics: {e}")
#         return {"hits": 0, "misses": 0, "hit_ratio": 0.0}

import logging
from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property

logger = logging.getLogger(__name__)

def get_all_properties():
    """
    Retrieve all properties, using Redis cache for 1 hour.
    """
    properties = cache.get('all_properties')
    if properties is None:
        properties = Property.objects.all()
        cache.set('all_properties', properties, 3600)
    return properties


def get_redis_cache_metrics():
    """
    Retrieve Redis cache metrics: keyspace hits, misses, and hit ratio.
    """
    try:
        redis_conn = get_redis_connection("default")
        info = redis_conn.info("stats")

        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)

        total_requests = hits + misses
        if total_requests > 0:
            hit_ratio = hits / total_requests
        else:
            hit_ratio = 0.0

        metrics = {
            "hits": hits,
            "misses": misses,
            "hit_ratio": round(hit_ratio, 4),
        }

        logger.info(f"Redis Cache Metrics: {metrics}")
        return metrics

    except Exception as e:
        logger.error(f"Error retrieving Redis cache metrics: {e}")
        return {"hits": 0, "misses": 0, "hit_ratio": 0.0}
