
from django.shortcuts import *
from django.http import JsonResponse
import csv
import pandas
from django.views.decorators.csrf import csrf_exempt
def home(request):
    return render(request, 'home.html')
def index(request):
    rd=open("Emissions.csv","r")
    x = []
    while True:
        line=rd.readline()
        if line=="":
            break
        data=line.split(",")
        d = []
        d.append(data[0])
        d.append(data[1])
        d.append(data[2])
        d.append(data[3])
        d.append(data[4])
        d.append(data[5])
        d.append(data[6])
        d.append(data[7])
        d.append(data[6])
        d.append(data[9])
        d.append(data[10])
        d.append(data[11])
        d.append(data[12])
        d.append(data[13])
        d.append(data[14])
        x.append(d)
    return JsonResponse(x,safe=False)
@csrf_exempt
def add(request):
    id=request.POST['textbox1']
    name=request.POST['textbox2']
    sal=request.POST['textbox3']
    des=request.POST['textbox4']
    mob=request.POST['textbox5']
    gen=request.POST['textbox6']
    x=[]
    x.append(id)

    x.append(name)

    x.append(sal)

    x.append(des)

    x.append(mob)

    x.append(gen)

    wr = open("Emissions.csv","a",newline='')
    obj=csv.writer(wr)
    obj.writerow(x)
    return HttpResponse("success")
def viewfiltercountry(request):

    value=request.GET['value']
    x = []
    if(value!=''):
        rd = open("Emissions.csv", "r")

        while True:
            line = rd.readline()
            if line == "":
                break
            data = line.split(",")
            d = []
            if (value in data[0]):
                d.append(data[0])
                d.append(data[1])
                d.append(data[2])
                d.append(data[3])
                d.append(data[4])
                d.append(data[5])
                d.append(data[6])
                d.append(data[7])
                d.append(data[6])
                d.append(data[9])
                d.append(data[10])
                d.append(data[11])
                d.append(data[12])
                d.append(data[13])
                d.append(data[14])
                x.append(d)
                print(x)
    else:
        d = []
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        d.append("--")
        x.append(d)
        print(x)
    return JsonResponse(x,safe=False)
def minimum(request):
    Minimum = []
    for i in range(1, 15):
        rd = open("Emissions.csv", "r")
        x = []
        b = []
        c = []
        while True:
            line = rd.readline()
            if line == "":
                break
            data = line.split(",")
            d = []
            d.append(data[i])
            x.append(d)
        a = min(x)
        rd2 = open("Emissions.csv", "r")
        while True:
            line1 = rd2.readline()
            if line1 == "":
                break
            data1 = line1.split(",")

            if (a[0] == data1[i]):
                b.append(data1[0])
                b.append(1996 + i)
                b.append(data1[i])
                c.append(b)
        Minimum.append(b)
    return JsonResponse(Minimum,safe=False)
def maximum(request):
    Maximum = []
    for i in range(1, 15):
        rd = open("Emissions.csv", "r")
        x = []
        b = []
        c = []
        while True:
            line = rd.readline()
            if line == "":
                break
            data = line.split(",")
            d = []
            d.append(data[i])
            x.append(d)
        # print(x)
        # g=max(x)
        # print("g-->",g)
        a = x[1]
        # print(a[0])
        for j in range(1, len(x)):
            n = x[j]
            if float(a[0]) < float(n[0]):
                a = n

        rd2 = open("Emissions.csv", "r")
        while True:
            line1 = rd2.readline()
            if line1 == "":
                break
            data1 = line1.split(",")
            if (a[0] == data1[i]):
                b.append(data1[0])
                b.append(1996 + i)
                b.append(data1[i])
                c.append(b)
        Maximum.append(b)
    return JsonResponse(Maximum,safe=False)
@csrf_exempt
def graph(request):
    import matplotlib.pyplot as plt
    import base64
    import urllib
    import io
    print("hello")
    value=[]
    value.append(request.GET['namegraph'])
    print(value)
    df = pandas.read_csv("Emissions.csv")
    x = ["1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"]
    ans = df["CO2 per capita"] == "India"
    plt.bar(x, df[x].iloc[82])
    fig = plt.gcf()
    # convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    print(uri)
    return JsonResponse({'data': uri}, safe=False)