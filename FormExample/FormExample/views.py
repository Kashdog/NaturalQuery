# importing required packages
from __future__ import print_function
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.db import connection, transaction
from itertools import *


# disabling csrf (cross site request forgery)
@csrf_exempt
def index(request):
    # if post request came
    if request.method == 'POST':
        # getting values from post
        engquery = request.POST.get('engquery')
        
        from . import eng2sql
        
        cursor = connection.cursor()
        cursor.execute(eng2sql.translate_sentence(engquery))
        table = cursor.fetchall()
        propertyNames = [col[0] for col in cursor.description]
        # adding the values in a context variable
        context = {
            'engquery': engquery,
            'sqlquery': eng2sql.translate_sentence(engquery),
            'data': table,
            'propertyNames': propertyNames,
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