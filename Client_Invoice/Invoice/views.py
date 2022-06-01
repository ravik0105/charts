from asyncio.windows_events import NULL
from django.shortcuts import render,redirect
from . models import Current_Year
from .forms import Current_YearForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.db.models import Avg, F, Window
import pandas as pd
import numpy as np
import csv
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator


# Create your views here.

@login_required()
def dashboard(request):
    orders=Current_Year.objects.all()
    
    #Total=Order.objects.filter(Total).count()
    Paid=Current_Year.objects.filter(Status='PAID').count()
    Unpaid=Current_Year.objects.filter(Status='UNPAID').count()
    
    process_status = Current_Year.objects.values('Billing','Collection').order_by('s_no')
    df = pd.DataFrame(process_status)

    monthchart = df.groupby('Collection')['Billing'].sum()
    billing = Current_Year.objects.aggregate(Sum("Billing"))
    Empsalary = Current_Year.objects.aggregate(Sum("Empsalary"))
    

    process_status2 = Current_Year.objects.values('Billing','Recruiter').order_by('s_no')
    df2 = pd.DataFrame(process_status2)


    recutchart = df2.groupby('Recruiter')['Billing'].sum()
    #billing2 = Order.objects.aggregate(Sum("Billing"))
    


    billings = billing["Billing__sum"]
    emp_salary = Empsalary["Empsalary__sum"]
    print(emp_salary)

    df1 = pd.DataFrame(process_status)
    #Pain_Unpaid = Order.objects.filter(Status='PAID')
    process_status1 = Current_Year.objects.values('Status','Billing').order_by('s_no')
    df1 = pd.DataFrame(process_status1)
    paidchart = df1.groupby('Status')['Billing'].sum()
    
    content = {
        'orders':orders,
        'Paid':Paid,
        'Unpaid':Unpaid,
        'process_status':process_status,
        'monthchart':monthchart,
        'paidchart':paidchart,
        'billings':billings,
        'emp_salary':emp_salary,
        'recutchart': recutchart
    }
   
    return render(request,'Invoice/dashboard.html',content)


def updateCurrent_Year (request,pk):
    order=Current_Year.objects.get(s_no=pk)
    form = Current_YearForm(request.POST or None, instance=order)

    if form.is_valid():
        form.save()
        return redirect('invoice_records')
    context={
        'order':order,
        'form':form,
    }
    return render(request,'Invoice/order_create.html',context)

def addrecord(request):
    submitted = False
    if request.method == "POST":
        form =Current_YearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/addrecord?submitted=True')

    else:
        form = Current_YearForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'Invoice/add_record.html',{'form':form, 'submitted':submitted})

@login_required()
def index(request):
    orders=Current_Year.objects.all()
    
    #Total=Order.objects.filter(Total).count()
    Paid=Current_Year.objects.filter(Status='PAID').count()
    Unpaid=Current_Year.objects.filter(Status='UNPAID').count()
    
    process_status = Current_Year.objects.values('Billing','Collection').order_by('s_no')
    df = pd.DataFrame(process_status)

    monthchart = df.groupby('Collection')['Billing'].sum()
    billing = Current_Year.objects.aggregate(Sum("Billing"))
    Empsalary = Current_Year.objects.aggregate(Sum("Empsalary"))
    

    process_status2 = Current_Year.objects.values('Billing','Recruiter').order_by('s_no')
    df2 = pd.DataFrame(process_status2)


    recutchart = df2.groupby('Recruiter')['Billing'].sum()
    #billing2 = Order.objects.aggregate(Sum("Billing"))
    


    billings = billing["Billing__sum"]
    emp_salary = Empsalary["Empsalary__sum"]
    #print(recutchart)

    ra = recutchart.to_dict()
    labels = list(ra.keys())
    data = list(ra.values())

    print(labels)
    print(data)

    df1 = pd.DataFrame(process_status)
    #Pain_Unpaid = Order.objects.filter(Status='PAID')
    process_status1 = Current_Year.objects.values('Status','Billing').order_by('s_no')
    df1 = pd.DataFrame(process_status1)
    
    paidchart = df1.groupby('Status')['Billing'].sum()
    rb = paidchart.to_dict()
    labels1 = list(rb.keys())
    data1 = list(rb.values())


    content = {
        'orders':orders,
        'Paid':Paid,
        'Unpaid':Unpaid,
        'process_status':process_status,
        'monthchart':monthchart,
        'paidchart':paidchart,
        'billings':billings,
        'emp_salary':emp_salary,
        'labels': labels,
        'data': data,
        'recutchart': recutchart,
        'labels1': labels1,
        'data1': data1
    }
   
    return render(request,'Invoice/index.html',content)


def Paid(request):
    a = Current_Year.objects.filter(Status='PAID')
    return render(request, 'Invoice/paid.html',{'a':a})


def Unpaid(request):
    b = Current_Year.objects.filter(Status='UNPAID')
    return render(request, 'Invoice/unpaid.html',{'b':b})

def Billing (request):
    billi_view=Current_Year.objects.all()
    return render(request, 'Invoice/billing.html',{'billi_view':billi_view})


def searchbar(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues= Current_Year.objects.filter(Name__contains=searched) | Current_Year.objects.filter(Invoice__contains=searched)
        return render (request, 'Invoice/searchbar.html',{'searched':searched , 'venues':venues})

    else:
        return render(request,'Invoice/searchbar.html',{}) 
@login_required()
def invoice_records(request):
    invoice_records = Current_Year.objects.all()
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        print(fromdate)
        print(todate)
        result=Current_Year.objects.raw('select s_no,Name,Clint,Position,Empsalary,Billing,Type,Status,Invoice,Doj,Invoiced_on,Payment_on,Total,Collection,Recruiter from list_order where Invoiced_on between "'+str(fromdate)+'" and "'+str(todate)+'"')
        print(result)
        return render(request, 'Invoice/invoice_records.html',{'result':result})

    return render(request,'Invoice/invoice_records.html',{'result':invoice_records})

def importcsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Backup_Year_Records.csv'
    writer = csv.writer(response)
    articles = Current_Year.objects.all()
    print(articles)
    writer.writerow(['s_no','Name','Clint','Position','Billing','Type','Status','Doj','Invoice','Invoiced_on','Payment_on','Total','Collection','Recruiter'])
    for article in articles:
        writer.writerow([article.s_no, article.Name, article.Clint, article.Position, article.Billing, article.Type, article.Status, article.Doj,article.Invoice,article.Invoiced_on,article.Payment_on,article.Total,article.Collection,article.Recruiter])
        return response
    return redirect('index')