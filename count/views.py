# from django.shortcuts import render

# Create your views here.


def home(request):
    ct = request.session.get('count', 0)
    newct = ct+1
    request.session['count'] = newct
    print(newct)
    return render(request, 'count/home.html', {'c': newct})
