# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Iphw(models.Model):
    pop = models.CharField(db_column='POP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    设备编号 = models.CharField(max_length=45, blank=True, null=True)
    台账编号 = models.CharField(max_length=45, blank=True, null=True)
    机房名称 = models.CharField(max_length=45, blank=True, null=True)
    设备名称 = models.CharField(max_length=45, blank=True, null=True)
    公网ip = models.CharField(db_column='公网IP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    设备型号 = models.CharField(max_length=45, blank=True, null=True)
    平台名称 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iphw'


class Ipwl(models.Model):
    地址分类 = models.CharField(max_length=45, blank=True, null=True)
    ip地址 = models.CharField(db_column='IP地址', max_length=45)  # Field name made lowercase.
    平台 = models.CharField(max_length=45, blank=True, null=True)
    用途 = models.CharField(max_length=45, blank=True, null=True)
    台账 = models.CharField(max_length=45, blank=True, null=True)
    主机名 = models.CharField(max_length=45, blank=True, null=True)
    pop点 = models.CharField(db_column='POP点', max_length=45, blank=True, null=True)  # Field name made lowercase.
    机房 = models.CharField(max_length=45, blank=True, null=True)
    对应交换机端口 = models.CharField(max_length=45, blank=True, null=True)
    对应主机物理网口 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipwl'


class T3AUsr(models.Model):
    adslname = models.CharField(max_length=20)
    loginname = models.CharField(primary_key=True, max_length=30)
    ipaddr = models.CharField(max_length=50, blank=True, null=True)
    logintime = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    mac = models.CharField(max_length=20, blank=True, null=True)
    stbid = models.CharField(max_length=50, blank=True, null=True)
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
        managed = False
        db_table = 't3a_usr'


class Tfhdbspace(models.Model):
    nodeename = models.CharField(db_column='nodeEname', max_length=50)  # Field name made lowercase.
    dbdatetime = models.DateTimeField()
    usedspace = models.FloatField()
    freespace = models.FloatField()
    totalspace = models.FloatField()
    usedpercent = models.FloatField()
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
        managed = False
        db_table = 'tfhdbspace'


class Tfhepgbf(models.Model):
    epgip = models.CharField(max_length=50)
    epgname = models.CharField(max_length=50)
    epgmaxbf = models.IntegerField()
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
        managed = False
        db_table = 'tfhepgbf'


class Tfhepgsheji(models.Model):
    epgname = models.CharField(max_length=50)
    epgip = models.CharField(unique=True, max_length=50)
    epgsjbf = models.IntegerField()
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
        managed = False
        db_table = 'tfhepgsheji'


class Tfhhmsbf(models.Model):
    hmsdatetime = models.DateTimeField()
    nodeename = models.CharField(db_column='nodeEname', max_length=50)  # Field name made lowercase.
    cpname = models.CharField(max_length=50)
    maxoutput = models.FloatField()
    maxinput = models.FloatField()
    maxhmsbf = models.IntegerField()
    maxbacksrc = models.IntegerField()
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
        managed = False
        db_table = 'tfhhmsbf'


class Tfhsheji(models.Model):
    nodearea = models.CharField(max_length=50)
    nodecname = models.CharField(db_column='nodeCname', unique=True, max_length=50)  # Field name made lowercase.
    nodeename = models.CharField(db_column='nodeEname', unique=True, max_length=50)  # Field name made lowercase.
    nodeid = models.CharField(unique=True, max_length=50)
    sjkyll = models.IntegerField()
    sjjdll = models.IntegerField()
    sjjdbf = models.IntegerField()
    sjdbkj = models.IntegerField()
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
        managed = False
        db_table = 'tfhsheji'


class Tfhyewu(models.Model):
    cpename = models.CharField(db_column='cpEname', max_length=50)  # Field name made lowercase.
    cpname = models.CharField(max_length=50)
    cptype = models.CharField(max_length=50)
    connzteflag = models.CharField(max_length=1)
    onlineflag = models.CharField(max_length=1)
    yewurukou = models.CharField(max_length=50, blank=True, null=True)
    cdntype = models.CharField(max_length=50, blank=True, null=True)
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
        managed = False
        db_table = 'tfhyewu'


class Thwethtraffic(models.Model):
    jiedian = models.CharField(max_length=30)
    ipaddr = models.CharField(max_length=30)
    srvtype = models.CharField(max_length=30)
    ethport = models.CharField(max_length=30)
    ethbandwidth = models.IntegerField()
    avginput = models.IntegerField()
    avgoutput = models.IntegerField()
    maxinput = models.IntegerField()
    maxoutput = models.IntegerField()
    inputper = models.IntegerField()
    outputper = models.IntegerField()
    status = models.CharField(max_length=30)
    ethinfo = models.CharField(max_length=30, blank=True, null=True)
    errornum = models.IntegerField()
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
        managed = False
        db_table = 'thwethTraffic'


class Thwsheji(models.Model):
    popid = models.IntegerField(unique=True)
    upid = models.IntegerField()
    quju = models.CharField(max_length=30)
    jiedian = models.CharField(unique=True, max_length=30)
    jdname = models.CharField(unique=True, max_length=30)
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
        managed = False
        db_table = 'thwsheji'


class Thwtongji(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    popid = models.CharField(max_length=10)
    upid = models.CharField(max_length=10)
    jiedian = models.CharField(max_length=30)
    tjdbkj = models.IntegerField(blank=True, null=True)
    tjsykj = models.IntegerField(blank=True, null=True)
    tjkjsyl = models.IntegerField(blank=True, null=True)
    tjepgrl = models.IntegerField(blank=True, null=True)
    tjepgsy = models.IntegerField(blank=True, null=True)
    tjepgsyl = models.IntegerField(blank=True, null=True)
    tjhmsrl = models.IntegerField(blank=True, null=True)
    tjhmssy = models.IntegerField(blank=True, null=True)
    tjhmssyl = models.IntegerField(blank=True, null=True)
    tjgfdb = models.IntegerField(blank=True, null=True)
    tjgfzb = models.IntegerField(blank=True, null=True)
    tjgq = models.IntegerField(blank=True, null=True)
    tjbq = models.IntegerField(blank=True, null=True)
    opt1 = models.CharField(max_length=45, blank=True, null=True)
    opt2 = models.CharField(max_length=45, blank=True, null=True)
    opt3 = models.CharField(max_length=45, blank=True, null=True)
    opt4 = models.CharField(max_length=45, blank=True, null=True)
    opt5 = models.CharField(max_length=45, blank=True, null=True)
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField()
    deletetime = models.DateTimeField(blank=True, null=True)
    createowner = models.CharField(max_length=45)
    updateowner = models.CharField(max_length=45)
    deleteowner = models.CharField(max_length=45, blank=True, null=True)
    deleteflag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'thwtongji'


class TmpTfhdbspace(models.Model):
    nodeename = models.CharField(db_column='nodeEname', max_length=50)  # Field name made lowercase.
    dbdatetime = models.DateTimeField()
    usedspace = models.FloatField()
    freespace = models.FloatField()
    totalspace = models.FloatField()
    usedpercent = models.FloatField()
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
        managed = False
        db_table = 'tmp_tfhdbspace'


class TmpTfhepgbf(models.Model):
    epgip = models.CharField(max_length=50)
    epgname = models.CharField(max_length=50)
    epgmaxbf = models.IntegerField()
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
        managed = False
        db_table = 'tmp_tfhepgbf'


class TmpTfhhmsbf(models.Model):
    hmsdatetime = models.DateTimeField()
    nodeename = models.CharField(db_column='nodeEname', max_length=50)  # Field name made lowercase.
    cpname = models.CharField(max_length=50)
    maxoutput = models.FloatField()
    maxinput = models.FloatField()
    maxhmsbf = models.IntegerField()
    maxbacksrc = models.IntegerField()
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
        managed = False
        db_table = 'tmp_tfhhmsbf'


class TmpThwethtraffic(models.Model):
    jiedian = models.CharField(max_length=30)
    ipaddr = models.CharField(max_length=30)
    srvtype = models.CharField(max_length=30)
    ethport = models.CharField(max_length=30)
    ethbandwidth = models.IntegerField()
    avginput = models.IntegerField()
    avgoutput = models.IntegerField()
    maxinput = models.IntegerField()
    maxoutput = models.IntegerField()
    inputper = models.IntegerField()
    outputper = models.IntegerField()
    status = models.CharField(max_length=30)
    ethinfo = models.CharField(max_length=30, blank=True, null=True)
    errornum = models.IntegerField()
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
        managed = False
        db_table = 'tmp_thwethTraffic'


class TmpThwtongji(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    popid = models.CharField(max_length=10)
    upid = models.CharField(max_length=10)
    jiedian = models.CharField(max_length=30)
    tjdbkj = models.IntegerField(blank=True, null=True)
    tjsykj = models.IntegerField(blank=True, null=True)
    tjkjsyl = models.IntegerField(blank=True, null=True)
    tjepgrl = models.IntegerField(blank=True, null=True)
    tjepgsy = models.IntegerField(blank=True, null=True)
    tjepgsyl = models.IntegerField(blank=True, null=True)
    tjhmsrl = models.IntegerField(blank=True, null=True)
    tjhmssy = models.IntegerField(blank=True, null=True)
    tjhmssyl = models.IntegerField(blank=True, null=True)
    tjgfdb = models.IntegerField(blank=True, null=True)
    tjgfzb = models.IntegerField(blank=True, null=True)
    tjgq = models.IntegerField(blank=True, null=True)
    tjbq = models.IntegerField(blank=True, null=True)
    opt1 = models.CharField(max_length=45, blank=True, null=True)
    opt2 = models.CharField(max_length=45, blank=True, null=True)
    opt3 = models.CharField(max_length=45, blank=True, null=True)
    opt4 = models.CharField(max_length=45, blank=True, null=True)
    opt5 = models.CharField(max_length=45, blank=True, null=True)
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField()
    deletetime = models.DateTimeField(blank=True, null=True)
    createowner = models.CharField(max_length=45)
    updateowner = models.CharField(max_length=45)
    deleteowner = models.CharField(max_length=45, blank=True, null=True)
    deleteflag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tmp_thwtongji'


class TmpTztedbkj(models.Model):
    seqnum = models.IntegerField(blank=True, null=True)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    qryinterval = models.CharField(max_length=30)
    hmsname = models.CharField(max_length=50)
    dbsjkj = models.IntegerField()
    dbsykj = models.IntegerField()
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
        managed = False
        db_table = 'tmp_tztedbkj'


class TmpTzteepgbf(models.Model):
    epgdate = models.DateField()
    epgtime = models.CharField(max_length=30)
    epgname = models.CharField(max_length=50)
    epgbf = models.IntegerField()
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
        managed = False
        db_table = 'tmp_tzteepgbf'


class TmpTztehmsbf(models.Model):
    seqnum = models.IntegerField(blank=True, null=True)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    qryinterval = models.CharField(max_length=30)
    hmsname = models.CharField(max_length=50)
    livenum = models.IntegerField()
    livebandwidth = models.IntegerField()
    vodnum = models.IntegerField()
    vodbandwidth = models.IntegerField()
    tvodnum = models.IntegerField()
    tvodbandwidth = models.IntegerField()
    tstvnum = models.IntegerField()
    tstvbandwidth = models.IntegerField()
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
        managed = False
        db_table = 'tmp_tztehmsbf'


class TnocUsrIppool(models.Model):
    ipstart = models.CharField(primary_key=True, max_length=50)
    ipend = models.CharField(max_length=50)
    quju = models.CharField(max_length=50)
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField(blank=True, null=True)
    deletetime = models.DateTimeField(blank=True, null=True)
    createowner = models.CharField(max_length=30, blank=True, null=True)
    updateowner = models.CharField(max_length=30, blank=True, null=True)
    deleteowner = models.CharField(max_length=30, blank=True, null=True)
    deleteflag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tnoc_usr_ippool'


class TywUsr(models.Model):
    adslname = models.CharField(max_length=20)
    loginname = models.CharField(primary_key=True, max_length=30)
    ipaddr = models.CharField(max_length=50, blank=True, null=True)
    logintime = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    mac = models.CharField(max_length=20, blank=True, null=True)
    stbid = models.CharField(max_length=50, blank=True, null=True)
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
        managed = False
        db_table = 'tyw_usr'


class Tztedayrpt(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nodename = models.CharField(max_length=50)
    nodeid = models.CharField(max_length=50)
    avgwidth = models.FloatField()
    sjjdll = models.FloatField()
    peakjdll = models.FloatField()
    jdllper = models.FloatField()
    sjepgbf = models.FloatField()
    peakepgbf = models.FloatField()
    epgbfper = models.FloatField()
    sjhmsbf = models.FloatField()
    peakhmsbf = models.FloatField()
    hmsbfper = models.FloatField()
    sjdbkj = models.FloatField()
    peakdbkj = models.FloatField()
    dbkjper = models.FloatField()
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
        managed = False
        db_table = 'tzteDayRpt'


class Tztedayrptareasum(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clustername = models.CharField(max_length=50)
    clusterid = models.CharField(max_length=50)
    avgwidth = models.FloatField()
    nodenum = models.FloatField()
    sjjdllsum = models.FloatField()
    peakjdllsum = models.FloatField()
    jdllsumper = models.FloatField()
    sjepgbfsum = models.FloatField()
    peakepgbfsum = models.FloatField()
    epgbfsumper = models.FloatField()
    sjhmsbfsum = models.FloatField()
    peakhmsbfsum = models.FloatField()
    hmsbfsumper = models.FloatField()
    sjdbkjsum = models.FloatField()
    peakdbkjsum = models.FloatField()
    dbkjsumper = models.FloatField()
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
        managed = False
        db_table = 'tzteDayRptAreaSum'


class Tztedbkj(models.Model):
    hmsname = models.CharField(max_length=50)
    dbsjkj = models.IntegerField()
    dbsykj = models.IntegerField()
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
        managed = False
        db_table = 'tztedbkj'


class Tzteepgbf(models.Model):
    epgname = models.CharField(max_length=50)
    epgbf = models.IntegerField()
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
        managed = False
        db_table = 'tzteepgbf'


class Tzteepggrpsvr(models.Model):
    epggroupid = models.IntegerField()
    epggroupname = models.CharField(max_length=50)
    epgterminalid = models.IntegerField(unique=True)
    epgname = models.CharField(unique=True, max_length=50)
    epgipaddr = models.CharField(max_length=30)
    epgmaxnum = models.IntegerField()
    epgstatus = models.CharField(max_length=30)
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
        managed = False
        db_table = 'tzteepggrpsvr'


class Tztehmsbf(models.Model):
    hmsname = models.CharField(max_length=50)
    livenum = models.IntegerField()
    livebandwidth = models.IntegerField()
    vodnum = models.IntegerField()
    vodbandwidth = models.IntegerField()
    tvodnum = models.IntegerField()
    tvodbandwidth = models.IntegerField()
    tstvnum = models.IntegerField()
    tstvbandwidth = models.IntegerField()
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
        managed = False
        db_table = 'tztehmsbf'


class Tztesheji(models.Model):
    nodename = models.CharField(unique=True, max_length=50)
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

