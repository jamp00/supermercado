from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.catalogo.models import Catalogo

# Create your views here.
import requests
requests.packages.urllib3.disable_warnings()

from bs4 import BeautifulSoup


def scraperSuper_1(request):

    session = requests.Session()
    session.header = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
    }

    url= 'https://www.lider.cl/supermercado/category/Bebidas-Licores/Bebidas/Energética/_/N-rnzp9l'
    conetnt = session.get(url, verify= False).content

    soup = BeautifulSoup(conetnt, "html.parser")

    items = soup.find_all('div', {'class':'product-item-box'}) #Return a list

    for i in items:
        precio = i.find('span', {'price-sell'}).text
        precio = precio.replace('$', '')
        sku = i['prod-number']
        articulo = i.find('span', {'class': 'product-description' }).text
        url_img = i.find('img', {'class': 'img-responsive'})['src']
        oferta  = i.find('span', {'class': 'label-llevamas_fondo'})
        if (oferta is not None ):
            oferta = oferta.text
        else:
            oferta = ''

        catalogo = Catalogo()
        catalogo.supermercado = 'Supermercado_1'
        catalogo.precio = precio
        catalogo.sku = sku
        catalogo.articulo = articulo
        catalogo.url_img = url_img
        catalogo.oferta = oferta
        catalogo.save()

#        print('SKU: ' +sku+ ' Descripcion: ' +articulo+ ' Precio: ' +precio)
#        print(oferta)

    scraperSuper_2()

#    return redirect('/')
    return HttpResponse("Carga terminada")
#    print(len(items))

#scraper()


def scraperSuper_2():

    session = requests.Session()
    session.header = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
    }

    url = 'https://www.tottus.cl/tottus/browse/Jugos/114.4'
    conetnt = session.get(url, verify= False).content

    soup = BeautifulSoup(conetnt, "html.parser")

    items = soup.find_all('div', {'class': 'item-product-caption'}) #Return a list

    for i in items:
        precio = i.find('span', {'active-price'}).find('span').text.strip()
        precio = precio.replace('$', '')
        sku = i.find('input', {'class':'btn-add-cart'})['value']
        articulo = i.find('div', {'class': 'title' }).find('div').text.strip()
        url_img = i.find('img', {'class': 'media-object'})['data-src']
        oferta  = i.find('span', {'class': 'nule-price'})
        if (oferta is not None ):
            oferta = oferta.text.strip()
        else:
            oferta = ''

        catalogo = Catalogo()
        catalogo.supermercado = 'Supermercado_2'
        catalogo.precio = precio
        catalogo.sku = sku
        catalogo.articulo = articulo
        catalogo.url_img = url_img
        catalogo.oferta = oferta
        catalogo.save()

"""
        print('SKU: ' +sku+ ' Descripcion: ' +articulo+ ' Precio: ' +precio)
        print('Oferta: ' +oferta)
        print('img: ' + url_img)
"""

#    print(len(items))
#    return redirect('/')
#    return HttpResponse("index")
#    print(len(items))

