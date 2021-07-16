from django.shortcuts import redirect, render
from .models import provider, Credit
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Avg, Max, Min, Sum

provider_name = provider.objects.all()
# Create your views here.
def home(request):
    
    

    return render(request, 'index.html', {'provider_name': provider_name})

def data(request, id):
    
    global provider_id 
    provider_id = id
    content = Credit.objects.filter(provider_id = provider_id).filter(status = "False")
    t_content  = Credit.objects.filter(provider_id = provider_id).filter(status = "True")
    f_content = Credit.objects.filter(provider_id = provider_id)
    global provider_title
    provider_title = provider.objects.get(id=provider_id)
    global remaining, total, paid
    remaining = list(content.aggregate(Sum('amount')).values())[0]
    total = list(f_content.aggregate(Sum('amount')).values())[0]
    paid = list(t_content.aggregate(Sum('amount')).values())[0]


    return render(request, 'table.html', {'provider_name': provider_name, 'data' : content, 'provider_title': provider_title, 'total':total, 'paid':paid, 'remaining':remaining})

def pay(request,b_id):
    a = Credit.objects.get(id = b_id)
    a.status = "True"
    a.save()
    return HttpResponseRedirect('/data/' + str(provider_id))

def reset(request, r_id):
    a = Credit.objects.get(id = r_id)
    a.status = "False"
    a.save()
  
    return HttpResponseRedirect('/data/' + str(provider_id))

def remaining(request):
    return HttpResponseRedirect('/data/' + str(provider_id))



def paid(request):
    paid_content = Credit.objects.filter(provider_id = provider_id).filter(status = 'True')
    return render(request, 'table.html', {'provider_name': provider_name, 'data' : paid_content, 'provider_title': provider_title,'total':total, 'paid':paid, 'remaining':remaining})

def add(request):
    if request.method == 'POST':
        p_id = request.POST['provider']
        date = request.POST['date']
        amount = request.POST['amount']
        c = Credit()
        c.bill_date = date
        c.provider_id = p_id
        c.amount = amount
        c.save()

    else:
        return HttpResponse('something wrong :(')
    return redirect('/')