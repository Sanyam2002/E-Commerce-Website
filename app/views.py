from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View   
from .models import Customer,Product,Cart,OrderPlaced , catcart
from .forms import CustomerRegistrationForm , CustomerProfileForm, LoginForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        men= Product.objects.filter(category= 'MF')
        women= Product.objects.filter(category= 'FF')
        mobiles= Product.objects.filter(category= 'M')
        laptops= Product.objects.filter(category= 'L')
        network= Product.objects.filter(category= 'ND')
        tv= Product.objects.filter(category= 'TVs')
        alls = Product.objects.filter(category ='TW')
        return render(request,'app/home.html',{'men': men ,'women':women,'mobiles':mobiles,'laptops':laptops,'network':network,'tv':tv ,'alls':alls})

def mobile(request,data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data=='MI' or data=='Samsung' or data=='Oneplus' or data=='Vivo' or data=='Oppo' or data=='iPhone':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data=='below':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__range=(0,10000))
    elif data=='above':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)
    return render(request, 'app/mobile.html', {'mobiles':mobiles})

def laptop(request,data=None):
    if data==None:
        laptops = Product.objects.filter(category="L")
    elif data=='Acer' or data=='Asus' or data=='Lenovo' or data=='MSI' or data=='HP' :
        laptops = Product.objects.filter(category='L').filter(brand=data)
    elif data=='below':
        laptops = Product.objects.filter(category='L').filter(discounted_price__range=(0,60000))
    elif data=='above':
        laptops = Product.objects.filter(category='L').filter(discounted_price__gt=60000)
    return render(request, 'app/laptop.html', {'laptops':laptops})


def men(request,data=None):
    if data==None:
        men = Product.objects.filter(category="MF")
    elif data=='Polo' or data=='Lee' or data=='Levis' or data=='Raymonds' or data=='Adidas':
        men = Product.objects.filter(category='MF').filter(brand=data)
    elif data=='below':
        men = Product.objects.filter(category='MF').filter(discounted_price__range=(0,1000))
    elif data=='above':
        men = Product.objects.filter(category='MF').filter(discounted_price__gt=1000)
    return render(request, 'app/men.html', {'men':men})

def women(request,data=None):
    if data==None:
        women = Product.objects.filter(category="FF")
    elif data=='Levis' or data=='Zara' or data=='Fashion_21' or data=='Mayra' or data=='Nike':
        women = Product.objects.filter(category='FF').filter(brand=data)
    elif data=='below':
        women = Product.objects.filter(category='FF').filter(discounted_price__range=(0,1000))
    elif data=='above':
        women = Product.objects.filter(category='FF').filter(discounted_price__gt=1000)

    return render(request, 'app/women.html', {'women':women})

def furniture(request,data=None):
    if data==None:
        furniture = Product.objects.filter(category="FU")
    elif data=='Levis' or data=='Zara' or data=='Fashion_21' or data=='Mayra' or data=='Nike':
        furniture = Product.objects.filter(category='FU').filter(brand=data)
    elif data=='below':
        furniture = Product.objects.filter(category='FU').filter(discounted_price__range=(0,1000))
    elif data=='above':
        furniture = Product.objects.filter(category='FU').filter(discounted_price__gt=1000)

    return render(request, 'app/furniture.html', {'furniture':furniture})

def appliances(request,data=None):
    if data==None:
        appliances = Product.objects.filter(category='AP')
    elif data=='Levis' or data=='Zara' or data=='Fashion_21' or data=='Mayra' or data=='Nike':
        appliances = Product.objects.filter(category='AP').filter(brand=data)
    elif data=='below':
        appliances = Product.objects.filter(category='AP').filter(discounted_price__range=(0,1000))
    elif data=='above':
        appliances = Product.objects.filter(category='AP').filter(discounted_price__gt=1000)

    return render(request, 'app/appliances.html', {'appliances':appliances})

def cart(request,category=None):
    user=request.user
    # product_id = request.GET.get('prod_id')
    # pr = product_id
    # print(product_id)
    # product = Product.objects.get(id=product_id)
    # Cart(user=user, product=product).save()
    if category==None:
        return redirect('/cart')
    elif category=='Electronics':
            # ca='Electronics'
            # catego=ca
            # catego='Electronics'
            # Cart(catego=catego).save()
            cart =Cart.objects.filter(user=user).filter(catego = 'E')
            # ca='Electronics'
            # catego=ca
            # Cart(catego=catego).save()
            # Cart(catego=ca).save()
            # cart=Cart.objects.filter(user=user).filter(catego='E') 
            return render(request , 'app/electronics.html',{'cart':cart})
    elif category=='Fashion':
        cart=Cart.objects.filter(catego='F') 
        return render(request , 'app/fashion.html',{'cart':cart})


class CatCartView(View):
    def get(self,request):
        # product = Product.objects.get(pk=pk)
        electronics = catcart.objects.filter(categ = 'E')
        fashion = catcart.objects.filter(categ = 'F')
        return render(request, 'app/addtocart.html',{'electronics':electronics,'fashion':fashion} )

# def catcartt(request,data=None):
#     if data==None:
#         cat=Cart.objects.filter()
#     elif data=='Electonics':  
#         cat = Cart.objects.filter(categ='E')
#     elif data=='Fashion':
#         cat = Cart.objects.filter(categ='F')
#     return render(request, 'app/addtocart.html',{'cat':cat})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class ProductDetailView(View):
    def get(self, request , pk):
        product = Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})


def add_to_cart(request, category=None):
   if not request.user.is_authenticated:
            form = LoginForm()
            return render(request, 'app/logincart.html',{'form':form})
            # return redirect('/addtocart/accounts/login')
   elif request.user.is_authenticated:
        user= request.user
        product_id = request.GET.get('prod_id')
    # print(product_id)
        product = Product.objects.get(id=product_id)
        Cart(user=user, product=product ).save()
        # if category=='M' or category=='L':
        #         catego='Electronics'
        #         c = catego
        #         c.save()        
        # Cart(user=user, product=product ).save()
        # if category=='Electronics':
        #     catego='E'
        #     catego=catego.save()
        return redirect('/cart')

def show_cart(request):
   if request.user.is_authenticated:
       user = request.user
       cart = Cart.objects.filter(user=user)
       amount = 0.0
       shipping_amount = 50.0
       total_amount = 0.0
       print(cart)  
       cart_product =  [p for p in Cart.objects.all() if p.user==user]
       print(cart_product)
       if cart_product:
            for p in cart_product:
               tempamount = (p.quantity * p.product.discounted_price)
               amount +=tempamount
               total_amount= amount + shipping_amount
            return render(request, 'app/addtocart.html',{'carts':cart , 'total_amount':total_amount , 'amount':amount})
       else:
            return render(request, 'app/emptycart.html')
            


def plus_cart(request):
    if request.method == 'GET':
        # user = request.user
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amaount = 50.0
        total_amount = 0.0
        cart_product =  [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
               tempamount = (p.quantity * p.product.discounted_price)
               amount +=tempamount
               total_amount= amount + shipping_amaount
        data = {
                'quantity': c.quantity,
                'amount': amount,
                'total_amount': total_amount,
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        # user = request.user
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amaount = 50.0
        total_amount = 0.0
        cart_product =  [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
               tempamount = (p.quantity * p.product.discounted_price)
               amount +=tempamount
               if(amount==0.0):
                total_amount= amount 
               else:
                   total_amount= amount + shipping_amaount  
        data = {
                'quantity': c.quantity,
                'amount': amount,
                'total_amount': total_amount,
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        # user = request.user
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.delete()  
        amount = 0.0
        shipping_amaount = 50.0
        total_amount = 0.0
        cart_product =  [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
               tempamount = (p.quantity * p.product.discounted_price)
               amount +=tempamount
               if(amount==0.0):
                total_amount= amount 
               else:
                   total_amount= amount + shipping_amaount  
        data = {
                # 'quantity': c.quantity,
                'amount': amount,
                'total_amount': total_amount,
        }
        return JsonResponse(data)

def buy_now(request):
    return render(request, 'app/buynow.html')
 
# def profile(request):
#  return render(request, 'app/profile.html')
class ProfileView(View):
    def get(self , request):
        form = CustomerProfileForm()
        return render(request,'app/profile.html',{'form':form, 'active':'btn-primary'})
    def post(self, request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            usr= request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            phone = form.cleaned_data['phone']
            reg = Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode,phone=phone)
            reg.save()
            messages.success(request,'Your Profile Updated')
            return render(request, 'app/profile.html',{'form':form, 'active':'btn-primary'})

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')

# def change_password(request):
#  return render(request, 'app/changepassword.html')
 


# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')
class CustomerRegistrationView(View):
    def get(self,request):
        form= CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form} )
    def post(self,request):
        form= CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,"Registered Succesfully")
            form.save()
        return render(request,'app/customerregistration.html',{'form':form})
            
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amaount = 50.0
    total_amount = 0.0
    cart_product =  [p for p in Cart.objects.all() if p.user==request.user]
    if(cart_product):
        for p in cart_product:
               tempamount = (p.quantity * p.product.discounted_price)
               amount +=tempamount
        if(amount==0.0):
            total_amount= amount 
        else:
            total_amount= amount + shipping_amaount  
    return render(request, 'app/checkout.html' ,{'add':add ,'total_amount':total_amount ,'cart_items':cart_items})

def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart =  Cart.objects.filter(user=user)
    for c in cart: 
        OrderPlaced(user=user, customer=customer, product=c.product , quantity=c.quantity).save()
        c.delete()
    return redirect("orders")