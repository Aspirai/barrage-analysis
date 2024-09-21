from django.shortcuts import render

# Create your views here.
from ai.models import Barrage
from rest_framework import viewsets

from ai.serializer import BarrageSerializer

from django.http import JsonResponse


class BarrageViewSet(viewsets.ModelViewSet):
    queryset = Barrage.objects.all()
    serializer_class = BarrageSerializer

from ai.models import Admin
from ai.serializer import AdminSerializer
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

def detail(request,Barrage_id):
    return HttpResponse("You're looking at barrage %s." %Barrage_id)

def results(request,Barrage_id):
    response = "You're looking at the results of barrage %s."
    return HttpResponse(response % Barrage_id)

# 处理弹幕文本
def test(request):
    # 获取所有弹幕文本
    barrage_texts = Barrage.objects.values_list('content', flat=True)

    # 将文本连接成一个字符串
    text = ' '.join(barrage_texts)

    # 分词
    import jieba
    ls = jieba.lcut(text)
    
    # 去除停用词
    stopwords = [ '[', ']', '的', '是', '在', '了', '和', '有', '我', '你', '他', '她', '它', '我们', '你们', '他们', '她们', '它们', '是', 'Â', '','(',')']#
    word_freq = [word for word in ls if word not in stopwords]
    
    # 统计词频
    from collections import Counter
    # print(word_freq)
    word_freq = Counter(word_freq)

    # 将 Counter 统计结果转换为特定格式的数组
    data = [{'name': word, 'value': freq} for word, freq in word_freq.items()]

    data.sort(key=lambda x: x['value'],reverse=True)

    top64 = data[:100]


    return JsonResponse(top64, safe=False)


def barrage_inquire(request):
    lately_five = Barrage.objects.order_by('-id')[:5]
    front_five = Barrage.objects.all()[:5]

    for record in lately_five:
        record.delete()
    return HttpResponse(lately_five)


def account_management(request,account_id):
    account_inquire = Admin.objects.filter(user_email=account_id)
    account_inquire.delete()
    return HttpResponse(account_inquire)

def barrage_delete(request,id):
    barrage_id = Barrage.objects.filter(id = id)
    barrage_id.delete()
    return HttpResponse(barrage_id)

def barrage_delete_all(request):
    barrage = Barrage.objects.all()
    for record in barrage:
        record.delete()
    return HttpResponse(barrage)

def paging(request,page):
    start_index = (int(page) - 1)*12
    end_index = int(page) *12
    pag = Barrage.objects.all()[start_index:end_index]
    data = []
    for obj in pag:
        data.append({
            'id':obj.id,
            'rood_id':obj.rood_id,
            'name': obj.name,
            'content': obj.content,
            'nature_of_words': obj.nature_of_words
        })
    return JsonResponse(data,safe=False)

def pagSum(request):
    pagSum = Barrage.objects.count()
    return HttpResponse(pagSum)


from ai.models import Room
from ai.serializer import RoomSerializer
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

def room_add(request,room_id):
    room = Room.objects.create(rood_id=room_id)
    return HttpResponse(f'添加房间号{room.rood_id}成功')