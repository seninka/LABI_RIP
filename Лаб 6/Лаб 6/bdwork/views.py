from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.template import Context
from django.template.context_processors import csrf
from django.views import generic
from bdwork.models import My_user, Ser_f_users
from .forms import ServesForm

# Create your views here.


def basicone(request):
    view = "basicone"
    html = "<html><body>This is %s view</body></html>" % view
    return HttpResponse(html)


class Users(generic.ListView):
    template_name = "users0.html"

    def get_queryset(self):
        return My_user.objects.all()


def users(request):
    return render(request, 'users.html', {'users': My_user.objects.all()})



def singleuser(request, user_id = 1):
        serves_form =  ServesForm
        args = {}
        args.update(csrf(request))
        args['user'] = My_user.objects.get(id=user_id)
        args['servese_id'] = Ser_f_users.objects.filter(customer=user_id)
        args['form'] = serves_form
        return render(request,'singleuser.html',args)


def addserves(request, user_id):
    if request.POST:
        form = ServesForm(request.POST)
        if form.is_valid():
            serv = form.save(commit=False)
            serv.customer = Ser_f_users.objects.get(id=user_id)
            form.save()
    return redirect("/users/get/%s" % user_id)

