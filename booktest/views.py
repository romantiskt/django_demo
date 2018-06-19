from django.shortcuts import render

# Create your views here.
from booktest.models import BookInfo


def index(request):
    bookList = BookInfo.objects.all()
    context = {'list': bookList}
    return render(request, 'booktest/index.html', context)

def detail(request,id):
    bookinfo = BookInfo.objects.get(pk=id)
    return render(request, 'booktest/detail.html', {'book': bookinfo})

def getTest(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    data={'a':a,'b':b,'c':c}
    return render(request, 'booktest/getTest.html',data)


def postTest(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname': uname, 'upwd': upwd, 'ugender': ugender, 'uhobby': uhobby}
    return render(request, 'booktest/postTest.html',context)