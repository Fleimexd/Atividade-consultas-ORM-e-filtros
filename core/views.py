from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Jogo, Desenvolvedora, Plataforma

def listar_jogos(request):
    busca = request.GET.get("busca", "").strip()
    desenvolvedora_id = request.GET.get("desenvolvedora", "")
    plataforma_id = request.GET.get("plataforma", "")

    jogos = Jogo.objects.all().order_by("nome")

    if busca:
        jogos = jogos.filter(nome__icontains=busca)

    if desenvolvedora_id:
        jogos = jogos.filter(desenvolvedora_id=desenvolvedora_id)

    if plataforma_id:
        jogos = jogos.filter(plataformas__id=plataforma_id)
        jogos = jogos.distinct()

    paginator = Paginator(jogos, 5)
    numero_pagina = request.GET.get("page")
    page_obj = paginator.get_page(numero_pagina)

    desenvolvedoras = Desenvolvedora.objects.all().order_by("nome")
    plataformas = Plataforma.objects.all().order_by("nome")

    contexto = {
        "page_obj": page_obj,
        "desenvolvedoras": desenvolvedoras,
        "plataformas": plataformas,
        "busca": busca,
        "desenvolvedora_selecionada": desenvolvedora_id,
        "plataforma_selecionada": plataforma_id,
    }

    return render(request, "core/listar.html", contexto)