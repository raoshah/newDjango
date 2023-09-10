from .forms import ChatForm, UserRegistrationForm, UserLoginForm, PaymentForm, PhotoUploadForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Question, Youtube, Chat, library, Payment
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from PIL import Image
from django.contrib import messages
from django.conf import settings
import razorpay, logging, json, io
from nsetools import Nse
from pprint import pprint



def home(request):
    from nsetools import Nse
    from pprint import pprint
    nse = Nse()
    q = nse.get_index_quote("nifty 50")

    lib = library.objects.all()
    post = Post.objects.all()
    ans = Question.objects.all()
    z = 1
    a = ans[0]
    l = lib[0] 
    return render(request, "myapp/home.html", { "post": post, "z": z, "a": a, "lib":lib, "l": l, "index": q } )

def videos(request):
    videos = Youtube.objects.all()
    return render(request, "myapp/videos.html", { "videos": videos})

def libr(request):
    lib = library.objects.all()
    l = lib[0]
    return render(request, "myapp/libr.html", {"lib":lib, "l": l})

def rjgk(request):
    ans = Question.objects.all()
    a = ans[0]
    return render(request, "myapp/rjgk.html", { "a":a })

def libra(request, id):
    try:
        post = library.objects.all()
        r = post[id]
        b = id - 1
        a = post[b]

        if 'count' not in request.session:
            request.session['count'] = 1

        if 'score' not in request.session:
            request.session['score'] = 0

        if request.session['count'] != a.id:
            request.session['score'] = 0
            request.session['count'] = 1


        if request.method == "POST":
            ans = request.POST.get('a')
            if ans == a.ans:
                request.session['score'] += 1
                request.session['count'] += 1
                messages.success(request, f'Your Last Answer Was Right ...🥳🥳🥳🥳...')
                return render(request, "myapp/libra.html", { "ans": ans, "a": r, "score": request.session['score'], "count": request.session['count'] })
            else:
                request.session['count'] += 1
                messages.warning(request, f'Your Last Answer Was Wrong 😢😢😢😢😢😢.  Right Answer Was " {a.ans} "')
                return render(request, "myapp/libra.html", { "ans": ans, "a": r, "score": request.session['score'], "count": request.session['count'] })
    except (ValueError, IndexError) as e:
        return render(request, "myapp/error.html", {"error_message": str(e), "score": request.session['score']})

def react(request, id):
    try:
        post = Question.objects.all()
        r = post[id]
        b = id - 1
        a = post[b]

        if 'count' not in request.session:
            request.session['count'] = 1

        if 'score' not in request.session:
            request.session['score'] = 0

        if request.session['count'] != a.id:
            request.session['score'] = 0
            request.session['count'] = 1


        if request.method == "POST":
            ans = request.POST.get('a')
            if ans == a.ans:
                request.session['score'] += 1
                request.session['count'] += 1
                messages.success(request, 'Your Last Answer Was Right ...')
                return render(request, "myapp/react.html", { "ans": ans, "a": r, "score": request.session['score'], "count": request.session['count'] })
            else:
                request.session['score'] -= 1
                request.session['count'] += 1
                messages.warning(request, f'Your Last Answer Was Wrong.  Right Answer Was " {a.ans} "')
                return render(request, "myapp/react.html", { "ans": ans, "a": r, "score": request.session['score'], "count": request.session['count'] })
    except (ValueError, IndexError) as e:
        return render(request, "myapp/error.html", {"error_message": str(e), "score": request.session['score']})

def post(request, post_id):
    post = Post.objects.all()
    posts = int(post_id) - 1
    p = post[posts]

    return render(request, "myapp/post.html", { "post": p, "posts": post })


def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contact.html")

def chat(request):
    username = request.user.username
    post = Chat.objects.all()
    if request.method == 'POST':
        form = ChatForm(request.POST, request.FILES)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.username = request.user.username  # Set the username
            chat.save()
            return redirect('chat')
        else:
            print(form.errors)  
    else:
        form = ChatForm()
    return render(request, "myapp/chat.html", {"form": form, "post": post})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserRegistrationForm()
    return render(request, "myapp/register.html", {"form":form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chat')
    else:
        form = UserLoginForm()
    return render(request, "myapp/user_login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect('home')

def profile(request):
    return render(request, "myapp/profile.html")

logger = logging.getLogger(__name__)
client = razorpay.Client(auth=('rzp_test_EhpwhFXUZM7A5f', 'o87txmxSQsfJh35LRGu7Pj0s'))
def create_order(request):
    print(request.META.get('HTTP_HOST'))
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            amount = int(form.cleaned_data['amount']) *100
            description = form.cleaned_data['name']
            order = client.order.create({'amount': amount, 'currency': 'INR',})
            if request.META.get('HTTP_HOST') == 'localhost:8000':
                short_url = f"http://localhost:8000/payment/{order['id']},{order['amount']},{description}"
                return redirect(short_url)
            else:
                short_url = f"https://jangooji.onrender.com/payment/{order['id']},{order['amount']},{description}"
                return redirect(short_url)
                
    else:
        payl = client.payment.all()
        payl_data = payl
        items = payl_data.get('items', [])
        processed_items = []
        for item in items:
            amount_after_subtraction = item.get('amount') / 100
            item['amount_after_subtraction'] = amount_after_subtraction
            processed_items.append(item)
            form = PaymentForm()
    return render(request, 'myapp/create_order.html', {'form': form, "payl": processed_items,  "client": client})


def payment_view(request, order_id, amount, description):
    amount = int(amount) / 100
    return render(request, 'myapp/payment.html', {"order_id": order_id, "amount":amount, "description": description})


@csrf_exempt
def verify_payment(request):
    return render(request, 'myapp/payment_done.html')

def photo_to_pdf(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_photo = form.cleaned_data['photo']
            pdf_bytes = io.BytesIO()
            image = Image.open(upload_photo)
            image.save(pdf_bytes, 'PDF')
            response = HttpResponse(pdf_bytes.getvalue(), content_type='application/pdf')
            response['content-Disposition'] = 'filename="image_to_pdf.pdf"'
            return response
    else:
        form = PhotoUploadForm()
    return render(request, 'myapp/upload.html', {"form": form})



@csrf_exempt  # For development purposes only, remove this in production.
def get_suggestions(request):
    # Logic to fetch suggestions based on user input
    user_input = request.GET.get('term', '')
    user = Chat.objects.all()
    suggestions = [i.username for i in user]  # Replace with your suggestions logic
    
    # Return suggestions as JSON
    return JsonResponse(suggestions, safe=False)
