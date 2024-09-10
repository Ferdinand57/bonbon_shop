from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306123456',
        'name': 'Ferdinand Bonfilio Simamora',
        'class': 'KKI',
        'product1name': 'Cucumber juice',
        'product1price': 'Rp 5000,00',
        'product1desc': 'Basic choice for basic people',
        'product2name': 'Lemon juice',
        'product2price': 'Rp 6000,00',
        'product2desc': 'Anti-basic drink',
        'product3name': 'Water',
        'product3price': 'Rp 1000,00',
        'product3desc': 'Literally water',
    }

    return render(request, "main.html", context)