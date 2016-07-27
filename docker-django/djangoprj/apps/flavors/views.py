
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from braces.views import LoginRequiredMixin

from .models import Flavor


class FlavorActionMixin(object):
    fields = ('title', 'slug', 'scoops_remaining')

    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(FlavorActionMixin, self).form_valid(form)


class FlavorCreateView(LoginRequiredMixin, FlavorActionMixin, CreateView):
    model = Flavor
    success_msg = "Flavor created!"


class FlavorUpdateView(LoginRequiredMixin, FlavorActionMixin, UpdateView):
    model = Flavor
    success_msg = "Flavor updated!"


class FlavorDetailView(DetailView):
    model = Flavor


class FlavorListView(ListView):
    model = Flavor

    def get_queryset(self):
        # Fetch the queryset from the parent get_queryset
        queryset = super(FlavorListView, self).get_queryset()

        # Get the q GET parameter
        q = self.request.GET.get("q")

        if q:
            # Return a filtered queryset
            return queryset.filter(title__icontains=q)

        # Return the base queryset
        return queryset
