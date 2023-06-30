from django.shortcuts import render
import pandas as pd
import numpy as np
from django.core.paginator import Paginator
from django.views import View
from .models import Day_Hate, Time_Hate
import datetime as dt

# plotly 관련
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Create your views here.
def index(request):
    # 일별 혐오표현 분석 게시판 구성
    page = request.GET.get("page", 1)
    board_list = Day_Hate.objects.filter(user_id=request.user.id).order_by("-rec_date")
    paginator = Paginator(board_list, 5)
    page_obj = paginator.get_page(page)
    # 일별 혐오표현 평가지표
    indicators = []
    for obj in page_obj:
        data = Time_Hate.objects.filter(
            rec_datetime__date=obj.rec_date  # obj.rec_date는 Day_Hate의 rec_date
        ).values_list()  # 2~10까지 각각 유형, 11이 clean, 12가 id이다.
        data_df = pd.DataFrame(data)
        indicators.append({"id": obj.id, "toxic": np.mean(data_df[11])})

    # 월별 혐오표현 통계(파이차트)
    monthly = Time_Hate.objects.all().values_list()
    monthly_df = pd.DataFrame(monthly)
    # 결과 처리
    datasets = []  # 딕셔너리 형태로 만들기
    cols = monthly_df.columns[2:11]
    for col in cols:
        vals = monthly_df[col].sum()
        datasets.append({col: vals})

    context = {
        "board_list": page_obj,
        "indicator": indicators,
        "monthly_df": datasets,
    }

    return render(request, "hopecharm/main.html", context)


def detail(request, board_id):
    user_data = Day_Hate.objects.filter(id=board_id).values('rec_date').get()
    # 아래 board_df가 일별 총 DB테이블
    board = Time_Hate.objects.filter(rec_datetime__date=user_data['rec_date'].isoformat()).values_list()
    board_df = pd.DataFrame(board)
    # 레이블용 Datetime 데이터!
    time_labels = board_df[1]
    ### 여기다가 alert 이벤트 넣을거!

    ### 여기다가 그래프 요소 넣을거!!
    # 일벌 혐오표현 통계(파이차트) : 클린포함
    # 결과 처리
    datasets = []  # 딕셔너리 형태로 만들기
    cols = board_df.columns[2:12]
    for col in cols:
        vals = board_df[col].sum()
        datasets.append({col: vals})

    # 월별 혐오표현 통계(라인차트) : 클린 제외
    # 시계열그래프 그리기
    fig = go.Figure()
    board_df[1] = pd.to_datetime(board_df[1]).dt.tz_localize(None)

    fig.add_trace(
        go.Scatter(  # 라인 그래프 그리기
            x=board_df[1],
            y=board_df['fg_woman_or_family'],
            name="여성/가족",
            mode="lines",  # 라인으로 표현
            # line=dict(color="#33CFA5") # 선색상 지정
        )
    )

    fig.add_trace(
        go.Scatter(  # 라인 그래프 그리기
            x=board_df[1],
            y=board_df['fg_man'],
            name="남성",
            mode="lines",  # 라인으로 표현
        )
    )
    fig.add_trace(
        go.Scatter(  # 라인 그래프 그리기
            x=board_df[1],
            y=board_df['fg_sexual_minority'],
            name="성소수자",
            mode="lines",  # 라인으로 표현
        )
    )
    fig.add_trace(
        go.Scatter(  # 라인 그래프 그리기
            x=board_df[1],
            y=board_df['fg_race_or_nationality'],
            name="인종/국적",
            mode="lines",  # 라인으로 표현
        )
    )
    fig.add_trace(
        go.Scatter(  # 라인 그래프 그리기
            x=board_df[1],
            y=board_df['fg_age'],
            name="연령",
            mode="lines",  # 라인으로 표현
        )
    )
    fig.add_trace(
        go.Scatter(  # 라인 그래프 그리기
            x=board_df[1],
            y=board_df['fg_region'],
            name="지역",
            mode="lines",  # 라인으로 표현
        )
    )
    fig.add_trace(
        go.Scatter(  # 라인 그래프 그리기
            x=board_df[1],
            y=board_df['fg_religion'],
            name="종교",
            mode="lines",  # 라인으로 표현
        )
    )
    fig.add_trace(
        go.Scatter(  # 라인 그래프 그리기
            x=board_df[1],
            y=board_df['fg_other_hate'],
            name="기타혐오",
            mode="lines",  # 라인으로 표현
        )
    )
    fig.add_trace(
        go.Scatter(  # 라인 그래프 그리기
            x=board_df[1],
            y=board_df['fg_normal_bad_comments'],
            name="악플/욕설",
            mode="lines",  # 라인으로 표현
        )
    )

    fig.update_layout(
        {
            "title": {
                "text": "<b>혐오표현 시계열그래프</b>",
                "x": 0.5,  # x축 위치
                "y": 0.9,
                "font": {"size": 30},
            },
            "showlegend": True,  # 범례표시
            "xaxis": {
                "title": "date",  # x축 타이틀 이름
                "showticklabels": True,  # x축 간격 표시
                #'dtick' : 'M1' # x축 간격 범위
            },
            "yaxis": {"title": "빈도"},
            "template": "plotly_white",  # 배경 설정
        }
    )

    # HTML 파일로 변환
    fig_timeline_html = fig.to_html()
    # alert용 수치 높은 행만 추출하기!

    return render(
        request,
        "hopecharm/detail.html",
        {
            "board": board_df,
            "title": user_data,
            "daily_list_pie": datasets,
            "fig_timeline_html": fig_timeline_html,
            "time_labels": time_labels,
        },
    )
