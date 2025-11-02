from django.views.decorators.cache import cache_page
from django.shortcuts import render
from .utils import get_all_properties
from django.http import JsonResponse
from .utils import get_redis_cache_metrics

def cache_metrics_view(request):
    metrics = get_redis_cache_metrics()
    return JsonResponse(metrics)

@cache_page(60 * 15)  # Still cache the view for 15 minutes
def property_list(request):
    properties = get_all_properties()
    return render(request, 'properties/property_list.html', {'properties': properties})

def property_list_json(request):
    properties = get_all_properties()
    data = [
        {
            "id": prop.id,
            "title": prop.title,
            "description": prop.description,
            "price": float(prop.price),
            "location": prop.location,
            "created_at": prop.created_at.isoformat(),
        }
        for prop in properties
    ]
    return JsonResponse({"data": data})