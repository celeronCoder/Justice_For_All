from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
g=''
em=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="akanksha@123A",database='Justice_For_All')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="First_Name":
                fn=value
            if key=="Last_Name":
                ln=value
            if key=="Gender":
                g=value
            if key=="Email":
                em=value
            if key=="Password":
                pwd=value
        
        c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,g,em,pwd)
        cursor.execute(c)
        m.commit()
    

    return render(request,'signup_page.html')