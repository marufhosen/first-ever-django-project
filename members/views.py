from django.http import HttpResponse
from django.template import loader

person = [
    {
        "name": "Maruf Hosen"
    }
]


# def members(request):
#     return HttpResponse(person)

def members(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
