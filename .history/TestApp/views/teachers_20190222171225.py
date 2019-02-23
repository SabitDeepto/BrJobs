from django.views.generic import CreateView, ListView, UpdateView


class TeacherSignUpView(CreateView):
    # model = User
    # form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'