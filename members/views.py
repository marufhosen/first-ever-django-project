from django.http import HttpResponse
from django.template import loader

# TEST JSON
person = [
    {
        "name": "Maruf Hosen"
    }
]

# 
def base(request):
    return HttpResponse(person)

# return a html template
def members(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
