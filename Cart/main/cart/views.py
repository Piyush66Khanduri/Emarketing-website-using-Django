from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .sform import slform,verif,medi,buyf,login
import smtplib
from .gene import otpgen
from io import BytesIO
from cart.models import sell,buy
def index(response):
    return render(response,'cart/index.html',{})
def seller(response):
    if response.method=='POST':
        f=slform(response.POST,response.FILES)
        if f.is_valid():
            em=f.cleaned_data['eml']
            nm=str(f.cleaned_data['num'])
            #img=response.FILES.get('imag')
            pno=int(f.cleaned_data['pno'])
            pnum=str(f.cleaned_data['pname'])
            prc=str(f.cleaned_data['prc'])
            cnt=int(f.cleaned_data['cnt'])
            pd=str(f.cleaned_data['Product_description'])
            ver=set_eml(em)
            response.session['otp']=ver
            response.session['num']=nm
            response.session['pno']=pno
            response.session['pnum']=pnum
            response.session['prc']=prc
            response.session['cnt']=cnt
            response.session['pd']=pd
            response.session['eml']=em
            return redirect('/veri/')
        else:
            return HttpResponse("<H1>Some thing went wrong please check your details again.<H1>")
    else:
        f=slform()
        return render(response,'cart/pro.html',{"form":f})
def set_eml(em):
    print("send otp")
    #cetqiwemdeecvriq
    msg=str(otpgen())
    print(msg)
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('piyushkhanduri65@gmail.com','cetqiwemdeecvriq')
    server.sendmail('piyushkhanduri65@gmail.com',em,msg)
    print("Email sent")
    server.quit()
    return msg
def verify(response):
    if response.method=='POST':
        vf=verif(response.POST)
        print('If')
        if vf.is_valid():
            vtp=vf.cleaned_data['value']
            otp=response.session.get('otp')
            if vtp==otp:
                num=response.session.get('num')
                eml=response.session.get('eml')
                pn=response.session.get('pno')
                pnm=response.session.get('pnum')
                prc=response.session.get('prc')
                cn=response.session.get('cnt')
                prd=response.session.get('pd')
                print(num,eml,pn,pnm,prc,cn,prd)
                n=sell(snum=num,mail=eml,pno=pn,pnum=pnm,pr=prc,cnt=cn,pd=prd,_pvt=otp)
                n.save()
                return redirect('/media')
            else:
                f=verif()
                wms="Wrong OTP"
                temp={"form":f,"mess":True}
                return render(response,'cart/otp.html',temp)
        else:
            vf=verif(response)
            print(response.method)
            return render(response,'cart/otp.html',{"form":vf,"mess":False})
    else:
        vf=verif()
        return render(response,'cart/otp.html',{"form":vf,"mess":False})
def med(response):
    if response.method=="POST":
        f=medi(response.POST,response.FILES)
        if f.is_valid():
            imga=f.cleaned_data['imag']
            pt=response.session.get('otp')
            n=sell.objects.get(_pvt=pt)
            n.img=imga
            n.save()
            return HttpResponse("<h1>Image inserted</h1>")
        else:
            return HttpResponse("<H1>Some thing went wrong</H1>")
    else:
        f=medi()
        return render(response,'cart/getimg.html',{'form':f})
def buyer(response):
        if response.method=="POST":
            f=buyf(response.POST)
            if f.is_valid():
                eml=f.cleaned_data['gml']
                eml=set_eml(eml)
                print(eml)
                response.session['nam']=str(f.cleaned_data['bnm'])
                response.session["gml"]=str(f.cleaned_data['gml'])
                response.session["phno"]=int(f.cleaned_data['pn'])
                response.session["dob"]=str(f.cleaned_data['dob'])
                response.session["ttp"]=eml
                return redirect('/bvr/')
        else:
            f=buyf()
            return render(response,"cart/bfm.html",{'form':f})
def bver(response):
    if response.method=="POST":
        f=verif(response.POST)
        if f.is_valid():
            ttp=f.cleaned_data['value']
            if ttp==response.session.get('ttp'):
                bnum=response.session.get('nam')
                mla=response.session.get('gml')
                no=response.session.get('phno')
                db=response.session.get('dob')
                n=buy(bnam=bnum,gm=mla,ph=no,dob=db,_bpt=ttp,avl=True)
                n.save()
                return render(response,'cart/index.html',{})
            else:
                pass
    else:
        f=verif()
        return render(response,'cart/botp.html',{"form":f,"mess":False})
def cust(response):
    if response.method=="POST":
        f=login(response.POST)
        if f.is_valid():
            n=buy.objects.all()
            id1=f.cleaned_data['code']
            for i in n:
                if (i._bpt)==id1:
                    if i.avl==True:
                        return render(response,"cart/index.html",{})
                    else:
                        inf=(mark(i.gm))
                        return render(response,"cart/log.html",{"form":f,"mess":False,"lot":True,"inf":inf})
            return render(response,"cart/log.html",{"form":f,"mess":True,"lot":False})
    else:
         f=login()
         return render(response,"cart/log.html",{"form":f,"mess":False})
def mark(gm):
    mes=str(otpgen())
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login('piyushkhanduri65@gmail.com','cetqiwemdeecvriq')
    server.sendmail('piyushkhanduri65@gmail.com',gm,mes)
    server.quit()
    return mes
def market(response):
    n=sell.objects.all()
    return render(response,"cart/market.html",{"sell":n})