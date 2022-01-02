from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import reportDataForm, OrderForm
from .models import reportData, orders_done
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user.models import Profile



# Create your views here.


#This is for the front page of sending work orders, this is connected to 'templates/dashboard/index.html' 
def index(request):
    report_data = reportData.objects.all()
    

    if request.method == "POST":
        form = reportDataForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Request Sent!')
            return redirect('dashboard-index')
    else:
        form = reportDataForm()

    context = {
        'report_data': report_data,
        'form': form,
        
    }

    return render(request, 'dashboard/index.html', context)

#Page for Staff Views, allows staff to send work orders and other features. Requries login access page found at 'templates/dashboard/staff.html' 
@login_required
def staff_index(request):
    report_data = reportData.objects.all()
    counter = reportData.objects.count()
    #Count how many reports based on cateogries
    pl = reportData.objects.filter(cateogry="PL").count
    el = reportData.objects.filter(cateogry="EL").count
    mt = reportData.objects.filter(cateogry="MT").count
    cas = reportData.objects.filter(cateogry="CAS").count
    eng= reportData.objects.filter(cateogry="ENG").count
    ext = reportData.objects.filter(cateogry="EXT").count
    

    context = {
        'report_data': report_data,
        'counter' : counter, 
        'pl':pl,
        'el':el,
        'mt':mt,
        'cas':cas,
        'eng':eng,
        'ext':ext,

    }
    return render(request, 'dashboard/staff.html', context)

#This is the page for the Admin Portal. Found at 'templates/dashboard/admin.html'
@login_required
def admin_index(request):
    report_data = reportData.objects.all()
    staff_data = Profile.objects.all()
    pl = reportData.objects.filter(cateogry="PL").count
    el = reportData.objects.filter(cateogry="EL").count
    mt = reportData.objects.filter(cateogry="MT").count
    cas = reportData.objects.filter(cateogry="CAS").count
    eng= reportData.objects.filter(cateogry="ENG").count
    ext = reportData.objects.filter(cateogry="EXT").count
    
    context ={
        'report_data':report_data,
        'staff_data':staff_data,
        'pl':pl,
        'el':el,
        'mt':mt,
        'cas':cas,
        'eng':eng,
        'ext':ext,
    }
    return render(request, 'dashboard/admin.html', context)


#This is for when sending work orders. Once sent out, it will delete the work order from the database. Found at 'templates/dashboard/sent_order.html'
@login_required
def staff_delete(request, key):
    item = reportData.objects.get(id=key)
    if request.method=='POST':
        form = OrderForm(request.POST)
        item.delete()
        return redirect('staff-index')
        

    return render(request, 'dashboard/sent_order.html')


#This is to view for when a staff or Admin wants to view and delete a work order if it doesn't meet requirements for order being sent. Found at 'templates/dashboard/staff_view.html'
@login_required
def staff_view(request, pk):
    report_data = reportData.objects.all()
    obj = reportData.objects.get(id=pk)
    if request.method =='POST':
        obj.delete()
        return redirect('staff-index')
    context = {
        'report_data' : report_data,
        'obj' : obj,
    }
    return render(request, 'dashboard/staff_view.html', context)

#This is to view and fire employees from the admin portal. If Fires, deletes them from the User Database. Found at 'templates/dashboard/admiv_view.html'
@login_required
def admin_fire(request,key):
    obj = Profile.objects.get(id=key)
    if request.method == 'POST':
        User.objects.get(username=obj.staff.username).delete()
        obj.delete()
       
        return redirect('admin-index')
    
    return render(request, 'dashboard/admin_view.html')


# For Admin to view each employee, created bugs with other features
"""
def admin_staff_profile(request, key):
    obj = Profile.objects.get(id=key)
    if request.method == 'POST':
        return redirect('admin-index')
    
    return render(request, 'dashboard/admin_staff_view.html')
"""