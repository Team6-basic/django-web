from django.shortcuts import render
import pandas as pd
import numpy as np
from django.core.paginator import Paginator
from django.views import View
from .models import Day_Hate, Time_Hate

# Create your views here.
def index(request):
    # 일별 혐오표현 분석 게시판 구성
    page = request.GET.get('page', 1)
    board_list = Day_Hate.objects.filter(user_id=request.user.id).order_by('-rec_date')
    paginator = Paginator(board_list, 5)
    page_obj = paginator.get_page(page)
    # 일별 혐오표현 평가지표 
    line_lables = []
    indicators = []
    toxic_day = []
    for obj in page_obj:
        data = Time_Hate.objects.filter(rec_datetime__date=obj.rec_date).values_list() # 2~10까지 각각 유형, 11이 clean, 12가 id이다.
        data_df = pd.DataFrame(data)
        indicators.append({ 'id':obj.id, 'toxic':np.mean(data_df[11])})
        line_lables.append(obj.rec_date.strftime('%y-%m-%d'))
        toxic_day.append(np.mean(data_df[11]))

    #월별 혐오표현 통계(파이차트)
    monthly = Time_Hate.objects.all().values_list()
    monthly_df = pd.DataFrame(monthly)
    # 결과 처리
    datasets = [] #파이차트 딕셔너리 형태로 만들기 
    cols = monthly_df.columns[2:11]
    for col in cols:
        vals = monthly_df[col].sum()
        datasets.append({col:vals})

    context = { 'board_list':page_obj,
                'indicator':indicators,
                'monthly_df':datasets,
                'line_lables':line_lables,
                'toxic_day':toxic_day,
                }

    return render(request, 'hopecharm/main.html', context)
    
def detail(request, board_id):
    day_hates = Day_Hate.objects.get(id=board_id)

    board = Time_Hate.objects.filter(rec_day_id=board_id)
    board_df = pd.DataFrame(list(board.values()))
    ### 여기다가 alert 이벤트 넣을거!
    

    ### 여기다가 그래프 요소 넣을거!!

    
    
    return render(request, 'hopecharm/detail.html', {'board':board_df, 'dayhate':day_hates})