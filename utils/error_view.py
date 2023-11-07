from django.http import JsonResponse

def handler404(request, excption):
    message = ('Path not found')
    response = JsonResponse(data={"Error":message})
    response.status_code = 404
    return response


def handler500(request):
    message = ('Internal server error')
    response = JsonResponse(data={"Error":message})
    response.status_code = 500
    return response