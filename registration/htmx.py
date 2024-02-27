from django.contrib.auth import get_user_model
from django.http import HttpResponse


def check_username_exists(request):
    username = request.POST.get("username")
    print(username)
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div style='color: red;'>This username is already exists</div>")
    else:
        return HttpResponse("<div style='color: green;'>This username is available</div>")
