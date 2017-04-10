from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Thwsheji(models.Model):
    popid = models.IntegerField(primary_key=True)
    upid = models.IntegerField()
    quju = models.CharField(max_length=30)
    jiedian = models.CharField(max_length=30)
    jdname = models.CharField(max_length=30)
    sjkyll = models.FloatField()
    sjjdll = models.FloatField()
    sjbf = models.IntegerField()
    sjepgbf = models.IntegerField()
    sjdbkj = models.FloatField()
    opt1 = models.CharField(db_column='OPT1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    opt2 = models.CharField(db_column='OPT2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    opt3 = models.CharField(db_column='OPT3', max_length=45, blank=True, null=True)  # Field name made lowercase.
    opt4 = models.CharField(db_column='OPT4', max_length=45, blank=True, null=True)  # Field name made lowercase.
    opt5 = models.CharField(db_column='OPT5', max_length=45, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField(blank=True, null=True)
    deletetime = models.DateTimeField(blank=True, null=True)
    createowner = models.CharField(max_length=30, blank=True, null=True)
    updateowner = models.CharField(max_length=30, blank=True, null=True)
    deleteowner = models.CharField(max_length=30, blank=True, null=True)
    deleteflag = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'thwsheji'

class Tztesheji(models.Model):
    nodename = models.CharField(primary_key=True,unique=True, max_length=50)
    wgname = models.CharField(max_length=50, blank=True, null=True)
    epggroupname = models.CharField(max_length=50, blank=True, null=True)
    sjkyll = models.IntegerField()
    sjjdll = models.IntegerField()
    sjhmsbf = models.IntegerField()
    sjepgbf = models.IntegerField()
    sjdbkj = models.IntegerField()
    nodeid = models.CharField(max_length=50)
    clusterid = models.CharField(max_length=50)
    clustername = models.CharField(max_length=50)
    opt1 = models.CharField(db_column='OPT1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    opt2 = models.CharField(db_column='OPT2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    opt3 = models.CharField(db_column='OPT3', max_length=45, blank=True, null=True)  # Field name made lowercase.
    opt4 = models.CharField(db_column='OPT4', max_length=45, blank=True, null=True)  # Field name made lowercase.
    opt5 = models.CharField(db_column='OPT5', max_length=45, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField(blank=True, null=True)
    deletetime = models.DateTimeField(blank=True, null=True)
    createowner = models.CharField(max_length=30, blank=True, null=True)
    updateowner = models.CharField(max_length=30, blank=True, null=True)
    deleteowner = models.CharField(max_length=30, blank=True, null=True)
    deleteflag = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'tztesheji'