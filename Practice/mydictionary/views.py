from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


vocabs = list()
meanings = list()
#pairs = dict()
class vocabForm(forms.Form):
    vocab = forms.CharField(label='New word')
    meaning = forms.CharField(label="Meaning")
    priority = forms.IntegerField(max_value=6, min_value=1, label='star')


# Create your views here.
#def dictName(request, dictname):
#    return render(request, "mydictionary/dictname.html", {'dictname': dictname})


def addWord(request):
    # server validation
    if request.method=='POST':
        filled_form=vocabForm(request.POST)
        if filled_form.is_valid():
            vocab=filled_form.cleaned_data[ 'vocab' ]
            meaning=filled_form.cleaned_data[ 'meaning' ]
            pairs.update({vocab:meaning})
            vocabs.append(vocab)
            meanings.append(meaning)
            #return HttpResponseRedirect("/mydictionary/listwords")
            return HttpResponseRedirect(reverse("mydict:listwords"))
        else:
            return render(request, 'mydictionary/addword.html', {'form':filled_form})

    return render(request, "mydictionary/addword.html", {'form':vocabForm()})
def listWords(request):
    if 'pairs' not in request.session:
        request.session['pairs']=dict()
    #return render(request, "mydictionary/listwords.html", {'vocabs': vocabs, 'meanings':meanings, 'Num':len(vocabs) })
    return render(request, "mydictionary/listwords.html", {'diction':request.session['pairs']})
