# importing required packages
from __future__ import print_function
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


# disabling csrf (cross site request forgery)
@csrf_exempt
def index(request):
    # if post request came
    if request.method == 'POST':
        # getting values from post
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        from . import eng2sql
        


        # adding the values in a context variable
        context = {
            'name': name,
            'email': eng2sql.translate_sentence(name),
            'phone': phone
        }

        # getting our showdata template
        template = loader.get_template('showdata.html')

        # returing the template
        return HttpResponse(template.render(context, request))
    else:
        # if post request is not true
        # returing the form template
        template = loader.get_template('index.html')
        return HttpResponse(template.render())