from django.shortcuts import render

from .forms import *


class ProductConstructorMixin:

    form = None
    template = None

    def get(self, request, *args, **kwargs):

        return render(request, self.template, context={'form': self.form})

    def post(self, request, *args, **kwargs):

        form = self.form(request.POST)

        if form.is_valid():

            form.save()

            return render(request, self.template, context={'form': self.form})

        else:

            return render(request, self.template, context={'form': self.form})


