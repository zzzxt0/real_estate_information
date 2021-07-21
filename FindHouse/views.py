from django.shortcuts import render
from . import models
# Create your views here.
def ToAddHouse(request):
    return render(request, 'AddHouse.html')

# 注册

def AddHouse(request):
    if request.method == "GET":
        userName = request.GET.get("username")
        print("*********111")
        if request.method == "POST":
            title = request.POST.get('title', None)
            houseType = request.POST.get('houseType', None)
            minPrice = request.POST.get('minPrice', None)
            maxPrice = request.POST.get('maxPrice', None)
            minSize = request.POST.get('minSize', None)
            maxSize = request.POST.get('maxSize', None)
            Elevator = request.POST.get('Elevator', None)
            renovation = request.POST.get('renovation', None)
            typeOfMes = request.POST.get('typeOfMes', None)
            userRealName = request.POST.get('userRealName', None)
            userTel = request.POST.get('userTel', None)
            userEmail = request.POST.get('userEmail', None)
            other = request.POST.get('other', None)
            # 空判断，留着待写
            print(userTel)
            record = models.FindHouseInfo.objects.create(title=title,
                                                houseType=houseType,
                                                minPrice=minPrice,
                                                maxPrice=maxPrice,
                                                minSize=minSize,
                                                maxSize=maxSize,
                                                Elevator=Elevator,
                                                renovation=renovation,
                                                typeOfMes=typeOfMes,
                                                userRealName=userRealName,
                                                userTel=userTel,
                                                userEmail=userEmail,
                                                other=other,
                                                userName = userName
                                                )
            print("***")
            message = "求租/购信息上传成功！"
            return render(request, 'AddHouse.html', {"message": message, "username":userName})
        return render(request, 'AddHouse.html',{"username":userName})
    return render(request, 'AddHouse.html')