from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import(
    ListView,
    DetailView,
    FormView
)
from main import models, forms
from django.views.generic.detail import BaseDetailView

class Index(ListView):
    model=models.Question
    template_name='main/index.html'
    context_object_name='question_list'  #this is defined by default just doing it for further understanding


class Question(BaseDetailView, FormView):
    model=models.Question
    template_name='main/questions.html'
    form_class=forms.AnswerForm


    def get_context_data(self,*args, **kwargs):
        data=super().get_context_data(*args, **kwargs)
        data['answer']= models.Answer.objects.get(
            question=self.get_object(),
            user=self.request.user
        )

        return data

    def form_valid(self,form):
        #called only when form in valid
        obj=form.save(commit=False) #form.save saves the data to the database but using commit=False, it is not saved
        obj.question=self.get_object()
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect('/')

    def post(self,request,*args, **kwargs):
        self.object=self.get_object()
        return super().post(request,*args, **kwargs)


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
