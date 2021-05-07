from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.http import HttpResponse
from .models import  City, Ma_dis, Sub_dis, Pos
from .form import  sub_disForm, MajorForm, CustomUserCreationForm





#SignUP View::
class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse("login")



class LandingPageView(TemplateView):
    template_name = "landing.html"


def landing_page(request):
    return render(request, "landing.html")

# Create your views here.

def homepage(request):
    #sub_dis = Sub_dis.objects.all()
    #context = {
    #    "Sub": sub_dis 
    #} 

    return render(request, "helpdesk/homepage.html")

# CREATE ----------------------------------------------------------
class Ma_disCreateView(CreateView):
    template_name = "helpdesk/major_create.html"
    form_class = MajorForm
    
    def get_success_url(self):
        return reverse("helpdesk:major-list")


def major_create (request):
    form = MajorForm()
    if request.method == "POST":
        form = MajorForm( request.POST)
        if form.is_valid():
            form.save()
            return redirect ("/")
    context = {
        "form" : form
    }
        
    return render(request, "helpdesk/major_create.html", context)



# liST ----------------------------------------------------------------------
class Ma_disListView(LoginRequiredMixin, ListView):
    template_name = "helpdesk/major_list.html"
    queryset = Ma_dis.objects.all()
    context_object_name = "ma_dis"

def major_List(request):
    ma_dis= Ma_dis.objects.all()
    
    context = {
        "ma_dis" : ma_dis
    }
        
    return render(request, "helpdesk/major_list.html", context)




# DETAILS ----------------------------------------------------------------------
class Ma_disDetailView(DetailView):
    template_name = "helpdesk/major_detail.html"
    queryset = Ma_dis.objects.all()
    context_object_name = "ma_dis"


def major_detail(request, pk):
    ma_dis= Ma_dis.objects.filter(id=pk)
   
    context = {
        "ma_dis" : ma_dis
    }
        
    return render(request, "helpdesk/major_detail.html", context)





# UPDATE views --------------------------------------------------------------------

class Ma_disUpdateView(UpdateView):
    template_name = "helpdesk/major_update.html"
    queryset = Ma_dis.objects.all()
    form_class = MajorForm
    
    def get_success_url(self):
        return reverse("helpdesk: major-list")



def major_update (request, pk):
   
    ma_dis= Ma_dis.objects.get(id=pk)
    form = MajorForm(instance=ma_dis)
    if request.method == "POST":
        form = MajorForm( request.POST, instance=ma_dis)
        if form.is_valid():
            form.save()
            return redirect ("/")
    context = {
        "form" : form,
        "ma_dis" : ma_dis
    }
        
    return render(request, "helpdesk/major_update.html", context)



# Delete views ----------------------------------------------------------------------------

class Ma_disDeleteView(DeleteView):
    template_name = "helpdesk/major_delete.html"
    queryset = Ma_dis.objects.all()
    
    
    def get_success_url(self):
        return reverse("helpdesk:major-list")


def major_delete(request, pk):
    ma_dis= Ma_dis.objects.get(id=pk)
    ma_dis.delete()

    return redirect ("helpdesk/")


'''    
##################################################
class Sub_CreateView(CreateView):
    model = Sub_dis
    form_class = sub_disForm
    success_url = reverse_lazy('person_changelist')

class Sub_UpdateView(UpdateView):
    model = Sub_dis
    form_class = sub_disForm
    success_url = reverse_lazy('person_changelist')

def load_cities(request):
    ma_id = request.GET.get('Ma_dis')
    cities = City.objects.filter(id=ma_id).order_by('name')
    return render(request, 'helpdesk/major_create.html', {'cities': cities})
#################################################





     # FORMs ------------------------------------------------------------>>
def region_create(request):
    form = RegionForm()
    if request.method == "POST":
        form = RegionForm( request.POST)
        if form.is_valid():
            form.save()
            return redirect ("/")
    context = {
        "form" : form
    }
        
    return render(request, "helpdesk/major_create.html", context)


def Sub_create(request):
    form = sub_disForm()
    if request.method == "POST":
        form = sub_disForm( request.POST)
        if form.is_valid():
            #ma_dis_id = Ma_dis.objects.get(mid=pk)
           # ma_dis_id = request.GET.get('Ma_dis')
            #cities = City.objects.filter(Ma_region=ma_dis_id).order_by('name')
        
            form.save()
            return redirect ("/")
    context = {
        "form" : form
    }
        
    return render(request, "helpdesk/major_create.html", context)

'''



'''
def Ma_dis_list(request):
    ma_dis = Ma_dis.objects.all()
    context = {
        "Major": ma_dis 
    } 

    return render(request, "helpdesk/Ma_dis_list.html", context)


def Ma_dis_detail(requast, pk):
    ma_dis = Ma_dis.objects.get(id=pk)

    print(lead)
    #return HttpResponse ("This is Detaul View")

    context = {
        "Major": lead 
    }
    return render(request, "helpdesk/Ma_dis_detail.html", context)


    #********************************************************************************************
    #********************************************************************************************
    #SUB_DIS ------------------------------------------------------>

def Sub_dis_list(request):
    sub_dis = Sub_dis.objects.all()
    context = {
        "Sub": sub_dis 
    }

    return render(request, "helpdesk/Sub_dis_list.html", context)

def Sub_dis_detail(requast, pk):
    sub_dis = Sub_dis.objects.get(id=pk)

    #return HttpResponse ("This is Detaul View")

    context = {
        "Sub": sub_dis 
    }
    return render(request, "helpdesk/Sub_dis_detail.html", context)



'''