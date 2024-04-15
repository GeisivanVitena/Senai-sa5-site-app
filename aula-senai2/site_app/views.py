from django.http import HttpResponse
from django.shortcuts import render, redirect
from site_app.models import Cliente

dados = []

# Create your views here.

def home(request):
    return render(request,'site_app/global/home.html') 

def cadastro(request):
    
    global dados
    nome = ""
    email = ""
    idade = 0
    pais = ""
    dados = Cliente.objects.all()

    if request.POST:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        idade = request.POST.get("idade", 0)
        pais = request.POST.get("pais")
        Cliente.objects.create(nome = nome, email = email, idade = idade, pais = pais)

    return render(request,'site_app/global/cadastro.html', context={"dados": dados, "nome": nome, "email": email, "idade": idade, "pais": pais}) 


def criar(request):

    nome = ""
    email = ""
    idade = 0
    pais = ""
    

    if request.POST:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        idade = request.POST.get("idade", 0)
        pais = request.POST.get("pais")
        Cliente.objects.create(nome = nome, email = email, idade = idade, pais = pais)

    return render(request,'site_app/partials/criar.html', context={"nome": nome, "email": email, "idade": idade, "pais": pais}) 

def deletar(request, id=0):

    cliente = {}

    if id:

        cliente = Cliente.objects.get(id=id)
        cliente.delete()
        return redirect(deletar)
    
    cliente["dados"] = Cliente.objects.all()
    return render(request, "site_app/partials/deletar.html", context=cliente)

def atualizar(request, id=0):

    cliente = {}

    if id:
    
        if request.POST:

            cliente = Cliente.objects.get(id=id)
            cliente.nome = request.POST.get("nome", cliente.nome)
            cliente.email = request.POST.get("email", cliente.email)
            cliente.idade = request.POST.get("idade", cliente.idade)
            cliente.pais = request.POST.get("pais", cliente.pais)

            cliente.save() 

            return redirect(atualizar)
        
        cliente["cliente"] = Cliente.objects.get(id=id)
        return render(request, "site_app/global/update.html", cliente)
    
    cliente["dados"] = Cliente.objects.all()
    return render(request, "site_app/global/atualizar.html", context=cliente)

def pesquisar(request):

    dados = {}
    
    if request.POST:
        nome_filter = request.POST.get("nome")
        dados["dados"] = Cliente.objects.filter(nome__icontains=nome_filter)
    else:
        dados["dados"] = Cliente.objects.all()
    
    return render(request, 'site_app/global/pesquisar.html', dados)
    

def contatos(request):
    return render(request, 'site_app/global/contatos.html')

def produtos(request, id=0):

    dados = [
        {
            "id" : 1,
            "titulo" : "X-Bacon",
            "img" : "https://emporioserradourada.com.br/wp-content/uploads/2022/01/x-bacon.jpeg"
        },
        {
            "id" : 2,
            "titulo" : "X-Galinha",
            "img" : "https://s3.us-west-2.amazonaws.com/whatsmenu/production/xandylanches/products/165735/20170914011528a269962fe1424e1ca3e68c328b9fed611936462551imgofertaspremiumjpg"
        },
        {
            "id" : 3,
            "titulo" : "Mafioso",
            "img" : "https://i0.wp.com/imagensemoldes.com.br/wp-content/uploads/2020/03/X-Burguer-Hamburguer-Gourmet-Cheeseburguer-PNG.png?fit=850%2C718&ssl=1"
        },
    ]

    if id != 0:
        produtos = [dados[id - 1]]
    return render(request, 'site_app/global/produtos.html', context={"produtos": dados})

def detalhesprodutos(request, id=0):

    detalhes = [
        {
            "id" : 1,
            "titulo" : "X-Bacon",
            "descricao" : "Double bacon, dois super hamburguers de 100g, queijo cheaddar, cebola caramelizada",
            "img" : "https://emporioserradourada.com.br/wp-content/uploads/2022/01/x-bacon.jpeg",
            "preco": 12.75 
        },
        {
            "id" : 2,
            "titulo" : "X-Galinha",
            "descricao" : "Dois super hamburgueres de frango de 100g, queijo mussarela e tomate",
            "img" : "https://s3.us-west-2.amazonaws.com/whatsmenu/production/xandylanches/products/165735/20170914011528a269962fe1424e1ca3e68c328b9fed611936462551imgofertaspremiumjpg",
            "preco": 15.33
        },
        {
            "id" : 3,
            "titulo" : "Mafioso",
            "descricao" : "Dois super hamburgueres de 100g, queijo mussarela, cebola caramelizada e Jack Daniels",
            "img" : "https://i0.wp.com/imagensemoldes.com.br/wp-content/uploads/2020/03/X-Burguer-Hamburguer-Gourmet-Cheeseburguer-PNG.png?fit=850%2C718&ssl=1",
            "preco": 18.75
        },
    ]

    produto = None
    for detalhe in detalhes:
        if detalhe['id'] == id:
            produto = detalhe
            break

    return render(request, 'site_app/global/detalhes.html', context={"detalhesprodutos": produto})

