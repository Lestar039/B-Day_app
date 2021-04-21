from django.contrib.auth.models import User
from django.urls import  reverse

from .models import BirthdayData
from .forms import BirthdayDataForm
from django.views.generic import TemplateView, ListView, CreateView


class IndexPage(TemplateView):
    template_name = 'birthday/index.html'


class Dashboard(ListView):
    model = ListView
    template_name = 'birthday/dashboard.html'
    context_object_name = 'birthdays'

    def get_queryset(self):
        return BirthdayData.objects.filter(user=self.kwargs['pk'])


class CreateBirthday(CreateView):
    form_class = BirthdayDataForm
    template_name = 'birthday/create_bday.html'
    model = BirthdayData

    def form_valid(self, form):
        obj = form.save(commit=False)
        current_user = User.objects.get(id=self.kwargs['pk'])
        obj.user = current_user
        return super(CreateBirthday, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard_url', kwargs={'pk': self.kwargs['pk']})

