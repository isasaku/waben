from .models import Oder
import datetime
from django.core.mail import send_mail
from django.db.models import Count
from apscheduler.schedulers.background import BackgroundScheduler

today = datetime.date.today()

def mailsend():
    od=Oder.objects.filter(month=today.month,dining="総務").all()
    dy=today.day
    d='day'+str(dy)
    groupby={}
    groupby1={}
    groupby2={}
    groupby3={}
    groupby4={}
    groupby5={}
    groupby6={}
    soumu_grby={}
    grby = od.values(d,'dining').annotate(total=Count(d))
    #grbyはオブジェクト型要素の配列となり、変数を使用できないのでオブジェクト型を用意して入れ替える
    if len(grby)>=1:
        groupby=grby[0]
        soumu_grby[groupby[d]]=groupby['total']
    if len(grby)>=2:
        groupby1=grby[1]
        soumu_grby[groupby1[d]]=groupby1['total']
    if len(grby)>=3:
        groupby2=grby[2]
        soumu_grby[groupby2[d]]=groupby2['total']
    if len(grby)>=4:
        groupby3=grby[3]
        soumu_grby[groupby3[d]]=groupby3['total']
    if len(grby)>=5:
        groupby4=grby[4]
        soumu_grby[groupby4[d]]=groupby4['total']
    if len(grby)>=6:
        groupby5=grby[5]
        soumu_grby[groupby5[d]]=groupby5['total']
    if len(grby)>=7:
        groupby6=grby[6]
        soumu_grby[groupby6[d]]=groupby6['total']
    
    od1=Oder.objects.filter(month=today.month,dining="製造").all()
    dy=today.day
    d='day'+str(dy)
    groupby10={}
    groupby11={}
    groupby12={}
    groupby13={}
    groupby14={}
    groupby15={}
    groupby16={}
    seizou_grby={}
    grby1 = od1.values(d,'dining').annotate(total=Count(d))
    #grbyはオブジェクト型要素の配列となり、変数を使用できないのでオブジェクト型を用意して入れ替える
    if len(grby1)>=1:
        groupby10=grby1[0]
        seizou_grby[groupby10[d]]=groupby10['total']
    if len(grby1)>=2:
        groupby11=grby1[1]
        seizou_grby[groupby11[d]]=groupby11['total']
    if len(grby1)>=3:
        groupby12=grby1[2]
        seizou_grby[groupby12[d]]=groupby12['total']
    if len(grby1)>=4:
        groupby13=grby1[3]
        seizou_grby[groupby13[d]]=groupby13['total']
    if len(grby1)>=5:
        groupby14=grby1[4]
        seizou_grby[groupby14[d]]=groupby14['total']
    if len(grby1)>=6:
        groupby15=grby1[5]
        seizou_grby[groupby15[d]]=groupby15['total']
    if len(grby1)>=7:
        groupby16=grby1[5]
        seizou_grby[groupby16[d]]=groupby16['total']
                
    seizou = ''
    soumu = ''
    od_mn = ''
    header = 'いつもお世話になっております。\n 今日の注文は\n'
    h1 = '　製造\n'
    h2 = '　総務　'
    footer = 'です。\n以上よろしくお願いいたします。\n旭エスケービー株式会社'
    for key,value in seizou_grby.items():
        seizou += ' '
        seizou += key
        seizou += ' '
        seizou += str(value)
        seizou += '\n'
    for key,value in soumu_grby.items():
        seizou += ' '
        soumu += key
        soumu += ' '
        soumu += str(value)
        soumu += '\n'
    od_mn = header+h1+seizou+h2+soumu+footer
    subject = "今日の弁当注文"
    message = od_mn
    from_email = "isasaku4669@gmail.com"
    recipient_list = ["isao@sakuma-elc.com"]
    
    send_mail(subject,message,from_email,recipient_list)

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(mailsend,'interval',days=1,start_date='2021-12-24 09:00:00')
    scheduler.start()
