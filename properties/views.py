# from django.shortcuts import render

# from django.http import JsonResponse
# from django.views.decorators.cache import cache_page
# from django.utils.decorators import method_decorator
# from django.views import View
# from .models import Property


# @method_decorator(cache_page(60 * 15), name='dispatch')  # cache for 15 minutes
# class PropertyListView(View):
#     def get(self, request):
#         properties = Property.objects.all().values("id", "title", "description", "price", "location", "created_at")
#         return JsonResponse(list(properties), safe=False)

from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property
from .utils import get_all_properties

@cache_page(60 * 15)  # cache for 15 minutes
def property_list(request):
    properties = Property.objects.all().values(
        "id", "title", "description", "price", "location", "created_at"
    )
    return JsonResponse({
        "data": list(properties)
    })

def property_list(request):
    properties = get_all_properties()
    return JsonResponse({
        "data": properties
    })
