from django.views.generic import ListView

from .models import Slider, Collection, BranchOffice


class MainPage(ListView):
    model = Slider
    template_name = "main_app/index.html"
    queryset = model.objects.filter(is_active=True)
    context_object_name = "sliders"

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context["collections"] = Collection.objects.filter(is_active=True)
        return context


class ContactPage(ListView):
    model = BranchOffice
    template_name = "main_app/contacts.html"
    queryset = model.objects.filter(is_active=True)
    context_object_name = "contacts"
