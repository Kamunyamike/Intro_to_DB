from django.http import HttpResponse

def my_message(request):
    message = "Hello, this is a message from the function view!"
    return HttpResponse(message)