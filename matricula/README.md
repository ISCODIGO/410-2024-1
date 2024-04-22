# Django
## Instalacion del entorno virtual
Crear un entorno virtual
```
python -m virtualenv .venv
```
Activar el entorno virtual (Windows)
```
.\.venv\Scripts\activate.bat
```
## Instalar django
Instalar la ultima version de django.
```
pip install django
```
Crear un proyecto
```
python -m django startproject [nombre-proyecto]
```
Crear un app
```
python -m django startapp app
```
Iniciar proyecto (servicio web)
```
python manage.py runserver
```

## Crear modelos
### ForeignKey
Este tipo de campo permite enlazar un modelo con otro cuando se tiene una relacion de `1 a 1` (tambien se puede usar OneToOneField) o de `1 a muchos`

Cuando se agregan este tipo de campos en el modelo es necesario indicar el atributo `on_delete`, donde A y B se relacionan:
```
class B:
    campo = models.ForeigKey(A)
```
Es necesario agregar la  aqui se muestran las opciones:
- models.CASCADE: Si el registro de A queda se elimina, el registro de B se elimina tambien.
- models.PROTECT: Si A se intenta eliminar, se genera un `ProtectedError`.
- models.RESTRICT: Si A se intenta eliminar, se genera un `RestrictedError`.
- models.SET_NULL: Debe especificarse el atributo `null=True` para utilizarlo. Establece el campo como nulo, cuando A se elimina.
- models.SET_DEFAULT: Debe especificarse el valor por defecto. Establece el valor por defecto cuando A se elimina.