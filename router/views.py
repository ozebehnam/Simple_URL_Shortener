from .serializers import RouteSerializer
from router import utils

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .forms import RouterForm
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Route

# Create your views here.
def home(request):
    BASE_URL = request.get_raw_uri()

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
    # if request.user.is_authenticated:
    #route = Route.objects.get(user=request.user, key=key)
    instance = get_object_or_404(Route, key=key)
    clicked_data = instance.clicked
    instance.clicked = clicked_data + 1
    instance.res_time = timezone.now()
    bench = instance.req_time - instance.res_time
    if instance.bench == 0:
        instance.bench = bench.microseconds
    instance.save()
    # clicked = request.clicked
    # Route.objects.update(user=request.user, clicked=clicked+1)
    # response = redirect('/shortened-urls/')
    # return response
    # return redirect(instance.original_url)
    # else:
    instance = get_object_or_404(Route, key=key)
    return redirect(instance.original_url)


class RouteListApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):

        routes = Route.objects
        serializer = RouteSerializer(routes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'original_url': request.data.get('original_url'),
            'key': utils.create_random_code(),
            'clicked': 1,
            'bench': request.data.get('time')
        }
        serializer = RouteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

