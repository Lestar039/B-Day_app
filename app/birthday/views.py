from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse

from .models import BirthdayData
from .forms import BirthdayDataForm
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

from loguru import logger
from .service.compire_date import run_compare


class IndexPage(TemplateView):
    template_name = 'birthday/index.html'


def redirect_to_user_page(request):
    """
    Redirect after Login to Dashboard Page
    """
    logger.debug(f'User {request.user.id} redirected to his dashboard')
    return redirect(f'/user/dashboard/{request.user.id}')


class Dashboard(ListView):
    model = ListView
    template_name = 'birthday/dashboard.html'
    context_object_name = 'birthdays'

    def get_queryset(self):
        return BirthdayData.objects.filter(user=self.kwargs['pk']).order_by('year', 'month', 'day')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_of_date'] = run_compare(self.kwargs['pk'])
        return context


class CreateBirthday(CreateView):
    form_class = BirthdayDataForm
    template_name = 'birthday/create.html'
    success_message = "B-Day Successfully Created"

    def form_valid(self, form):
        obj = form.save(commit=False)
        current_user = User.objects.get(id=self.kwargs['pk'])
        obj.user = current_user
        return super(CreateBirthday, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard_url', kwargs={'pk': self.kwargs['pk']})


class DetailBirthday(DetailView):
    model = BirthdayData
    template_name = 'birthday/detail.html'


class UpdateBirthday(UpdateView):
    model = BirthdayData
    template_name = 'birthday/update.html'
    fields = ['name', 'day', 'month', 'year']
    success_message = "Birthday data successfully updated!"


class DeleteBirthday(DeleteView):
    model = BirthdayData
    template_name = 'birthday/delete.html'
    success_message = "Deleted Successfully"

    def get_success_url(self):
        return reverse('dashboard_url', kwargs={'pk': self.kwargs['pk']})
