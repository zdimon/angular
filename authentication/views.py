from django.views.generic.edit import FormView
from .form import AuthForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

class AuthView(FormView):
    template_name = 'main/auth-form.html'
    form_class = AuthForm
    success_url = reverse_lazy('form_data_valid')



@csrf_exempt
def login(request):
    context = { }
    out = {
        'status': 0,
        'message': 'ok',
    }
    return HttpResponse(json.dumps(out), content_type='application/json')   


@csrf_exempt
def logout(request):
    context = { }
    out = {
        'status': 0,
        'message': 'ok',
    }
    return HttpResponse(json.dumps(out), content_type='application/json') 

@csrf_exempt
def registration(request):
    context = { }
    out = {
        'status': 0,
        'message': 'ok',
    }
    return HttpResponse(json.dumps(out), content_type='application/json') 


    
