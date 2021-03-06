from django.shortcuts import render,redirect 
from PyDictionary import PyDictionary
import requests
from .forms import AddLinkForm, AddDictForm, GenerateMetaForm
from .models import GenerateMeta, Link, WordDictionary
from django.views.generic import DeleteView
from django.urls import reverse_lazy 
from bs4 import BeautifulSoup
import requests
import lxml

# Create your views here.
def index(request):
    return render(request, 'scrapbs4/index.html')

def priceTracker(request):
     no_discounted = 0
     error = None 
     form = AddLinkForm(request.POST or None)

     if request.method == 'POST':
          try:
               if form.is_valid():
                    form.save()   
          except AttributeError:
               error = "Something went wrong with attributes............"

          except:
               error = "something went wrong...................."

     form = AddLinkForm()
     queryset = Link.objects.all()
     items_no = queryset.count()

     if items_no > 0 :
          discount_list = []
          for item in queryset:
               if item.old_price > item.current_price:
                    discount_list.append(item)
               no_discounted = len(discount_list)

     context = {
          'queryset':queryset,
          'items_no':items_no,
          'no_discounted':no_discounted,
          'form':form,
          'error':error,
     }

     return render(request, 'scrapbs4/pricetracker.html', context)

class LinkDeleteView(DeleteView):
     model = Link 
     template_name = 'scrapbs4/confirm_del.html'
     success_url = reverse_lazy('price-tracker')

def update_prices(request):
     queryset = Link.objects.all()
     for link in queryset:
          link.save()

     return redirect('price-tracker')     

def wordDictionary(request): 
     error = ""
     form = AddDictForm(request.POST or None)

     if request.method == 'POST':
          try:           
               if form.is_valid():
                    form.save()
          except:
               error = "Something Went Wrong..." 
    
     form = AddDictForm()
     queryset = WordDictionary.objects.all().order_by('-timeStamp')
     print(queryset)
    
     context =  {
          'queryset':queryset,
          'form':form,
          'error':error,
     }
     return render(request, 'scrapbs4/dictionary.html', context)

def SearchWord(request): 
     error = ""   
     if request.method == "POST":      
          word = request.POST['word']
          url = 'https://www.dictionary.com/browse/'+word 
          r = requests.get(url)
          data = r.content
          soup = BeautifulSoup(data, 'html.parser')
          span = soup.find_all('span', {"class": "one-click-content"})
          context = {'text': span[0].text, 'word': word}
          return render(request, 'scrapbs4/dictionary.html', context)
     else:
          context = {'error': "Something Went Wrong..."}
          return render(request, 'scrapbs4/dictionary.html', context)

def metaGenerator(request):
     error = ""
     form = GenerateMetaForm(request.POST or None)
     if request.method == 'POST':
          try:
               if form.is_valid():
                    form.save()
          except:
               error = "something went wrong........."

     form = GenerateMetaForm()
     queryset = GenerateMeta.objects.all()
     context = {
        'queryset':queryset,
        'form':form,
        'error':error,
     }

     return render(request, 'scrapbs4/metagenerator.html', context)  

def textGenerator(request):
     return render(request, 'scrapbs4/textgenerator.html')

def getPdf(request):
     return render(request, 'scrapbs4/getpdf.html')

def Blog(request):
     return render(request, 'scrapbs4/blog.html')

# def BlogPost(request, slug):
#      # return render(request, 'scrapbs4/blogpost.html {slug}')