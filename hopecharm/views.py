# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Day_Hate, Time_Hate

# Create your views here.
def index(request):
    page = request.GET.get('page', 1)
    board_list = Day_Hate.objects.order_by('-rec_date')
    paginator = Paginator(board_list, 6)
    page_obj = paginator.get_page(page)
    context = {'board_list':page_obj}
    # return HttpResponse("bbsnote에 오신 것을 환영합니다!");
    return render(request, 'hopecharm/main.html', context)

def detail(request, board_id):
    board = Time_Hate.objects.get(id=board_id)
    context = {'board':board}
    return render(request, 'hopecharm/main.html', context)

# today_min = datetime.combine(timezone.now().date(), datetime.today().time().min)
# today_max = datetime.combine(timezone.now().date(), datetime.today().time().max)
# objetcs_for_today = MyModel.objects.filter(date__range=(today_min, today_max))