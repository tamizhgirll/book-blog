from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from blog.models import Books, Recommendations
from django.template.defaulttags import register
from django.contrib.auth.decorators import login_required

@register.filter
def get_range(value):
    return range(value)

def mainPage(request):
    products = Books.objects.all()
    return render(request,'base.html',{'books':products})

def detailPage(request,id):
    data = get_object_or_404(Books,pk=id)
    return render(request,'detail.html',{'data':data})

@login_required()
def profilePage(request):
    data = Books.objects.all()
    return render(request,'profile.html',{'reviews':data})

class AddReview(CreateView):
    model = Books
    fields = "__all__"
    success_url = reverse_lazy('main')
    template_name = 'addBook.html'

class EditReview(UpdateView):
    model = Books
    fields = "__all__"
    success_url = reverse_lazy('profile')
    template_name = 'editReview.html'
    context_object_name = 'obj'
    def get_object(self, queryset=None):
        obj = get_object_or_404(Books,pk=self.kwargs['id'])
        return obj

class DeleteReview(DeleteView):
    model = Books
    template_name = 'deleteReview.html'
    success_url = reverse_lazy('profile')
    context_object_name = 'obj'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Books, pk=self.kwargs['id'])
        return obj


class AddRecommendation(CreateView):
    model = Recommendations
    fields = "__all__"
    success_url = reverse_lazy('main')
    template_name = 'recommend.html'


class ViewRecommendations(ListView):
    model = Recommendations
    context_object_name = 'recs'
    template_name = 'recommendations.html'