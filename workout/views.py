from django.shortcuts import render
from .models import Workout
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



@login_required
def index(request):
    all_workout = Workout.objects.all().count()
    powers = Workout.objects.filter(type__contains='po').count()
    functionals = Workout.objects.filter(type__contains='fu').count()
    cardios = Workout.objects.filter(type__contains='ca').count()
    crossfits = Workout.objects.filter(type__contains='cr').count()
    pilatess = Workout.objects.filter(type__contains='pi').count()
    rehabs = Workout.objects.filter(type__contains='re').count()

    context = {
        'all_workout': all_workout,
        'powers': powers,
        'functionals': functionals,
        'cardios': cardios,
        'crossfits': crossfits,
        'pilatess': pilatess,
        'rehabs': rehabs,
    }

    return render(request, 'index.html', context)


class PowerListView(LoginRequiredMixin, generic.ListView):
    model = Workout
    template_name = 'workout/power_list.html'
    paginate_by = 20

    def get_queryset(self):
        return Workout.objects.filter(type__contains='po')

class FunctionalListView(LoginRequiredMixin, generic.ListView):
    model = Workout
    template_name = 'workout/power_list.html'
    paginate_by = 20

    def get_queryset(self):
        return Workout.objects.filter(type__contains='fu')


class CardioListView(LoginRequiredMixin, generic.ListView):
    model = Workout
    template_name = 'workout/power_list.html'
    paginate_by = 20

    def get_queryset(self):
        return Workout.objects.filter(type__contains='ca')


class CrossfitListView(LoginRequiredMixin, generic.ListView):
    model = Workout
    template_name = 'workout/power_list.html'
    paginate_by = 20

    def get_queryset(self):
        return Workout.objects.filter(type__contains='cr')


class PilatesListView(LoginRequiredMixin, generic.ListView):
    model = Workout
    template_name = 'workout/power_list.html'
    paginate_by = 20

    def get_queryset(self):
        return Workout.objects.filter(type__contains='pi')


class RehabListView(LoginRequiredMixin, generic.ListView):
    model = Workout
    template_name = 'workout/power_list.html'
    paginate_by = 20

    def get_queryset(self):
        return Workout.objects.filter(type__contains='re')


class WorkoutDetailView(LoginRequiredMixin, generic.DetailView):
    model = Workout
    template_name = 'workout/power_detail.html'


class WorkoutCreate(CreateView):
    model = Workout
    fields = '__all__'



class WorkoutUpdate(UpdateView):
    model = Workout
    fields = '__all__'

class WorkoutDelete(DeleteView):
    model = Workout
    success_url = reverse_lazy('index')