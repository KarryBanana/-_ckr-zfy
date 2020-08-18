from django.shortcuts import render

# Create your views here.
import pymysql
from django.http import JsonResponse


def save_doc(request):
    con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
    cur=con.cursor()
    id=request.POST['num']
    msg=request.POST['msg']
    userid=request.POST['userid']
    sql="update Table_file set doctext='"+msg+"' where id="+str(id)
    cur.execute(sql)
    sql="update Table file set lastauthor_id="+str(userid)+",lasttime=now() where id="+str(id)
    cur.execute(sql)
    cur.connection.commit()
    con.close()
    return JsonResponse(1,safe=False)


def change_info(request):
    con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
    cur=con.cursor()
    id=request.POST['id']
    msg=request.POST['msg']
    op=request.POST['op']
    op=int(op)
    opc=""
    if op==1:opc="docname"
    elif op==2:opc="doctitle"
    elif op==3:opc="docintro"
    sql="update Table_file set "+opc+"='"+msg+"' where id="+str(id)
    cur.execute(sql)
    cur.connection.commit()
    con.close()
    return JsonResponse(1,safe=False)


def get_doc(request):
    con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
    cur=con.cursor()
    id=request.POST['id']
    op=request.POST['op']
    opc=""
    op=int(op)
    print(op)
    if op==1:opc="doctitle"
    if op==2:opc="docintro"
    if op==3:opc="doctext"
    sql="select "+opc+" from Table_file where id="+str(id)
    print(sql)
    cur.execute(sql)
    chars=""
    for row in cur:
        chars=row[0]
    con.close()
    return JsonResponse(chars,safe=False)


# def submit_comment(request):
#     con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
#     cur=con.cursor()
#     id=request.POST['id']
#     docnum=request.POST['docnum']
#     content=request.POST['content']
#     sql="insert into Commentlist values('"+content+"',"+str(id)+","+str(docnum)+",now())"
#     cur.execute(sql)
#     sql="select username from auth_user where id="+str(id)
#     cur.execute(sql)
#     for row in cur:
#         username=row[0]
#     sql = "select docname from Table_file where id=" + str(docnum)
#     cur.execute(sql)
#     for row in cur:
#         docname = row[0]
#     content=username+" 评论了您的文档: "+docname+" ,去看看吧!"
#     sql = "select author_id from Table_file where id=" + str(docnum)
#     cur.execute(sql)
#     for row in cur:
#         author_id = row[0]
#     sql = "insert into Noticelist values(," + str(author_id) + ",'" + content + "',now(),0)"
#
#     cur.connection.commit()
#     con.close()
#     return JsonResponse(1,safe=False)
#
#
# def get_comments(request):
#     con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
#     cur=con.cursor()
#     docnum=request.POST['docnum']
#     sql="select auth_user.username,commenttime,content from (auth_user join Commentlist on auth_user.id=Commentlist.id) where docnum="+str(docnum)
#     cur.execute(sql)
#     con.close()
#     return JsonResponse(cur.fetchall(),safe=False)


def submit_comment(request):
    con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
    cur=con.cursor()
    cid = request.POST['cid']
    uid=request.POST['uid']
    f_cid = request.POST['f_cid']
    f_uid = request.POST['f_uid']
    f_name = request.POST['f_name']
    docnum=request.POST['docnum']
    content=request.POST['content']
    commenttime = request.POST['commenttime']
    sql="insert into Commentlist values('"+content+"',"+str(docnum)+",'"+ commenttime +"',"+str(cid)+","+str(uid)+","+str(f_cid)+","+str(f_uid)+",'"+f_name+"')"
    cur.execute(sql)
    sql = "select username from auth_user where id=" + str(id)
    cur.execute(sql)
    for row in cur:
        username=row[0]
    sql = "select docname from Table_file where id=" + str(docnum)
    cur.execute(sql)
    for row in cur:
        docname = row[0]
    content=username+" 评论了您的文档: "+docname+" ,去看看吧!"
    sql = "select author_id from Table_file where id=" + str(docnum)
    cur.execute(sql)
    for row in cur:
        author_id = row[0]

    sql="select count(*) from Noticelist"
    cur.execute(sql)
    for row in cur:
        nid=row[0]+1

    sql ="insert into Noticelist values("+str(nid)+","+str(author_id)+",'"+content+"',now(),0,1)"
    cur.execute(sql)
    cur.connection.commit()
    con.close()
    return JsonResponse(1,safe=False)


def get_comments(request):
    con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
    cur=con.cursor()
    docnum=request.POST['docnum']
    sql="select cid,uid,auth_user.username,content,commenttime,f_cid,f_name from (auth_user join Commentlist on auth_user.id=Commentlist.uid) where docnum="+str(docnum)
    cur.execute(sql)
    con.close()
    return JsonResponse(cur.fetchall(),safe=False)


def search_docs(request):
    con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
    cur=con.cursor()
    key=request.POST['key']
    sql="select id,docname,doctitle,docintro from Table_file where docname like '%"+key+"%'"
    cur.execute(sql)
    con.close()
    return JsonResponse(cur.fetchall(),safe=False)


def get_group_docs(request):
    con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
    cur=con.cursor()
    groupnum=request.POST['groupnum']
    sql="select id,docname,lasttime from Table_file where groupnum="+str(groupnum)
    cur.execute(sql)
    con.close()
    return JsonResponse(cur.fetchall(),safe=False)


def match_edit(request):
    con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
    cur=con.cursor()
    id=request.POST['id']
    sql="select isedit from Table_file where id="+str(id)
    cur.execute(sql)
    a=0
    for row in cur:
        a=row[0]
    if a==1: return JsonResponse(0,safe=False)
    else:
        sql="update Table_file set isedit=1 where id="+str(id)
        cur.execute(sql)
        cur.connection.commit()
        con.close()
        return JsonResponse(1,safe=False)


def end_edit(request):
    con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
    cur=con.cursor()
    id=request.POST['id']
    sql="update Table_file set isedit=0 where id="+str(id)
    cur.execute(sql)
    cur.connection.commit()
    con.close()
    return JsonResponse(1,safe=False)


def get_groupnum(request):
    con=pymysql.connect(host="39.97.101.50", port=3306, user="root", password="rjgcxxq", database="xxqdb", charset="utf8")
    cur=con.cursor()
    id=request.POST['id']
    sql="select groupnum from Table_file where id="+str(id)
    cur.execute(sql)
    for row in cur:
        r=row[0]
    con.close()
    return JsonResponse(r,safe=False)