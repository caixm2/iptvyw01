from django.shortcuts import render
from django.db import connection
import logging

# Create your views here.

def index(request):
    logger = logging.getLogger('django')
    return render(request, 'reports/index.html')

def usrs_in_ippool(request):
    rows = call_p3a_usrs_in_ippool()
    return render(request, 'reports/usrs_in_ippool.html', {'rows': rows})

def call_p3a_usrs_in_ippool():
    with connection.cursor() as cursor:
        #cursor.execute("select ipstart, ipend from tnoc_usr_ippool;")
        #rows = cursor.fetchall()
        args = (16, 'B')
        cursor.callproc("p3a_usrs_in_ippool", args)
        #for results in cursor.stored_results():
        rows = cursor.fetchall()
        cursor.close()
    return rows