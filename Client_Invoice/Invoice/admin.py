from django.contrib import admin
from django.core.paginator import Paginator
from .models import Current_Year, Backup_Year
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.urls import reverse, path
from django.contrib import messages
import re, csv
from django import forms
from django.shortcuts import render, redirect
import codecs

admin.site.unregister(Group)
admin.site.unregister(User)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('s_no','Name','Clint','Position','Billing','Type','Status','Doj','Invoice','Invoiced_on','Payment_on','Total','Collection','Recruiter')
    search_fields = ['Name']
    list_per_page = 5

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class BackupYearAdmin(admin.ModelAdmin):
    list_display = ('s_no','Name','Clint','Position','Billing','Type','Status','Doj','Invoice','Invoiced_on','Payment_on','Total','Collection','Recruiter')
    search_fields = ['Name']
    list_per_page = 5

    def get_urls(self):
            urls = super().get_urls()
            new_urls = [
                path('upload-csv/', self.upload_csv),
            ]
            return new_urls + urls
            
    def upload_csv(self, request):
        if request.method == 'POST':
            csv_file = request.FILES["csv_upload"]
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            file_data = csv_file.read().decode("utf-8")
            print(file_data)
            csv_data = file_data.split("\n")
            print(csv_data)
            for x in csv_data:
                fields = x.split(",")
                created = Backup_Year.objects.update_or_create(
                    s_no = fields[0],
                    Name = fields[1],
                    Clint = fields[2],
                    Position = fields[3],
                    Empsalary = fields[4],
                    Billing = fields[5],
                    Type = fields[6],
                    Status = fields[7],
                    Invoice = fields[8],
                    Doj = fields[9],
                    Invoiced_on = fields[10],
                    Payment_on = fields[11],
                    Total = fields[12],
                    Collection = fields[13],
                    Recruiter = fields[14],
                )
            messages.warning(request, 'Upload completed...')
            url = reverse('index')
            return HttpResponseRedirect(url)
        form = CsvImportForm()
        data = {'form': form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(Current_Year, EmployeeAdmin)
admin.site.register(Backup_Year, BackupYearAdmin)

