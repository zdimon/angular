from django.views.generic.edit import FormView
from .form import AuthForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User

class AuthView(FormView):
    template_name = 'main/auth-form.html'
    form_class = AuthForm
    success_url = reverse_lazy('form_data_valid')



@csrf_exempt
def login(request):
    context = { }
    out = {
        'status': 0,
        'message': 'login ok',
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


def registration(request):
    data = json.loads(request.body)
    try: 
        User.objects.get(username=data['username'])
        return HttpResponse(json.dumps({'status': 1, 'message': 'This user already exists!'}), content_type='application/json') 
    except:
        u = User()
        u.username = data['username']
        u.email = data['email']
        u.set_password(data['password1'])
        u.save()
    context = { }
    out = {
        'status': 1,
        'message': 'ok',
    }
    return HttpResponse(json.dumps(out), content_type='application/json') 


    
