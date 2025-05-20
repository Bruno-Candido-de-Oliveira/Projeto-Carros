from django.shortcuts import render
from cars.models import Car

# Create your views here.
def cars_view(request):
    cars = Car.objects.all().order_by('model') #Define a variável cars como o retorno de todos os objetos da classe cars por meio da função 'all', ou seja, será atribuiído a ela todos os carros criados
    search = request.GET.get('search') #recebe a busca do usuário

    if search: #se a busca do usuário for verdadeira, exibirá o conteúdo conforme a solicitação
        cars = Car.objects.filter(model__icontains=search).order_by('model')


    return render( #no retorno da função, será exibido na tela do usuário o contúdo da variável car
        request, 'cars.html', 
        {'cars': cars}
    )

