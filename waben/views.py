from django.shortcuts import render,redirect
from django.views.generic import View
from django.views.generic.list import ListView
from .forms import SignUpForm,OderForm
from .models import Oder
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
import datetime
from django.contrib.auth.models import User
import calendar
from django.db.models import Count
from django.core.mail import send_mail

today = datetime.date.today()

class IndexView(View):

    def get(self,request, *args, **kwargs):
        form = OderForm()
        context = {}
        context['form'] = form
        nm = request.user
        mn = today.month
        if Oder.objects.filter(
            name=nm,
            month=mn,
            ).exists():
            return redirect('check')
        else:
            return render(request, 'registration/index.html', context)

    def post(self, request, *args, **kwargs):
        if request.POST.get('dining') != None:        
            din = request.POST.get('dining')        
        if request.POST.get('day1') != None:        
            d1 = request.POST.get('day1')
        else:
            d1 = '休み'
        if request.POST.get('day2') != None:        
            d2 = request.POST.get('day2')
        else:
            d2 = '休み'        
        if request.POST.get('day3') != None:        
            d3 = request.POST.get('day3')
        else:
            d3 = '休み'
        if request.POST.get('day4') != None:        
            d4 = request.POST.get('day4')
        else:
            d4 = '休み'
        if request.POST.get('day5') != None:        
            d5 = request.POST.get('day5')
        else:
            d5 = '休み'
        if request.POST.get('day6') != None:        
            d6 = request.POST.get('day6')
        else:
            d6 = '休み'
        if request.POST.get('day7') != None:        
            d7 = request.POST.get('day7')
        else:
            d7 = '休み'
        if request.POST.get('day8') != None:        
            d8 = request.POST.get('day8')
        else:
            d8 = '休み'
        if request.POST.get('day9') != None:       
            d9 = request.POST.get('day9')
        else:
            d9 = '休み'
        if request.POST.get('day10') != None:        
            d10 = request.POST.get('day10')
        else:
            d10 = '休み'
        if request.POST.get('day11') != None:        
            d11 = request.POST.get('day11')
        else:
            d11 = '休み'
        if request.POST.get('day12') != None:        
            d12 = request.POST.get('day12')
        else:
            d12 = '休み'
        if request.POST.get('day14') != None:        
            d13 = request.POST.get('day13')
        else:
            d13 = '休み'
        if request.POST.get('day14') != None:        
            d14 = request.POST.get('day14')
        else:
            d14 = '休み'
        if request.POST.get('day15') != None:        
            d15 = request.POST.get('day15')
        else:
            d15 = '休み'
        if request.POST.get('day16') != None:        
            d16 = request.POST.get('day16')
        else:
            d16 = '休み'
        if request.POST.get('day17') != None:        
            d17 = request.POST.get('day17')
        else:
            d17 = '休み'
        if request.POST.get('day18') != None:        
            d18 = request.POST.get('day18')
        else:
            d18 = '休み'
        if request.POST.get('day19') != None:        
            d19 = request.POST.get('day19')
        else:
            d19 = '休み'
        if request.POST.get('day20') != None:        
            d20 = request.POST.get('day20')
        else:
            d20 = '休み'
        if request.POST.get('day21') != None:
            d21 = request.POST.get('day21')
        else:
            d21 = '休み'
        if request.POST.get('day22') != None:
            d22 = request.POST.get('day22')
        else:
            d22 = '休み'
        if request.POST.get('day23') != None:
            d23 = request.POST.get('day23')
        else:
            d23 = '休み'
        if request.POST.get('day24') != None:
            d24 = request.POST.get('day24')
        else:
            d24 = '休み'
        if request.POST.get('day25') != None:
            d25 = request.POST.get('day25')
        else:
            d25 = '休み'
        if request.POST.get('day26') != None:
            d26 = request.POST.get('day26')
        else:
            d26 = '休み'
        if request.POST.get('day27') != None:
            d27 = request.POST.get('day27')
        else:
            d27 = '休み'
        if request.POST.get('day28') != None:
            d28 = request.POST.get('day28')
        else:
            d28 = '休み'
        if request.POST.get('day29') != None:
            d29 = request.POST.get('day29')
        else:
            d29 = '休み'
        if request.POST.get('day30') != None:
            d30 = request.POST.get('day30')
        else:
            d30 = '休み'
        if request.POST.get('day31') != None:
            d31 = request.POST.get('day31')
        else:
            d31 = '休み'
        nm = request.user
        un = request.user.username
        mn = today.month
        if Oder.objects.filter(
            name=nm,
            month=mn,
            ).exists():
            od = Oder.objects.get(name=nm,month=mn)
            od.dining = din        
            od.day1 = d1
            od.day2 = d2
            od.day3 = d3
            od.day4 = d4
            od.day5 = d5
            od.day6 = d6
            od.day7 = d7
            od.day8 = d8
            od.day9 = d9
            od.day10 = d10
            od.day11 = d11
            od.day12 = d12
            od.day13 = d13
            od.day14 = d14
            od.day15 = d15
            od.day16 = d16
            od.day17 = d17
            od.day18 = d18
            od.day19 = d19
            od.day20 = d20
            od.day21 = d21
            od.day22 = d22
            od.day23 = d23
            od.day24 = d24
            od.day25 = d25
            od.day26 = d26
            od.day27 = d27
            od.day28 = d28
            od.day29 = d29
            od.day30 = d30
            od.day31 = d31
            od.month = mn
            od.save()        
            print(str(od))
        else:
            Oder.objects.create(
                dining = din,        
                name=nm,
                username=un,
                month=mn,
                day1=d1,
                day2=d2,
                day3=d3,
                day4=d4,
                day5=d5,
                day6=d6,
                day7=d7,
                day8=d8,
                day9=d9,
                day10=d10,
                day11=d11,
                day12=d12,
                day13=d13,
                day14=d14,
                day15=d15,
                day16=d16,
                day17=d17,
                day18=d18,
                day19=d19,
                day20=d20,
                day21=d21,
                day22=d22,
                day23=d23,
                day24=d24,
                day25=d25,
                day26=d26,
                day27=d27,
                day28=d28,
                day29=d29,
                day30=d30,
                day31=d31,
            )        
        return redirect('check')
               
class NextView(CreateView):
    form_class = OderForm
    template_name = "registration/index2.html"
    model = Oder
    success_url = reverse_lazy('check2')

    def get(self,request, *args, **kwargs):
        form = OderForm()
        context = {}
        context['form'] = form
        if today.month!=12:
            mn=today.month+1
        else:
            mn=1
        nm = request.user
        if Oder.objects.filter(
            name=nm,
            month=mn,
            ).exists():
            return redirect('check2')
        else:
            return render(request, 'registration/index2.html', context)

    def post(self, request, *args, **kwargs):
        
        if request.POST.get('day1') != None:        
            d1 = request.POST.get('day1')
        else:
            d1 = '休み'
        if request.POST.get('day2') != None:        
            d2 = request.POST.get('day2')
        else:
            d2 = '休み'        
        if request.POST.get('day3') != None:        
            d3 = request.POST.get('day3')
        else:
            d3 = '休み'
        if request.POST.get('day4') != None:        
            d4 = request.POST.get('day4')
        else:
            d4 = '休み'
        if request.POST.get('day5') != None:        
            d5 = request.POST.get('day5')
        else:
            d5 = '休み'
        if request.POST.get('day6') != None:        
            d6 = request.POST.get('day6')
        else:
            d6 = '休み'
        if request.POST.get('day7') != None:        
            d7 = request.POST.get('day7')
        else:
            d7 = '休み'
        if request.POST.get('day8') != None:        
            d8 = request.POST.get('day8')
        else:
            d8 = '休み'
        if request.POST.get('day9') != None:       
            d9 = request.POST.get('day9')
        else:
            d9 = '休み'
        if request.POST.get('day10') != None:        
            d10 = request.POST.get('day10')
        else:
            d10 = '休み'
        if request.POST.get('day11') != None:        
            d11 = request.POST.get('day11')
        else:
            d11 = '休み'
        if request.POST.get('day12') != None:        
            d12 = request.POST.get('day12')
        else:
            d12 = '休み'
        if request.POST.get('day14') != None:        
            d13 = request.POST.get('day13')
        else:
            d13 = '休み'
        if request.POST.get('day14') != None:        
            d14 = request.POST.get('day14')
        else:
            d14 = '休み'
        if request.POST.get('day15') != None:        
            d15 = request.POST.get('day15')
        else:
            d15 = '休み'
        if request.POST.get('day16') != None:        
            d16 = request.POST.get('day16')
        else:
            d16 = '休み'
        if request.POST.get('day17') != None:        
            d17 = request.POST.get('day17')
        else:
            d17 = '休み'
        if request.POST.get('day18') != None:        
            d18 = request.POST.get('day18')
        else:
            d18 = '休み'
        if request.POST.get('day19') != None:        
            d19 = request.POST.get('day19')
        else:
            d19 = '休み'
        if request.POST.get('day20') != None:        
            d20 = request.POST.get('day20')
        else:
            d20 = '休み'
        if request.POST.get('day21') != None:
            d21 = request.POST.get('day21')
        else:
            d21 = '休み'
        if request.POST.get('day22') != None:
            d22 = request.POST.get('day22')
        else:
            d22 = '休み'
        if request.POST.get('day23') != None:
            d23 = request.POST.get('day23')
        else:
            d23 = '休み'
        if request.POST.get('day24') != None:
            d24 = request.POST.get('day24')
        else:
            d24 = '休み'
        if request.POST.get('day25') != None:
            d25 = request.POST.get('day25')
        else:
            d25 = '休み'
        if request.POST.get('day26') != None:
            d26 = request.POST.get('day26')
        else:
            d26 = '休み'
        if request.POST.get('day27') != None:
            d27 = request.POST.get('day27')
        else:
            d27 = '休み'
        if request.POST.get('day28') != None:
            d28 = request.POST.get('day28')
        else:
            d28 = '休み'
        if request.POST.get('day29') != None:
            d29 = request.POST.get('day29')
        else:
            d29 = '休み'
        if request.POST.get('day30') != None:
            d30 = request.POST.get('day30')
        else:
            d30 = '休み'
        if request.POST.get('day31') != None:
            d31 = request.POST.get('day31')
        else:
            d31 = '休み'
        nm = request.user
        un = request.user.username
        if today.month!=12:
            mn=today.month+1
        else:
            mn=1
        if Oder.objects.filter(
            name=nm,
            month=mn,
            ).exists():
            od = Oder.objects.get(name=nm,month=mn)
            od.day1 = d1
            od.day2 = d2
            od.day3 = d3
            od.day4 = d4
            od.day5 = d5
            od.day6 = d6
            od.day7 = d7
            od.day8 = d8
            od.day9 = d9
            od.day10 = d10
            od.day11 = d11
            od.day12 = d12
            od.day13 = d13
            od.day14 = d14
            od.day15 = d15
            od.day16 = d16
            od.day17 = d17
            od.day18 = d18
            od.day19 = d19
            od.day20 = d20
            od.day21 = d21
            od.day22 = d22
            od.day23 = d23
            od.day24 = d24
            od.day25 = d25
            od.day26 = d26
            od.day27 = d27
            od.day28 = d28
            od.day29 = d29
            od.day30 = d30
            od.day31 = d31
            od.month = mn
            od.save()        
            print(str(od))
        else:
            Oder.objects.create(
                name=nm,
                username=un,
                month=mn,
                day1=d1,
                day2=d2,
                day3=d3,
                day4=d4,
                day5=d5,
                day6=d6,
                day7=d7,
                day8=d8,
                day9=d9,
                day10=d10,
                day11=d11,
                day12=d12,
                day13=d13,
                day14=d14,
                day15=d15,
                day16=d16,
                day17=d17,
                day18=d18,
                day19=d19,
                day20=d20,
                day21=d21,
                day22=d22,
                day23=d23,
                day24=d24,
                day25=d25,
                day26=d26,
                day27=d27,
                day28=d28,
                day29=d29,
                day30=d30,
                day31=d31,
            )
        return redirect('check2')

class SignUpView(CreateView):
    model = Oder
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def signup(request):
        if request.method=='POST':
            form=SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form=SignUpForm()

class CheckView(ListView):
    template_name = 'registration/check.html'
    model = Oder
    def get_queryset(self):
        return Oder.objects.filter(name=self.request.user,month=today.month).all()

    def get_context_data(self, **kwargs):
        year = today.year
        month = today.month
        mon_con = calendar.monthrange(year,month)[1]
        youbi = {}
        for i in range(1,mon_con+1):
            day = i
            dt = datetime.datetime(year,month,day)        
            youb = {0:'(月)',1:'(火)',2:'(水)',3:'(木)',4:'(金)',5:'(土)',6:'(日)'}
            yobNo = dt.weekday()                      
            youbi[i] = youb[yobNo]
        context = super().get_context_data(**kwargs)
        context['youbi'] = youbi
        return context

class Check2View(ListView):
    template_name = 'registration/check2.html'
    model = Oder
    def get_queryset(self):
        return Oder.objects.filter(name=self.request.user,month=today.month+1).all()

    def get_context_data(self, **kwargs):
        year = today.year
        if today.month!=12:
            month=today.month+1
        else:
            month=1
        mon_con = calendar.monthrange(year,month)[1]
        youbi = {}
        for i in range(1,mon_con+1):
            day = i
            dt = datetime.datetime(year,month,day)        
            youb = {0:'(月)',1:'(火)',2:'(水)',3:'(木)',4:'(金)',5:'(土)',6:'(日)'}
            yobNo = dt.weekday()
            youbi[i] = youb[yobNo]
        context = super().get_context_data(**kwargs)
        context['youbi'] = youbi
        return context

class FixView(CreateView,ListView):
    form_class = OderForm
    template_name = "registration/fix.html"
    model = Oder
    success_url = reverse_lazy('check')

    def get_queryset(self):
        return Oder.objects.filter(name=self.request.user,month=today.month).all()

    def get_context_data(self, **kwargs):
        year = today.year
        month = today.month
        mon_con = calendar.monthrange(year,month)[1]
        youbi = {}
        for i in range(1,mon_con+1):
            day = i
            dt = datetime.datetime(year,month,day)        
            youb = {0:'(月)',1:'(火)',2:'(水)',3:'(木)',4:'(金)',5:'(土)',6:'(日)'}
            yobNo = dt.weekday()
            youbi[i] = youb[yobNo]
        context = super().get_context_data(**kwargs)
        context['youbi'] = youbi
        return context    

    def post(self, request, *args, **kwargs):
        nm = request.user
        mn = today.month
        od = Oder.objects.get(name=nm,month=mn)        
        if request.POST.get('day1') != None:        
            d1 = request.POST.get('day1')
            od.day1 = d1
        if request.POST.get('day2') != None:        
            d2 = request.POST.get('day2')
            od.day2 = d2
        if request.POST.get('day3') != None:        
            d3 = request.POST.get('day3')
            od.day3 = d3
        if request.POST.get('day4') != None:        
            d4 = request.POST.get('day4')
            od.day4 = d4
        if request.POST.get('day5') != None:        
            d5 = request.POST.get('day5')
            od.day5 = d5
        if request.POST.get('day6') != None:        
            d6 = request.POST.get('day6')
            od.day6 = d6
        if request.POST.get('day7') != None:        
            d7 = request.POST.get('day7')
            od.day7 = d7
        if request.POST.get('day8') != None:        
            d8 = request.POST.get('day8')
            od.day8 = d8
        if request.POST.get('day9') != None:        
            d9 = request.POST.get('day9')
            od.day9 = d9
        if request.POST.get('day10') != None:        
            d10 = request.POST.get('day10')
            od.day10 = d10
        if request.POST.get('day11') != None:        
            d11 = request.POST.get('day11')
            od.day11 = d11
        if request.POST.get('day12') != None:        
            d12 = request.POST.get('day12')
            od.day12 = d12
        if request.POST.get('day13') != None:        
            d13 = request.POST.get('day13')
            od.day13 = d13
        if request.POST.get('day14') != None:        
            d14 = request.POST.get('day14')
            od.day14 = d14
        if request.POST.get('day15') != None:        
            d15 = request.POST.get('day15')
            od.day15 = d15
        if request.POST.get('day16') != None:        
            d16 = request.POST.get('day16')
            od.day16 = d16
        if request.POST.get('day17') != None:        
            d17 = request.POST.get('day17')
            od.day17 = d17
        if request.POST.get('day18') != None:        
            d18 = request.POST.get('day18')
            od.day18 = d18
        if request.POST.get('day19') != None:        
            d19 = request.POST.get('day19')
            od.day19 = d19
        if request.POST.get('day20') != None:        
            d20 = request.POST.get('day20')
            od.day20 = d20
        if request.POST.get('day21') != None:        
            d21 = request.POST.get('day21')
            od.day21 = d21
        if request.POST.get('day22') != None:        
            d22 = request.POST.get('day22')
            od.day22 = d22
        if request.POST.get('day23') != None:        
            d23 = request.POST.get('day23')
            od.day23 = d23
        if request.POST.get('day24') != None:        
            d24 = request.POST.get('day24')
            od.day24 = d24
        if request.POST.get('day25') != None:        
            d25 = request.POST.get('day25')
            od.day25 = d25
        if request.POST.get('day26') != None:        
            d26 = request.POST.get('day26')
            od.day26 = d26
        if request.POST.get('day27') != None:        
            d27 = request.POST.get('day27')
            od.day27 = d27
        if request.POST.get('day28') != None:        
            d28 = request.POST.get('day28')
            od.day28 = d28
        if request.POST.get('day29') != None:        
            d29 = request.POST.get('day29')
            od.day29 = d29
        if request.POST.get('day30') != None:        
            d30 = request.POST.get('day30')
            od.day30 = d30
        if request.POST.get('day31') != None:        
            d31 = request.POST.get('day31')
            od.day31 = d31               
        od.save()        
        return redirect('check')

class Fix2View(CreateView,ListView):
    form_class = OderForm
    template_name = "registration/fix2.html"
    model = Oder
    success_url = reverse_lazy('check2')
    
    def get_queryset(self):
        if today.month!=12:
            month=today.month+1
        else:
            month=1
        return Oder.objects.filter(name=self.request.user,month=month).all()

    def get_context_data(self, **kwargs):
        if today.month!=12:
            year = today.year+1
        else:
            year = today.year+1
        if today.month!=12:
            month=today.month+1
        else:
            month=1
        mon_con = calendar.monthrange(year,month)[1]
        youbi = {}
        for i in range(1,mon_con+1):
            day = i
            dt = datetime.datetime(year,month,day)        
            youb = {0:'(月)',1:'(火)',2:'(水)',3:'(木)',4:'(金)',5:'(土)',6:'(日)'}
            yobNo = dt.weekday()
            youbi[i] = youb[yobNo]
        context = super().get_context_data(**kwargs)
        context['youbi'] = youbi
        return context    

    def post(self, request, *args, **kwargs):
        nm = request.user
        if today.month!=12:
            mn=today.month+1
        else:
            mn=1
        od = Oder.objects.get(name=nm,month=mn)        
        if request.POST.get('day1') != None:        
            d1 = request.POST.get('day1')
            od.day1 = d1
        if request.POST.get('day2') != None:        
            d2 = request.POST.get('day2')
            od.day2 = d2
        if request.POST.get('day3') != None:        
            d3 = request.POST.get('day3')
            od.day3 = d3
        if request.POST.get('day4') != None:        
            d4 = request.POST.get('day4')
            od.day4 = d4
        if request.POST.get('day5') != None:        
            d5 = request.POST.get('day5')
            od.day5 = d5
        if request.POST.get('day6') != None:        
            d6 = request.POST.get('day6')
            od.day6 = d6
        if request.POST.get('day7') != None:        
            d7 = request.POST.get('day7')
            od.day7 = d7
        if request.POST.get('day8') != None:        
            d8 = request.POST.get('day8')
            od.day8 = d8
        if request.POST.get('day9') != None:        
            d9 = request.POST.get('day9')
            od.day9 = d9
        if request.POST.get('day10') != None:        
            d10 = request.POST.get('day10')
            od.day10 = d10
        if request.POST.get('day11') != None:        
            d11 = request.POST.get('day11')
            od.day11 = d11
        if request.POST.get('day12') != None:        
            d12 = request.POST.get('day12')
            od.day12 = d12
        if request.POST.get('day13') != None:        
            d13 = request.POST.get('day13')
            od.day13 = d13
        if request.POST.get('day14') != None:        
            d14 = request.POST.get('day14')
            od.day14 = d14
        if request.POST.get('day15') != None:        
            d15 = request.POST.get('day15')
            od.day15 = d15
        if request.POST.get('day16') != None:        
            d16 = request.POST.get('day16')
            od.day16 = d16
        if request.POST.get('day17') != None:        
            d17 = request.POST.get('day17')
            od.day17 = d17
        if request.POST.get('day18') != None:        
            d18 = request.POST.get('day18')
            od.day18 = d18
        if request.POST.get('day19') != None:        
            d19 = request.POST.get('day19')
            od.day19 = d19
        if request.POST.get('day20') != None:        
            d20 = request.POST.get('day20')
            od.day20 = d20
        if request.POST.get('day21') != None:        
            d21 = request.POST.get('day21')
            od.day21 = d21
        if request.POST.get('day22') != None:        
            d22 = request.POST.get('day22')
            od.day22 = d22
        if request.POST.get('day23') != None:        
            d23 = request.POST.get('day23')
            od.day23 = d23
        if request.POST.get('day24') != None:        
            d24 = request.POST.get('day24')
            od.day24 = d24
        if request.POST.get('day25') != None:        
            d25 = request.POST.get('day25')
            od.day25 = d25
        if request.POST.get('day26') != None:        
            d26 = request.POST.get('day26')
            od.day26 = d26
        if request.POST.get('day27') != None:        
            d27 = request.POST.get('day27')
            od.day27 = d27
        if request.POST.get('day28') != None:        
            d28 = request.POST.get('day28')
            od.day28 = d28
        if request.POST.get('day29') != None:        
            d29 = request.POST.get('day29')
            od.day29 = d29
        if request.POST.get('day30') != None:        
            d30 = request.POST.get('day30')
            od.day30 = d30
        if request.POST.get('day31') != None:        
            d31 = request.POST.get('day31')
            od.day31 = d31               
        od.save()        
        print(str(od))        
        return redirect('check2')

class TotalView(ListView):
    template_name = 'registration/total.html'
    model = Oder
    def get_queryset(self):
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
        mn_list=[]
        grby = od.values(d,'dining').annotate(total=Count(d))
        #grbyはオブジェクト型要素の配列となり、変数を使用できないのでオブジェクト型を用意して入れ替える
        if len(grby)>=1:
            groupby=grby[0]
            groupby['day']=groupby[d]
            mn_list.append(groupby)
        if len(grby)>=2:
            groupby1=grby[1]
            groupby1['day']=groupby1[d]
            mn_list.append(groupby1)
        if len(grby)>=3:
            groupby2=grby[2]
            groupby2['day']=groupby2[d]
            mn_list.append(groupby2)
        if len(grby)>=4:
            groupby3=grby[3]
            groupby3['day']=groupby3[d]
            mn_list.append(groupby3)
        if len(grby)>=5:
            groupby4=grby[4]
            groupby4['day']=groupby4[d]
            mn_list.append(groupby4)
        if len(grby)>=6:
            groupby5=grby[5]
            groupby5['day']=groupby5[d]
            mn_list.append(groupby5)
        if len(grby)>=7:
            groupby6=grby[6]
            groupby6['day']=groupby6[d]
            mn_list.append(groupby6)
        
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
        grby1 = od1.values(d,'dining').annotate(total=Count(d))
        #grbyはオブジェクト型要素の配列となり、変数を使用できないのでオブジェクト型を用意して入れ替える
        if len(grby1)>=1:
            groupby10=grby1[0]
            groupby10['day']=groupby10[d]
            mn_list.append(groupby10)
        if len(grby1)>=2:
            groupby11=grby1[1]
            groupby11['day']=groupby11[d]
            mn_list.append(groupby11)
        if len(grby1)>=3:
            groupby12=grby1[2]
            groupby12['day']=groupby12[d]
            mn_list.append(groupby12)
        if len(grby1)>=4:
            groupby13=grby1[3]
            groupby13['day']=groupby13[d]
            mn_list.append(groupby13)
        if len(grby1)>=5:
            groupby14=grby1[4]
            groupby14['day']=groupby14[d]
            mn_list.append(groupby14)
        if len(grby1)>=6:
            groupby15=grby1[5]
            groupby15['day']=groupby15[d]
            mn_list.append(groupby15)
        if len(grby1)>=7:
            groupby16=grby1[6]
            groupby16['day']=groupby16[d]
            mn_list.append(groupby16)
        print(mn_list)
        return mn_list

    def get_context_data(self, **kwargs):
        od=Oder.objects.filter(month=today.month,dining="総務").all()
        day = today.day        
        context = super().get_context_data(**kwargs)
        context['dy'] = day
        return context

class DetaiView(ListView):
    template_name = 'registration/detai.html'
    model = Oder
    def get_queryset(self):
        od=Oder.objects.filter(month=today.month).all()
        dy=today.day
        d='day'+str(dy)
        groupby={}
        groupby1={}
        groupby2={}
        groupby3={}
        groupby4={}
        groupby5={}
        groupby6={}
        group_by={}
        mn_list=[]
        grby = od.values('dining','username',d).annotate(total=Count(d))
        #grbyはオブジェクト型要素の配列となり、変数を使用できないのでオブジェクト型を用意して入れ替える
        print(grby)
        if len(grby)>=1:
            groupby=grby[0]
            groupby['day']=groupby[d]
            mn_list.append(groupby)
        if len(grby)>=2:
            groupby1=grby[1]
            groupby1['day']=groupby1[d]
            mn_list.append(groupby1)
        else:
            return mn_list
        if len(grby)>=3:
            groupby2=grby[2]
            groupby2['day']=groupby2[d]
            mn_list.append(groupby2)
        else:
            return mn_list         
        if len(grby)>=4:
            groupby3=grby[3]
            groupby3['day']=groupby3[d]
            mn_list.append(groupby3)
        else:
            return mn_list
        if len(grby)>=5:
            groupby4=grby[4]
            groupby4['day']=groupby4[d]
            mn_list.append(groupby4)
        else:
            return mn_list
        if len(grby)>=6:
            groupby5=grby[5]
            groupby5['day']=groupby5[d]
            mn_list.append(groupby5)
        else:
            return mn_list
        if len(grby)>=7:
            groupby6=grby[6]
            groupby6['day']=groupby6[d]
            mn_list.append(groupby6)
        else:
            return mn_list
        return mn_list

    def get_context_data(self, **kwargs):
        day = today.day        
        context = super().get_context_data(**kwargs)
        context['dy'] = day
        return context

class SendView(View):    
    def get(self,request, *args, **kwargs):        
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

        print(seizou)

        subject = "今日の弁当注文"
        message = od_mn
        from_email = "isasaku4669@gmail.com"
        recipient_list = ["isao@sakuma-elc.com"]
        
        send_mail(subject,message,from_email,recipient_list)

        return render(request, 'registration/send.html')     
