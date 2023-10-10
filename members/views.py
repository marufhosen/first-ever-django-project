from django.http import HttpResponse
from django.template import loader
import db_config

# test json
person = [
    {
        "name": "Maruf Hosen"
    }
]
# connect mongo_db
is_connect = db_config()


def base(request):
    return HttpResponse(person)

# return a html template
def members(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
