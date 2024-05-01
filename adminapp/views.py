from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .forms import ArtistRegistrationForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Replace with your desired redirect URL after login
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})

    return render(request, 'login.html')


from .models import Artist, Admin, Customer, Artwork , product # Import your Artist model


def artist_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        # Extract other form fields

        # Create and save the Artist instance
        artist = Artist(username=username, email=email)
        artist.save()

        # Redirect to a success page or login page
        return redirect('login')

    return render(request, 'artistregister.html')  # Render the registration form template


def checkadminlogin(request):
    adminuname = request.POST["username"]
    adminpassword = request.POST["password"]
    flag = Admin.objects.filter(Q(username=adminuname) & Q(password=adminpassword))
    if flag:
        return render(request, "adminhome.html")
    else:
        return HttpResponse("Login Failed")


def artistregisteration(request):
    name = request.POST["username"]
    email = request.POST["email"]
    mobile = request.POST["mobile"]
    password = request.POST["password"]
    gender = request.POST["gender"]
    dob = request.POST["dob"]
    types = request.POST["artist-type"]
    artist1 = Artist(name=name, email=email, mobile=mobile, gender=gender, date_of_birth=dob, category=types)
    Artist.save(artist1)
    return HttpResponse("Registered")


def addartist(request):
    form = ArtistRegistrationForm()
    return render(request, "add_artist.html", {"form": form})


# views.py

from django.shortcuts import render, redirect
from .forms import ArtistForm


def add_artist(request):
    if request.method == 'POST':
        artistuname = request.POST["username"]
        artistpassword = request.POST["password"]
        artistmobile = request.POST["mobile"]
        artistdob = request.POST["dob"]
        artistemail = request.POST["email"]
        artistgender = request.POST["gender"]
        artistcategory = request.POST["artist-type"]

        artist = Artist(username=artistuname, email=artistemail, phonenumber=artistmobile, gender=artistgender,
                        password=artistpassword)
        Artist.save(artist)

        return render(request, "artistregister.html")


def add_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  # You should hash and salt the passwords

        # Create a new admin user
        admin_user = Admin(username=username, password=password)
        admin_user.save()

        return redirect('admin_list')  # Redirect to the admin list page

    return render(request, 'add_admin.html')


from django.shortcuts import render
from .models import Admin,AuctionItem


def admin_list(request):
    admin_users = Admin.objects.all()
    context = {'admin_users': admin_users}
    return render(request, 'admin_list.html', context)


from django.shortcuts import render, redirect
from .models import Artist

from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

def admin_artist_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')

        # Create a new AdminArtist instance
        artist = Artist(name=username, password=password,  email=email, gender=gender, date_of_birth=dob)
        artist.save()

        return redirect('artistlogin')  # Redirect to the admin artist list

    return render(request, 'artist_signup_template.html')



def admin_customer_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')

        # Check if the mobile number is exactly 10 digits
        if len(mobile) == 10 and mobile.isdigit():
            # Create a new AdminArtist instance
            artist = Artist(name=username, password=password, mobile=mobile, email=email, gender=gender,
                            date_of_birth=dob)
            artist.save()

            return redirect('artistlogin')  # Redirect to the admin artist list
        else:
            # Mobile number is not valid, return an error or display a message
            error_message = "Mobile number must be exactly 10 digits."
            return render(request, 'artistlogin.html', {'error_message': error_message})

    return render(request, 'artistlogin.html')


def checkartistlogin(request):
    adminuname = request.POST["username"]
    adminpassword = request.POST["password"]
    flag = Artist.objects.filter(Q(name=adminuname) & Q(password=adminpassword))
    if flag:
        return render(request, "artist_home.html")
    else:
        return render(request,"artistlogin.html")


def admin_list(request):
    admin_users = Admin.objects.all()
    context = {'admin_users': admin_users}
    return render(request, 'artist.html', context)


def artwork_list(request):
    artworks = Artwork.objects.all()  # Retrieve all artwork listings from the database
    return render(request, 'artwork_list.html', {'artworks': artworks})


def add_artwork(request):


    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']

        # Create and save the artwork instance
        artwork = Artwork(
            title=title,
            description=description,
            price=price,
            image=image
        )
        artwork.save()
        return redirect('artwork_list')  # Redirect to the artwork list page

    return render(request, 'add_artwork.html')
def auction_list(request):
    items = AuctionItem.objects.all()
    return render(request, 'auction_list.html', {'items': items})


def cart_view(request):
    products = product.objects.all()
    total = sum(product.price for product in products)
    context = {'products': products, 'total': total}
    return render(request, 'cart.html', context)

def add_to_cart(request):
    product_id = request.POST.get('product_id')
    if product_id:
        cart = request.session.get('cart', {})
        cart[product_id] = cart.get(product_id, 0) + 1
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('cart')
def register(request, *args, ** kwargs):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if(password1 == password2):
            print(email)
            print(user_name)
            if(Artist.objects.filter(email=email).exists()):
                print('email exist')
                return redirect('register')
            elif (Artist.objects.filter(username=user_name).exists()):
                print('username exist')
            else:
                user = Artist.objects.create_user(username = user_name,password=password1, email=email,
                            first_name=first_name, last_name=last_name)
                user.save()
        else:
            return redirect('register')

        return redirect('login')
    return render(request, 'register.html')

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

stripe.api_key = 'sk_test_51O8rWvSDTDcI9bu1Hv5PoUsJ8bDz3QKD90dozlNXVyyg04NYWi5ufpAsChsbSRhPBweScCdUianIp8A4plKfHCy000v47tiQp9'

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET_KEY




def charge(request):

    return render(request, 'charge.html')
def payment_form(request):
    return render(request, 'payement_form.html')
