import io
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.backends.backend_agg import FigureCanvasAgg

from apps.catalogo.models import Catalogo

# Create your views here.

def home(request):
    return render(request, 'plot/index.html')

def plotS1(request):

    precioS1 = Catalogo.objects.filter(supermercado='Supermercado_1').values('precio')
    precioS2 = Catalogo.objects.filter(supermercado='Supermercado_2').values('precio')

    res1 = [int(sub['precio'].replace('.', '')) for sub in precioS1]
    res2 = [int(sub['precio'].replace('.', '')) for sub in precioS2]

    length_1 = len(res1)
    length_2 = len(res2)

    if (length_1 > length_2):
        x = range(0, length_1)
        res2 = res2 + [0] * (length_1 - length_2)  # Iguala las dimensiones del set para graficar
    else:
        x = range(0, length_2)
        res1 = res1 + [0] * (length_2 - length_1)  # Iguala las dimensiones del set para graficar

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()

    # Creamos los ejes
    axes = f.add_axes([0.15, 0.15, 0.75, 0.75]) # [left, bottom, width, height]
    axes.plot(x, res1)
    axes.plot(x, res2)
    axes.set_ylabel("Precio $")
    axes.set_title("Precio de catalogos por supermercado")

    f.legend(['Lider', 'Tottus'], loc='lower right')

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response
