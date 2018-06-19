from django.shortcuts import render

# Create your views here.
from df_goods.models import TypeInfo


def index(request):
    typeInfoList=TypeInfo.objects.all();
    context={'title':'首页','typelist':typeInfoList}
    return render(request,'df_goods/index.html',context)