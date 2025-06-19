# configurations/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Configuration
import json

#  Backend Task 1: GET configuration by ID
def get_configuration(request, id):
    if request.method == "GET":
        try:
            config = Configuration.objects.get(configurationId=id)
            return JsonResponse(config.array, safe=False)
        except Configuration.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)
    return JsonResponse({"error": "Method not allowed"}, status=405)

#  Backend Task 2: PUT update remark by ID
@csrf_exempt
def update_remark(request, id):
    print(" PUT view hit with ID:", id)
    if request.method == "PUT":
        try:
            config = Configuration.objects.get(configurationId=id)
            data = json.loads(request.body)
            # remark = data.get("remark", "")
            # config.remark = remark if remark is not None else ""
            config.remark = data.get("remark", "")
            config.save()
            return JsonResponse({"message": "success"})
        except Configuration.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)
    return JsonResponse({"error": "Method not allowed"}, status=405)

#  Frontend Task 1: Render fetch_config.html
def fetch_page(request):
    return render(request, "configurations/fetch_config.html")

#  Frontend Task 2: Render update_remark.html
def update_page(request):
    return render(request, "configurations/update_remark.html")






# from django.shortcuts import render

# # Create your views here.
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render
# from .models import Configuration
# import json

# def get_configuration(request, id):
#     try:
#         config = Configuration.objects.get(configurationId=id)
#         return JsonResponse(config.array, safe=False)
#     except Configuration.DoesNotExist:
#         return JsonResponse({"error": "Not found"}, status=404)

# @csrf_exempt
# def update_remark(request, id):
#     if request.method == "PUT":
#         try:
#             config = Configuration.objects.get(configurationId=id)
#             data = json.loads(request.body)
#             config.remark = data.get("remark", "")
#             config.save()
#             return JsonResponse({"message": "success"})
#         except Configuration.DoesNotExist:
#             return JsonResponse({"error": "Not found"}, status=404)

# def fetch_page(request):
#     return render(request, "configurations/fetch_config.html")

# def update_page(request):
#     return render(request, "configurations/update_remark.html")
