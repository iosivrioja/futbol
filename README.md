# Sistema de Gestión de Futbol - USAT

_Este proyecto es un entregable del curso de Ingenieria y Calidad de Sotfware, liderado por el Ing. Vilchez Rivas, Marlon Eugenio de la Universidad Nacional Santo Toribio de Mogrovejo_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Necesitas las siguientes herramientas para poder instalar el proyecto en tu máquina local. Revisar el archivo requirements.txt_

```
Python
Django
```

### Instalación 🔧

```
git clone https://github.com/iosivrioja/futbol.git #clona el repo

cd futbol # entras a la carpeta del repo

git branch nombre_de_su_rama # crea el nombre de tu rama

git checkout nombre_de_su_rama # cambias a tu rama

py -3 -m venv .venv # crea el entorno virtual de python (importante, si no lo haces puedes 
                    # arruinar tu python)

.venv\Scripts\activate # inicia el entorno virtual

pip install Django
pip install django-admin-volt
pip install Pillow
pip install colorama
pip install django-debug-toolbar
```

### Uso

```
git checkout nombre_de_su_rama # así cambian a su rama, por si acaso

git add . # para añadir los cambios

git commit -m "lo que quieran comentar" # para confirmar los cambios

git push -u origin nombre_de_su_rama
```

### Luego entran al Github

```
Entran a pull request
Hacen click en New Pull Request
Seleccionan la rama que han creado
Hacen click en Create Pull Request
```

### Luego de que los cambios fueran aprobados o de que alguien haya actualizado antes que ustedes

```
git add .
git commit -m "comentario"
git pull origin main # para descargar los cambios a tu rama
```


