from .models import EnglishWord, RussianWord, Picture
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


# Create your views here.
class AddEngWordView(CreateView):
    model = EnglishWord
    fields = ['word', 'rating']
    template_name = 'add_eng_word.html'
    success_url = '/add-rus-word/'

    def form_valid(self, form):
        word = form.cleaned_data.get('word')
        if not EnglishWord.objects.filter(word=word).exists():
            english_word = form.save()
            self.request.session['eng-pk'] = english_word.pk
        else:
            english_word = EnglishWord.objects.get(word=word)
            self.request.session['eng-pk'] = english_word.pk
        return redirect(self.success_url)

class AddRusWordView(CreateView):
    model = RussianWord
    fields = ['word',]
    template_name = 'add_rus_word.html'
    success_url = '/add-picture/'
    

    def form_valid(self, form):
        eng_pk = self.request.session['eng-pk']
        word = form.cleaned_data.get('word')
        if not RussianWord.objects.filter(word=word).exists():
            russian_word = form.save()
            self.request.session['rus-pk'] = russian_word.pk
        else:
            russian_word = RussianWord.objects.get(word=word)
            self.request.session['rus-pk'] = russian_word.pk
        return redirect(self.success_url)    

class AddPictureView(CreateView):
    model = Picture
    fields = ['image', 'description']
    template_name = 'add_picture.html'

    def form_valid(self, form):
        eng_pk = self.request.session['eng-pk']
        rus_pk = self.request.session['rus-pk']
        eng_inst = EnglishWord.objects.get(id=eng_pk)
        rus_inst = RussianWord.objects.get(id=rus_pk)
        pic_inst = Picture(english_word=eng_inst, russian_word=rus_inst)
        pic_inst.save()
        # Update success url later 
        return redirect('/add-rus-word/')