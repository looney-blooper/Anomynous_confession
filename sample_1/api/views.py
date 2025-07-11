from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Confessions
from .forms import confession_form

class home_page(View):
    def get(self,request):
        model = Confessions
        if request.user.is_authenticated:
            template = "home.html"
            my_comments = Confessions.objects.filter(user=request.user).order_by("-timestamp")
            return render(request, template, {'confessions':my_comments})
        else:
            template = "home.html"
            confessions = Confessions.objects.all().order_by("-timestamp")
            return render(request, template, {'confessions':confessions})
    

class create_confession(LoginRequiredMixin, View):
    template = "confession_form.html"
    success_url = reverse_lazy("api:all")

    def get(self, request):
        form = confession_form()
        ctx = {"form":form}
        return render(request, self.template,ctx )
    
    def post(self, request):
        form = confession_form(request.POST)
        if not form.is_valid():
            ctx = {'form':form}
            return render(request, self.template, ctx)
        confession = form.save(commit=False)
        confession.user = request.user
        confession.save()
        return redirect(self.success_url)
    

class update_confession(LoginRequiredMixin, View):
    model = Confessions
    template = "confession_form.html"
    success_url = reverse_lazy("api:all")

    def get(self, request, pk):
        confession = get_object_or_404(self.model, pk=pk)
        ctx = {"confession":confession}
        return render(request, self.template, ctx)
    
    def post(self,request,pk):
        confession = get_object_or_404(self.model, pk=pk)
        form = confession_form(request.POST, instance = confession)
        if not form.is_valid():
            ctx = {"form":form}
            return render(request, self.template, ctx)
        confession = form.save(commit=False)
        confession.user = request.user
        confession.save()
        return redirect(self.success_url)

class delete_confession(LoginRequiredMixin, View):
    model = Confessions
    template = "confession_delete_form.html"
    success_url = reverse_lazy("api:all")

    def get(self, request, pk):
        Confession = get_object_or_404(self.model, pk=pk)
        ctx = {"confession":Confession}
        return render(request, self.template, ctx)
    
    def post(self, request, pk):
        confession = get_object_or_404(self.model, pk=pk)
        confession.delete()
        return redirect(self.success_url)