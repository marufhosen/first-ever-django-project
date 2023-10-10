from django.http import HttpResponse

# get ip


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def board(request):
    ip = get_client_ip(request)
    param_id = request.GET.get('id', 1)
    print(f"Your ip is {ip}")
    print(f"Your request params is {param_id}")
    return HttpResponse("I'm from board")


# Create your views here.
