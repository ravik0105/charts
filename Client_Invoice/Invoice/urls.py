from unicodedata import name
from django.urls import URLPattern, path
from .import views
#from list.views import chartView

urlpatterns=[

    path('index/',views.index,name='index'),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('update/<str:pk>/',views.updateCurrent_Year,name='update'),
    path('addrecord/',views.addrecord,name='addrecord'),
    #path('',chartView.as_view(),name='dashboard'),
    path('paid_status/', views.Paid, name="paid_status"),
    path('unpaid_status/', views.Unpaid, name="unpaid_status"),
    path('billing_status/', views.Billing, name="billing_status"),
#    path('records/',views.records,name="records"),
    path('invoice_records/',views.invoice_records,name="invoice_records"),
    path('search/',views.searchbar,name="search"),
    path('downloadcsv/', views.importcsv, name="downloadcsv"),
    
]