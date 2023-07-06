from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from butler.forms import *
# Create your views here.
from django.core.mail import EmailMessage, get_connection
import core.config_template as settings


def send_email_mess(body, sub):
    with get_connection(  
        host=settings.EMAIL_HOST, 
        port=settings.EMAIL_PORT,  
        username=settings.EMAIL_HOST_USER, 
        password=settings.EMAIL_HOST_PASSWORD, 
        use_tls=settings.EMAIL_USE_TLS,
        use_ssl=settings.EMAIL_USE_SSL
        ) as connection:
        #print(form.cleaned_data)
        subject = sub  
        email_from = settings.EMAIL_HOST_USER  
        recipient_list = [settings.EMAIL_TO]  
        message = body 
        EmailMessage(subject, message, email_from, recipient_list, connection=connection).send() 

def index_html(request):
    if request.POST:
        form = MyForm(request.POST)
        if form.is_valid():
            body = f"""
            Имя: {form.cleaned_data['name']}\n
            Email: {form.cleaned_data['email']}\n
            Комментарий: {form.cleaned_data['message']}
            """
            send_email_mess(body, "Пользователь оставил отзыв")
    else:
        form = MyForm()

    menu = ButlerPage.objects.filter(slug__startswith='clean')
    context = {
        # "mainpage":ButlerPage.objects.get(slug="main"),
        "menu":menu,
        "form":form
    }
    return render(request, 'butler/pages/main.html', context=context)



def page_html(request):
    if request.POST:
        form = MyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = MyForm()
    slug = (request.path[1:-1])
    if not ButlerPage.objects.filter(slug=slug):
        menu = ButlerPage.objects.filter(slug__startswith='clean')
        print(menu)
        if not ButlerPage.objects.filter(slug__startswith='clean'):
            menu = ButlerPage.objects.filter(slug__startswith='clean')
            context = {
                "form":form
            }
        else:
            context = {
                "form":form,
                "menu":menu
            }
        return render(request, 'butler/pages/in_work.html', context=context)
    else:
        menu = ButlerPage.objects.filter(slug__startswith='clean')
        print(menu)
        context = {
            "mainpage":ButlerPage.objects.get(slug=slug),
            "form":form,
            "menu":menu
        }
        return render(request, 'butler/pages/simple.html', context=context)

def send_email(request):
    if request.method == 'POST':
        print(request.POST['email'])
    
    return HttpResponseRedirect('/')

#simple page
def contact_html(request):
    return render(request, 'butler/pages/contact.html')

def price_html(request):
    return render(request, 'butler/pages/price.html')

def order_html(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            services = ""
            for item in form.cleaned_data['service']:
                services += f"{SERVICE_CHOICES[int(item)][1]}, " 
            body = f"""
            Имя: {form.cleaned_data['name']}\n
            Фамилия: {form.cleaned_data['surname']}\n
            Номер телефона: {form.cleaned_data['phone']}\n
            Выбранные услуги: {services}\n
            Желаемое время оказания услуги: {form.cleaned_data['datetime']}\n
            Комментарий: {form.cleaned_data['comment'] or "Комментарий отсутствует"}
            """
            send_email_mess(body, "ЗАКАЗ")
    else:
        form = OrderForm()
    context = {
            "form":form
        }
    return render(request, 'butler/pages/order.html', context)

def faq_html(request):
    if request.POST:
        form = MyForm(request.POST)
        if form.is_valid():
            body = f"""
            Имя: {form.cleaned_data['name']}\n
            Email: {form.cleaned_data['email']}\n
            Вопрос: {form.cleaned_data['message']}
            """
            send_email_mess(body, "Пользователь задал вопрос")
    else:
        form = MyForm()
    context = {
            "form":form,
            "faq":FAQmodel.objects.all()
        }
    return render(request, 'butler/pages/faq.html', context)



