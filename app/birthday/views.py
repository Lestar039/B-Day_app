from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse

from .models import BirthdayData
from .forms import BirthdayDataForm
from django.views.generic import TemplateView, ListView, CreateView

from loguru import logger


class IndexPage(TemplateView):
    template_name = 'birthday/index.html'


def redirect_to_user_page(request):
    """
    Redirect after Login to Dashboard Page
    """
    logger.debug(f'Redirect from login to {request.user.id} user dashboard')
    return redirect(f'/user/dashboard/{request.user.id}')


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

