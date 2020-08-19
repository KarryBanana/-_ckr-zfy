from django.shortcuts import render

# Create your views here.
import pymysql
from django.http import JsonResponse


def get_notice(request):
    con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
    cur=con.cursor()
    id=request.POST['id']
    op=request.POST['op']
    op=int(op)
    sql="select nid,content,ntime,isread from Noticelist where isread<>-1 and id="+str(id)+" and type="+str(op)
    cur.execute(sql)
    con.close()
    return JsonResponse(cur.fetchall(),safe=False)


def read_notice(request):
    con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
    cur=con.cursor()
    nid=request.POST['nid']
    sql="update table Noticelist set isread=1 where nid="+str(nid)
    cur.execute(sql)
    cur.connection.commit()
    con.close()
    return JsonResponse(1,safe=False)


def check_notice(request):
    con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
    cur=con.cursor()
    id=request.POST['id']
    sql="select count(*) from Noticelist where isread=0 and id="+str(id)
    nr=0
    cur.execute(sql)
    for row in cur:
        nr=row[0]

    sql="select count(*) from Msglist where ishandle=0 and receiveid="+str(id)
    cur.execute(sql)
    for row in cur:
        nr+=row[0]
    if nr>0:return JsonResponse(1,safe=False)
    else:return JsonResponse(0,safe=False)


def delete_notice(request):
    con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
    cur=con.cursor()
    nid=request.POST['nid']
    # sql="delete from Noticelist where nid="+str(nid)
    sql="update Noticelist set isread=-1 where nid="+str(nid)
    cur.execute(sql)
    cur.connection.commit()
    con.close()
    return JsonResponse(1,safe=False)


def clear_notice(request):
    con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
    cur=con.cursor()
    id=request.POST['id']
    # sql="delete from Noticelist where id="+str(id)
    sql="update Noticelist set isread=-1 where id="+str(id)
    cur.execute(sql)
    cur.connection.commit()
    con.close()
    return JsonResponse(1,safe=False)