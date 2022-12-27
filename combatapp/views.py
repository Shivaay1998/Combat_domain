from django.shortcuts import render
from django.http import HttpResponse
from combatapp.models import Entry
def index(request):
    if request.method == "POST":
        fnm = request.POST["first_name"]
        lnm = request.POST["last_name"]
        pf_img = request.POST["profile_img"]
        em = request.POST["email"]
        cont = request.POST["contact"]
        gen = request.POST["gender"]
        dy = request.POST["day"]
        mon = request.POST["month"]
        yer = request.POST["year"]
        cit = request.POST["city"]
        cntry = request.POST["country"]
        docs = request.POST["documents"]
        passw = request.POST["Passwords"]

        
        data= Entry(first_name=fnm, last_name=lnm,profile_img=pf_img, email=em, contact=cont, gender = gen , day=dy, month=mon, year=yer, city=cit, country=cntry,
        documents=docs, passwords=passw)
        data.save()
        return HttpResponse("<h1 style='color:green;'>Data Saved Successfully!</h1>")
    return render(request, "index.html")
