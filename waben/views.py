from django.shortcuts import render,redirect
from django.views.generic import UpdateView
from django.views.generic.list import ListView
from .forms import SignUpForm,OderForm
from .models import Oder
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
import datetime
from django.contrib.auth.models import User
import calendar
from django.db.models import Count

today = datetime.date.today()

class IndexView(CreateView):
    form_class = OderForm
    template_name = "registration/index.html"
    model = Oder
    success_url = reverse_lazy('check')

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
        mn = today.month
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
        grby = od.values(d).annotate(total=Count(d))
        #grbyはオブジェクト型要素の配列となり、変数を使用できないのでオブジェクト型を用意して入れ替える
        if grby[0] is not None:
            groupby=grby[0]
            groupby['day']=groupby[d]
            group_by[groupby[d]]=groupby['total']
            mn_list.append(groupby)
        if len(grby)>=2:
            groupby1=grby[1]
            groupby1['day']=groupby1[d]
            group_by[groupby1[d]]=groupby1['total']
            mn_list.append(groupby1)
        else:
            return mn_list
        if len(grby)>=3:
            groupby2=grby[2]
            groupby2['day']=groupby2[d]
            group_by[groupby2[d]]=groupby2['total']
            mn_list.append(groupby2)
        else:
            return mn_list         
        if len(grby)>=4:
            groupby3=grby[3]
            groupby3['day']=groupby3[d]
            group_by[groupby3[d]]=groupby3['total']
            mn_list.append(groupby3)
        else:
            return mn_list
        if len(grby)>=5:
            groupby4=grby[4]
            groupby4['day']=groupby4[d]
            group_by[groupby4[d]]=groupby4['total']
            mn_list.append(groupby4)
        else:
            return mn_list
        if len(grby)>=6:
            groupb5=grby[5]
            groupby5['day']=groupby5[d]
            group_by[groupby5[d]]=groupby5['total']
            mn_list.append(groupby5)
        else:
            return mn_list
        if len(grby)>=7:
            groupby6=grby[6]
            groupby6['day']=groupby6[d]
            group_by[groupby6[d]]=groupby6['total']
            mn_list.append(groupby6)
        else:
            return mn_list
        return mn_list

    def get_context_data(self, **kwargs):
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
        grby2 = od.values('id').all()
        grby = od.values(d,'name').annotate(total=Count(d))
        #grbyはオブジェクト型要素の配列となり、変数を使用できないのでオブジェクト型を用意して入れ替える
        print(grby2)
        print(grby)
        if grby[0] is not None:
            groupby=grby[0]
            groupby['day']=groupby[d]
            group_by[groupby[d]]=groupby['total']
            mn_list.append(groupby)
        if len(grby)>=2:
            groupby1=grby[1]
            groupby1['day']=groupby1[d]
            group_by[groupby1[d]]=groupby1['total']
            mn_list.append(groupby1)
        else:
            return mn_list
        if len(grby)>=3:
            groupby2=grby[2]
            groupby2['day']=groupby2[d]
            group_by[groupby2[d]]=groupby2['total']
            mn_list.append(groupby2)
        else:
            return mn_list         
        if len(grby)>=4:
            groupby3=grby[3]
            groupby3['day']=groupby3[d]
            group_by[groupby3[d]]=groupby3['total']
            mn_list.append(groupby3)
        else:
            return mn_list
        if len(grby)>=5:
            groupby4=grby[4]
            groupby4['day']=groupby4[d]
            group_by[groupby4[d]]=groupby4['total']
            mn_list.append(groupby4)
        else:
            return mn_list
        if len(grby)>=6:
            groupb5=grby[5]
            groupby5['day']=groupby5[d]
            group_by[groupby5[d]]=groupby5['total']
            mn_list.append(groupby5)
        else:
            return mn_list
        if len(grby)>=7:
            groupby6=grby[6]
            groupby6['day']=groupby6[d]
            group_by[groupby6[d]]=groupby6['total']
            mn_list.append(groupby6)
        else:
            return mn_list
        return mn_list

    def get_context_data(self, **kwargs):
        day = today.day        
        context = super().get_context_data(**kwargs)
        context['dy'] = day
        return context
     