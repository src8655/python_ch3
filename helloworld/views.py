from django.db.models import Max, F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from helloworld.models import Counter


def hello(request):
    return render(request, 'helloworld/hello.html')


def hello2(request, id=0):
    return HttpResponse('id:{0}'.format(id))


def hello3(request):
    jsonresult = {
        'result': 'success',
        'data': ['hello', 1, 2, True, ('a', 'b', 'c')]
    }

    return JsonResponse(jsonresult)


def counter_add(request):
    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 1
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 2
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 3
    c.save()

    return HttpResponse('ok')


def counter_max(request):
    value = Counter.objects.aggregate(max_groupno=Max('groupno'))
    max_groupno = 0 if value['max_groupno'] is None else value['max_groupno']
    return HttpResponse('max groupno:{0}'.format(max_groupno))


def counter_update(request):
    # groupno = 1 이고
    # orderno >= 2 의 게시물의
    # orderno를 1씩 증가
    # __gt, __lt, __gte, __lte
    Counter.objects.filter(groupno=1).filter(orderno__gte=2).update(orderno=F('orderno')+1)
    # for c in result:  # 이렇게 하지 말아라(주석)
    #     c.orderno = c.order + 1
    #     c.save()

    return HttpResponse('ok')
