# views.py

import account.views
import .forms


class SignupView(account.views.SignupView):

   form_class = classgotcha.forms.SignupForm

   def after_signup(self, form):
       self.create_profile(form)
       super(SignupView, self).after_signup(form)

   def create_profile(self, form):
       profile = self.created_user.profile  # replace with your reverse one-to-one profile attribute
       profile.birthdate = form.cleaned_data["birthdate"]
       profile.save()
