from django.shortcuts import render, redirect
from app01 import models

# Create your views here.


def index(request):
    if request.method == "POST":
        admission = request.POST.get("admission")
        print(admission, 'admission')
        obj = models.UserInfo.objects.filter(admission=admission).first()
        print(obj)
        if obj:
            info_list = [
                    obj.username,
                    obj.admission,
                    obj.code,
                    obj.type,
                    obj.one,
                    obj.two,
                    obj.three,
                    obj.four,
                         ]
            print(info_list)

            return render(request, 'info_list.html', {'info_list': info_list})

    return render(request, 'index.html')


def info_list(request):
    # info_list = request.POST.get('info_list')
    print(info_list)
    return render(request, 'info_list.html')

#     if request.method == "POST":
#         obj = request.POST.get('obj')
#         print(obj)
#     # info = models.UserInfo.objects.all().values("username", "admission","code","type","one","two","three","four").first()
#         info = models.UserInfo.objects.all()

        # dict_info = {}
        # for k,v in info.items():
        #     dict_info[models.UserInfo._meta.get_field(k).verbose_name] = v
    #     info_list = [
    #         info.get("username"),
    #         info.get("admission"),
    #         info.get("code"),
    #         info.get("type"),
    #         info.get("one"),
    #         info.get("two"),
    #         info.get("three"),
    #         info.get("four"),
    #     ]
    #
    #     print(info)
    #     print(info_list,'info_list')
    #     return render(request,'info_list.html',{'info_list': info_list})
    # return redirect('/index/')