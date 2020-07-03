from django.shortcuts import render
from django.http import Http404
from django.urls import reverse,reverse_lazy
from .models import SMS
from django.views.generic import CreateView,DetailView,DeleteView,ListView
from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Users


from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class CreateMessage(LoginRequiredMixin,CreateView):
    model = SMS
    fields = ('message',)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.user.save()
        return super().form_valid(form)

class MessageList(LoginRequiredMixin,ListView):
    model = SMS

class MessageDetail(LoginRequiredMixin,DetailView):
    model = SMS

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['accounts'] = User
        return content


class MessageDelete(LoginRequiredMixin,DeleteView):
    model = SMS
    success_url = reverse_lazy('messages:all')

class UserMessages(LoginRequiredMixin,ListView):
    model = SMS
    template_name = 'Message/_sms.html'


    def get_queryset(self):
        try:
            self.message_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.message_user.posts.all()

    def get_context_data(self, **kwargs):  # this isn't necessary
        content = super().get_context_data(**kwargs)
        content['us'] = self.message_user.posts.all()
        return content