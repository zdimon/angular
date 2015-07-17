from django.views.generic.edit import FormView
from .form import AuthForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from django.contrib.auth import login

from django.views.generic import TemplateView
from .forms import AccountForm
from .models import Account

class AccountFormView(TemplateView):
    template_name = 'authentication/profile.html'

    def get_context_data(self, **kwargs):
        context = super(AccountFormView, self).get_context_data(**kwargs)
        account = Account.objects.get(pk=self.request.user.id)
        context.update(form=AccountForm(instance=account))
        return context

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
            out = { 'status': 0, 'message': 'ok', 'username': user.username, 'user_id': user.id }
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
        out = { 'isauth': 1, 'username': request.user.username, 'user_id': request.user.id }        
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


    
