from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Route
from .forms import RouterForm
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone

# Create your views here.
def home(request):
    BASE_URL = request.get_raw_uri()
    # return HttpResponse('Site is working')

    # mobile = request.user_agent.is_mobile
    # pc = request.user_agent.is_pc
    # device = 'Unkown'
    # if mobile:
    #     device='mobile'
    # elif pc:
    #     device='pc'
    #///
    # form.device = device

    # if request.user.is_authenticated:
    #     form.user = request.user
    # else:
    #     form.user = request.Meta.get('REMOTE_ADDR')

    form = RouterForm(request.POST or None)
    if form.is_valid():
        form.save()
        key = form.cleaned_data.get('key')
        messages.success(request, f"URL has been successfully shortened to {BASE_URL}{key}")
        url = str(BASE_URL)+str(key)
        return redirect(url)
    return render(request, 'router/homepage.html', {"form": form})

def how_to(request):
    # return HttpResponse("<h1>About Page</h1>")
    return render(request, 'router/guide.html')

class URLListView(ListView):
    model = Route
    context_object_name = 'urls'
    paginate_by = 10

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def redirector(request, key):

    if request.user.is_authenticated:
        route = Route.objects.get(user=request.user, key=key)
        instance = get_object_or_404(Route, key= key)
        clicked_data = route.clicked
        route.clicked = clicked_data + 1
        route.res_time = timezone.now()
        bench = route.req_time - route.res_time
        if route.bench == 0:
            route.bench = bench.microseconds
        route.save()
        #clicked = request.clicked
        #Route.objects.update(user=request.user, clicked=clicked+1)
        # response = redirect('/shortened-urls/')
        # return response
        return redirect(instance.original_url)
    else:
        instance = get_object_or_404(Route, key=key)
        return redirect(instance.original_url)