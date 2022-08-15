from django.views import generic
from .forms import UserCreationForm
from .service import send


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'User/signup.html'
    success_url = "/"

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form)