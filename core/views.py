from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import  OrderForm
from tgmessages import tgbot
from .decorators import check_recaptcha
# Create your views here.


form = OrderForm()

def index(request):
    return render(request, 'core/index.html', {'form': form})

def show_vacancy(request):
    return render(request, 'core/vacancy.html', {'form': form})

def show_contacts(request):
    return render(request, 'core/contacts.html', {'form': form})

@require_http_methods(["POST",])
def get_order(request):
    if request.is_ajax:
        form = OrderForm(request.POST)
        if check_recaptcha(request) and form.is_valid():
            tgbot.send_order_to_tg(tgbot.url, tgbot.method, tgbot.chat_id_al, request.POST)
            form.save()
            return JsonResponse({'success': ' Заявка принята'})
        else:
            return HttpResponse(status='400')

