from django.views.generic.edit import FormView
from .form import AuthForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from django.contrib.auth import login

class AuthView(FormView):
    template_name = 'main/auth-form.html'
    form_class = AuthForm
    success_url = reverse_lazy('form_data_valid')




def login_user(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    
    #import pdb; pdb.set_trace()
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request,user)
            out = { 'status': 0, 'message': 'ok' }
        else:
            out = { 'status': 1, 'message': 'Password does not match!' }
    except:
        out = { 'status': 1, 'message': 'User does not found!' }
        
    context = { }
   
    return HttpResponse(json.dumps(out), content_type='application/json')   


def logout(request):
    from django.contrib.auth import logout
    logout(request)
    out = {
        'status': 0,
        'message': 'ok',
    }
    return HttpResponse(json.dumps(out), content_type='application/json') 


def isauth(request):
    if request.user.is_authenticated():
        out = { 'isauth': 1 }        
    else:
        out = { 'isauth': 0 }        
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


    
