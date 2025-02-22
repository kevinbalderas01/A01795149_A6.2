# Reservation system

Primero, para agregar Clientes, tenemos que llamar al programa de la manera 
```
 python .\handleClients.py -m:C .\Files\Customer_create.json
```
De esta manera cliente se añadira y se almacenara en el archivo Customers.json

Luego para editar y eliminar ponemos respectivamente


```
 python .\handleClients.py -m:U .\Files\Customer_update.json
```

```
 python .\handleClients.py -m:D .\Files\Customer_delete.json
```

Y se muestra al final el coverage:
![Imagen coverga](./imgs/Captura%20de%20pantalla%202025-02-22%20144426.png)

Ejecución de flake y de pylint:
![Imagen coverga](./imgs/image.png)

![Imagen coverga](./imgs/Captura%20de%20pantalla%202025-02-22%20145537.png)

Agregando un Cliente en un Archivo JSON primero, extraemos información, leemos modo de operación y creación nuevo archivo para persistencia de información:

![Imagen coverga](./imgs/Captura%20de%20pantalla%202025-02-22%20145739.png)


Ahora para añadir Hoteles, mismo comando con diferentes flags en la consola:

![Imagen coverga](./imgs/Captura%20de%20pantalla%202025-02-22%20145914.png)


