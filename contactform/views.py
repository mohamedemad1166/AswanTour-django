from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = {
            'name': name,
            'email': email,
            'message': message
        }
        message = '''
        New Message:{}
        
        From:{}
        '''.format(data['name'], data['email'], data['message'])
        send_mail(data['name'], message, '', ['emadfire22@gmail.com'])
    return render(request, 'contactus.html')
