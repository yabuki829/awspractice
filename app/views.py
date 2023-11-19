from django.http import HttpResponse


def index(request):
    return HttpResponse('コレをAWSで表示する')