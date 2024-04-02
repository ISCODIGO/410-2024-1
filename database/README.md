# CRUD
C - Create
```
INSERT INTO [nombre-tabla] (lista-de-campos) VALUES(valores-a-insertar)
```

Ejemplo
```
insert into alumnos(cuenta, nombre, carrera)
    values('202310011214', 'Andrea Alves', 'Derecho')
```


R - Read

Seleccionar una listas de campos de la tabla
```
SELECT lista-de-campos FROM tabla
```

Seleccionar todos los campos de la tabla
```
SELECT * FROM tabla

U - Update
```
UPDATE tabla SET campo=nuevo-valor, campo2=nueva-valor2
WHERE filtro
```

D - Delete
```
DELETE FROM tabla WHERE filtro
```

El objetivo del WHERE es que la condicion impuesta sea `TRUE` para que la sentencia sea ejecutada.

```
SELECT * FROM alumnos WHERE carrera='arquitectura'
```
