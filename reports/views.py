from django.shortcuts import render
from django.db import connection
import logging
from django.http import HttpResponse

from .forms import AddForm
# Create your views here.

def index(request):
    logger = logging.getLogger('django')
    #return render(request, 'reports/index.html')
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            addnum = int(a) + int(b)
            #return HttpResponse(str(int(a) + int(b)))
            return render(request, 'reports/index.html', {'addnum': addnum})
    else:
        form = AddForm()
    return render(request, 'reports/index.html', {'form': form})

def usrs_in_ippool(request):
    if request.method == 'POST':
        ipnum = request.POST["ipnum"]
        ipfield = request.POST["ipfield"]
        #ipnum = 128
        #ipfield = 'B'
        rows = call_p3a_usrs_in_ippool(ipnum, ipfield)
        return render(request, 'reports/usrs_in_ippool.html', {'rows': rows})
    else:
        pass
    return render(request, 'reports/usrs_in_ippool.html')

def call_p3a_usrs_in_ippool(ipnum, ipfield):
    with connection.cursor() as cursor:
        #cursor.execute("select ipstart, ipend from tnoc_usr_ippool;")
        #rows = cursor.fetchall()
        args = (ipnum, ipfield)
        cursor.callproc("p3a_usrs_in_ippool", args)
        #for results in cursor.stored_results():
        rows = cursor.fetchall()
        cursor.close()
    return rows