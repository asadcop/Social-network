# from tokenize import generate_tokens
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from socialnetwork import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .tokens import generate_tokens


# Create your views here.

def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['psw']
            password2 = request.POST['psw-repeat']
            
            if User.objects.filter(username=username):
                messages.error(request, "Username already exist! please try some other username")
                return redirect('/accounts/signup')
            
            if User.objects.filter(email=email):
                messages.error(request, "Emali already registered!")
                return redirect('/accounts/signup')
                        
            if password1 != password2:
                messages.error(request,"Password didn't match!")
                return redirect('/accounts/signup')
            
            if not username.isalnum():
                messages.error(request,"Username must be Alpha-Numeric!")
                return redirect('/accounts/signup')


            newuser = User.objects.create_user(username, email, password1)
            newuser.is_active=False


            newuser.save()

            messages.success(request, "Your Account has been successfully created. We have a confirmation email, please confiram your email in order to activate your account.")


            currency_site = get_current_site(request)
            email_subject = "Confirm your email"
            email_body = render_to_string('authentication/email_confirmation.html', {
                'name': newuser.username,
                'domain': currency_site.domain,
                'uid': newuser.pk, 
                'token': generate_tokens.make_token(newuser)
            }
            )
            email =  EmailMessage(
                email_subject,
                email_body,
                settings.EMAIL_HOST_USER,
                [newuser.email],
                
            )
            email.fail_silently=True
            email.send()

            return redirect('/accounts/login')
        return render(request, "authentication/signup.html")
    else:
        return redirect('/timeline/')
    

def signin(request):
    if not request.user.is_authenticated:      
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['psw']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "LogIn Successfull")
                return redirect('/timeline/')
            else:
                messages.error(request, "username or password maybe incorrect")
                return redirect('/accounts/login')

        return render(request, "authentication/signin.html")
    else:
        return redirect('/timeline/')

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfull")
    return redirect('/')

#email activate
def activate(request, uid, token):

    try:
        newuser = User.objects.get(pk=uid)
       
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        newuser = None
        
    if newuser is not None and generate_tokens.check_token(newuser, token):
        newuser.is_active=True 
        newuser.save()
        login(request, newuser)
        return  redirect('/timeline/')
    else:
        return render(request,'authentication/activation_failed.html')


#forgot password page rendar and get email address 
def forgot_password(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            email=request.POST['email']
            forgot_user=User.objects.filter(email=email).exists()
            if forgot_user:

                forgot_user_object=User.objects.get(email=email)
                currency_site = get_current_site(request)
                email_subject = "Forgot Password"
                email_body = render_to_string('authentication/email_forgot_password.html', {
                    'name': forgot_user_object.username,
                    'domain': currency_site.domain,
                    'uid': forgot_user_object.pk, 
                    'token': generate_tokens.make_token(forgot_user_object)
                }
                )
                email =  EmailMessage(
                    email_subject,
                    email_body,
                    settings.EMAIL_HOST_USER,
                    [forgot_user_object.email],
                    
                )
                email.fail_silently=True
                email.send()
            messages.success(request,'email sent successfully')
            return redirect('/accounts/login')
        return render(request,'authentication/forgot_password.html')
    else:
        return redirect('/')


def forgot_password_active_url(request,uid,token):
    try:
        resatuser = User.objects.get(pk=uid)
       
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        resatuser = None
    
    if resatuser is not None and generate_tokens.check_token(resatuser, token):
       return  render(request, 'authentication/resat_password.html',{'uid': uid})
    else:
        return render(request,'authentication/activation_failed.html')

#set new password 
def resat_password(request):
    if request.method=='POST':
        uid=request.POST['uid']
        password1=request.POST['psw']
        password2=request.POST['psw-repeat']

        try:
            resatuser = User.objects.get(pk=uid)
       
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            resatuser = None
        if resatuser is not None:

            if password1 != password2:
                    messages.error(request,"Password didn't match!")
                    return  render(request, 'authentication/resat_password.html',{'uid': uid})
            resatuser.set_password(password1)
            resatuser.save()
            messages.success(request,'your password has been successfully updated')


    

    return redirect('/accounts/login')
