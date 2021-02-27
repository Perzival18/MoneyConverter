from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "convert/home.html")

def result(request):

    peso = float(request.GET.get('peso', 1))

    sar = peso * 0.077
    jpy = peso * 2.19
    usd = peso * 0.041
    cad = peso * 0.026
    ued = peso * 0.075

    return render(request, 'convert/conversion.html', {

      'sar': sar,
      'jpy': jpy,
      'usd': usd,
      'cad': cad,
      'ued': ued,

    })
