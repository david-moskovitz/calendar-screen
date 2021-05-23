from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from luach.models import *
from luach.forms import *


def screen_page(request):
    mydate = MyDate.objects.get(english_date=timezone.now())
    dayimage = DayImage.objects.filter(date=mydate)
    daymazel = MazelTov.objects.filter(date=mydate)
    add = Add.objects.last()
    message = Message.objects.first()


    context = {'mydate':mydate,'dayimage':dayimage,'daymazel':daymazel,'add':add,'message':message}
    return render(request, 'new.html',context)

def day_preview(request,pk):
    mydate = MyDate.objects.get(pk=pk)
    dayimage = DayImage.objects.filter(date=mydate)
    daymazel = MazelTov.objects.filter(date=mydate)
    add = Add.objects.last()
    message = Message.objects.first()

    context = {'mydate':mydate,'dayimage':dayimage,'daymazel':daymazel,'add':add,'message':message}
    return render(request, 'luach/preview.html',context)
########
#date
########
class MyDateListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'new.html'
    model = MyDate
    context_object_name = 'mydate'

    def get_queryset(self):
        return MyDate.objects.filter(english_date__gte=timezone.now()).order_by('english_date')

class CreateMyDateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'luach/dashboard.html'
    form_class = MyDateForm
    model = MyDate
    
@login_required   
def my_date_detail(request,pk):
    mydate = MyDate.objects.get(pk=pk)
    dayimage = DayImage.objects.filter(date=mydate)
    daymazel = MazelTov.objects.filter(date=mydate)


    context = {'mydate':mydate,'dayimage':dayimage,'daymazel':daymazel}
    return render(request, 'luach/mydate_detail.html',context)


class MyDateUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'luach/dashboard.html'
    form_class = MyDateForm
    model = MyDate
    

class MyDateDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'luach/dashboard.html'
    model = MyDate
    success_url = reverse_lazy('calendar')

########
#images
########
class ImagesListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'luach/dashboard.html'
    model = Images
    context_object_name = 'images'

@login_required
def create_image_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        
        
        for file_num in range(0, int(length)):
            Images.objects.create(
                image = request.FILES.get(f'images{file_num}')
            )

    return render(request, 'luach/add_images.html')
    

class ImagesDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'luach/dashboard.html'
    model = Images
    success_url = reverse_lazy('images')


########
#day image
########
@login_required
def create_day_image_view(request,pk):
    date = get_object_or_404(MyDate,pk=pk)

    hdate = date.hebrew_date
    alldate = MyDate.objects.filter(hebrew_date=hdate)

    if request.method == 'POST':
        form = DayImageForm(request.POST)
        if form.is_valid():
            image = form.cleaned_data['images']
            keep = form.cleaned_data['keep_every_year']
            till = form.cleaned_data['keep_till']
            if keep:
                for day in alldate:
                    DayImage.objects.create(
                        date = day,
                        images = image
                    )
            elif till > 1:
                keep_till = MyDate.objects.filter(english_date__gte=date.english_date)[:till]
                for day in keep_till:
                    DayImage.objects.create(
                        date = day,
                        images = image
                    )
            else:
                dayimage = form.save(commit=False)
                dayimage.date = date
                dayimage.save()
            return redirect('date_detail',pk=date.pk)
            
    else:
        form = DayImageForm()

    context = {'form': form,'date': date,}
    return render(request,'luach/dayimage_form.html',context=context)

class DayImageDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    redirect_field_name = 'luach/dashboard.html'
    model = DayImage


@login_required
def day_image_delete(request,pk):
    dayimage = get_object_or_404(DayImage,pk=pk)
    date_pk = dayimage.date.pk
    dayimage.delete()
    return redirect('date_detail',pk=date_pk)


#######
#mazel
#######
@login_required
def create_mazel_tov(request,pk):
    date = get_object_or_404(MyDate,pk=pk)
    if request.method == 'POST':
        form = MazelTovForm(request.POST)
        if form.is_valid():
            mazel = form.cleaned_data['mazel_tov']
            till = form.cleaned_data['keep_till']
            if till > 1:
                keep_till = MyDate.objects.filter(english_date__gte=date.english_date)[:till]
                for day in keep_till:
                    MazelTov.objects.create(
                        date = day,
                        mazel_tov = mazel
                    )
            else:
                mazel = form.save(commit=False)
                mazel.date = date
                mazel.save()
            return redirect('date_detail',pk=date.pk)
        
    else:
        form = MazelTovForm()
    
    context = {'form': form,'date': date,}
    return render(request,'luach/mazeltov_form.html',context=context)

class MazelTovUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'luach/dashboard.html'
    form_class = MazelTovForm
    model = MazelTov

class MazelTovDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    redirect_field_name = 'luach/dashboard.html'
    model = MazelTov

@login_required
def mazel_tov_delete(request,pk):
    mazel = get_object_or_404(MazelTov,pk=pk)
    date_pk = mazel.date.pk
    mazel.delete()
    return redirect('date_detail',pk=date_pk)

@login_required
def dashboard(request):
    mydate = MyDate.objects.filter(english_date__gte=timezone.now()).order_by('english_date')
    date = MyDate.objects.get(english_date=timezone.now())
    dayimage = DayImage.objects.filter(date=date)
    daymazel = MazelTov.objects.filter(date=date)
    add = Add.objects.last()
    message = Message.objects.first()

    context = {'mydate':mydate,'date':date,'dayimage':dayimage,'daymazel':daymazel,'add':add,'message':message}
    return render(request, 'luach/dashboard.html',context)
    
class MessageUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'luach/dashboard.html'
    form_class = MessageForm
    model = Message
    success_url = '/'

class AddCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'luach/dashboard.html'
    form_class = AddForm
    model = Add
    success_url = '/'

class LoginRedirect(TemplateView):
    template_name = 'luach/login_redirect.html'

class LogoutRedirect(TemplateView):
    template_name = 'luach/logout_redirect.html'