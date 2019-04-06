from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic, View
from django.http import JsonResponse
from recruitment.forms import GradeForm
from recruitment.models import Grade

# Create your views here.


class MainPageView(generic.TemplateView):
    template_name = 'index.html'


class AddMarkView(View, PermissionRequiredMixin):
    permission_required = 'recruitment.add_mark'
    template_name = 'add_mark.html'
    form_class = GradeForm

    def get(self, request):
        form = self.form_class(initial={
            'recruiter': request.user.id,
        })
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.recruiter = request.user
            grade.save()
            messages.success(request, 'The grade was successfully added')
            return redirect('/')
        return render(request, self.template_name, {'form': form})


class CandidatesListView(View):

    def get(self, request):
        response = []
        ids =[]
        grades = Grade.objects.all()
        for grade in grades:
            if grade.candidate.id in ids:
                pass
            else:
                response.append({
                    "pk": grade.candidate.id,
                    "full_name": grade.candidate.first_name + ' ' + grade.candidate.last_name,
                    "grades": [grade.value for grade in Grade.objects.filter(candidate_id=grade.candidate.id)],
                    "avg_grade": sum([grade.value for grade in Grade.objects.filter(candidate_id=grade.candidate.id)])\
                                / Grade.objects.filter(candidate_id=grade.candidate.id).count(),

                })
                ids.append(grade.candidate.id)
        return JsonResponse(response, safe=False)
