from django.shortcuts import render
from django.db import connection
import logging
from django.http import HttpResponse
import time

from reports.tools.forms import AddForm, UsrInPoolForm
# Create your views here.
'''
index显示内容
'''
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

'''
显示一个IP段内有多少用户和对应的区局
'''
def usrs_in_ippool(request):
    time1 = time.time()
    ursinpool = UsrInPoolForm()
    '''if request.method == 'POST':
        ipnum = request.POST["ipnum"]
        ipfield = request.POST["ipfield"]
        sipaddr = request.POST.get("sipaddr","")
        daylenth = request.POST["daylenth"]
        plat = request.POST["plat"]
        zero = request.POST.get("zero",1)

        args = (ipnum, ipfield, daylenth, plat, sipaddr, zero)
        rows = call_p3a_usrs_in_ippool(*args)
        rowslen = len(rows)
        time2 =time.time()
        timeminus = round(time2-time1,3)
        return render(request, 'reports/usrs_in_ippool.html', {'rows': rows, 'timeminus': timeminus,'rowslen':rowslen})'''
    return render(request, 'reports/usrs_in_ippool.html', {'ursinpool': ursinpool})

def call_p3a_usrs_in_ippool(*args):
    with connection.cursor() as cursor:
        #args = (ipnum, ipfield)
        #cursor.callproc("p3a_usrs_in_ippool", args)
        cursor.callproc("pusrs_in_ippool_fin", args)
        rows = cursor.fetchall()
        cursor.close()
    return rows