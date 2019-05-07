from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import edit
from django.contrib.auth import authenticate, login, logout, get_user
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Survey, Question, Answer, Publication
class LoginView(generic.View):
    template_name = 'main/login.html'
    def get(self,request,*args,**kwargs):
        return render(request,"main/login.html")
    def post(self,request,*args,**kwargs):
        username = request.POST['email']
        password = request.POST['password']    
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            context = {
                "not_user": True
            }
            return render(request,"main/login.html", context)
        return redirect(reverse_lazy('main:home'))
def logout_view(request):
    logout(request)
    return redirect("../")
def home_view(request):
    return render(request,"main/home.html",{})
class SurveyList(generic.ListView):
    model = Survey
    
class SurveyDetail(generic.DetailView):
    model = Survey
    fields = ['name','ask_count','surveyors','fee']    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.filter(survey=self.object)
        return context
class SurveyCreate(edit.CreateView):
    model = Survey
    fields = ['name','ask_count','fee','created_by']
    success_url = reverse_lazy('main:survey_list')
class SurveyDelete(edit.DeleteView):
    model= Survey
    success_url = reverse_lazy('main:survey_list')

class SurveyUpdate(edit.UpdateView):
    model = Survey
    fields = ['name','ask_count','fee']
    def get_success_url(self):
        return reverse('main:survey_detail',kwargs={'pk': self.object.id})
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.filter(survey=self.object)
        return context

class QuestionList(generic.ListView):
    model = Question
    def get_queryset(self):
        return Question.objects.filter(survey=Survey.objects.get(self.kwargs['pk']))

class QuestionDetail(generic.DetailView):
    model = Question
    fields = ['name']
    def get_object(self):
        return Question.objects.get(pk=self.kwargs['pk_q'])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answer_list'] = Answer.objects.filter(question=self.object)
        return context

class QuestionCreate(edit.CreateView):
    model = Question
    fields = ['name']
    def get_success_url(self):
        return reverse('main:survey_detail',kwargs={'pk': self.kwargs['pk']})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['survey_name'] = Survey.objects.get(pk=self.kwargs['pk']).name
        return context
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.survey = Survey.objects.get(pk=self.kwargs['pk'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class QuestionDelete(edit.DeleteView):
    model = Question
    def get_object(self):
        return Question.objects.get(pk=self.kwargs['pk_q'])
    def get_success_url(self):
        return reverse('main:survey_detail',kwargs={'pk': self.kwargs['pk']})

class AnswerCreate(edit.CreateView):
    model = Answer
    fields = ['text']
    def get_success_url(self):
        return reverse('main:question_detail',kwargs={'pk': self.kwargs['pk'],'pk_q': self.kwargs['pk_q']})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question_name'] = Question.objects.get(pk=self.kwargs['pk_q']).name
        return context
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.question = Question.objects.get(pk=self.kwargs['pk_q'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
class AnswerUpdate(edit.UpdateView):
    model = Answer
    fields = ['text']
    def get_success_url(self):
        return reverse('main:question_detail',kwargs={'pk': self.kwargs['pk'],'pk_q': self.kwargs['pk_q']})
    def get_object(self):
        return Answer.objects.get(pk=self.kwargs['pk_answer'])

class AnswerDelete(edit.DeleteView):
    model = Answer
    def get_object(self):
        return Answer.objects.get(pk=self.kwargs['pk_answer'])
    def get_success_url(self):
        return reverse('main:question_detail',kwargs={'pk': self.kwargs['pk'],'pk_q': self.kwargs['pk_q']})

class PublicationList(generic.ListView):
    template_name = 'main/publication_list.html'
    model = Publication
    def get_queryset(self):
        return self.request.user.publications.all
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        return context

class PublicationDetail(generic.DetailView):
    model = Publication
    fields = ['header', 'source', 'date_published','date_created','text']
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        return context

class PublicationUpdate(edit.UpdateView):
    model = Publication
    fields = ['header', 'source', 'date_published', 'text','releated_to']
    def get_success_url(self):
        return reverse_lazy('main:publication_detail',kwargs={'pk': self.kwargs['pk']})

class PublicationCreate(edit.CreateView):
    model = Publication
    fields = ['header', 'source', 'date_published', 'text','releated_to']
    success_url = reverse_lazy('main:publication_list')

class PublicationDelete(edit.DeleteView):
    model = Publication
    success_url = reverse_lazy('main:publication_list')