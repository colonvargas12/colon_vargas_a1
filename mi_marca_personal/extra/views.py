from django.http import HttpResponse

def extra_inicio(request):
    return HttpResponse("App secundaria creada correctamente. Esta app queda como complemento del proyecto.")
