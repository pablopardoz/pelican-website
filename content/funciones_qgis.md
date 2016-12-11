Title: Funciones con Python en QGIS
Date: 2010-12-03 10:20
Category: GIS
Tags: qgis, geoinnova, cartography
Slug: funciones_python_qgis
Summary: Primera aproximación al uso de las funciones propias con python



En este artículo voy a explicar un poco las **primeras aproximaciones con Python para QGIS** **utilizando el nuevo editor de funciones**. Una de las herramientas que ha incorporado QGIS desde su versión 2.8 ha sido el editor de funciones propias con [Python](https://www.python.org/).

Como bien es sabido, QGIS dispone de una poderosa [API](http://qgis.org/api/) para realizar tanto plugins como scripts con este lenguaje. Esta API, en mi opinión, **a pesar de ser muy poderosa, resultaba algo inaccesible para un usuario no experimentado**, ya que tendía que acceder a ella a través de la consola de Python, lo cuál es bastante incómodo.

Como digo, a partir de esta versión de QGIS, **el usuario puede obtener una interfaz algo más amigable para empezar a programar pequeñas funciones con Python**.

Pero…**¿Qué son las pequeñas funciones?** Si no estás experimentado con temas de programación o de scripting, tal vez no sepas ni por dónde empezar, por eso vamos a ver una pequeña aproximación a esta funcionalidad a través de algunos casos prácticos.

Para comenzar se me ocurre un pequeño **CASO PRÁCTICO**: **A partir de una tabla de parcelas de las cuales tenemos el precio de venta, queremos calcular el precio del metro cuadrado. Una vez calculado, queremos colorear los “caros” en rojo y los “baratos” en verde**. Fácil, ¿No? Después podremos etiquetar las parcelas con su precio por metro cuadrado.

Como puedes intuir, no sólo habrá una manera de hacerlo, es más, no es una tarea muy difícil para realizar con el **selector de expresiones**, o con la **calculadora de campos**. Este es sólo un pequeño ejemplo de cómo empezar con las **funciones de Python**, pero también hay otra ventaja, y es que podemos acceder a las funciones desde cualquier ámbito de QGIS que nos permita el uso de expresiones. Por tanto, podremos usar la función para etiquetar, para colorear, y para calcular campos. Con el ahorro de esfuerzo que supone.

**Vamos a ver cómo empezar a trabajar con funciones:**

Importar una tabla de precios.

![EJERCICIO PRÁCTICO CON PYTHON](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/04/Captura-de-pantalla-2016-04-29-a-las-16.17.11-226x300.png)

Aspecto de la tabla a utilizar, con el campo precio

Primero debemos importar la tabla de precios a nuestro proyecto. Suponemos que podremos conectarnos vía Postgres, pero por el momento vamos a hacerlo con una tabla en local. Este es el aspecto que tendrá la tabla, sólo mostrará el ID de la parcela, y su precio catastral.

Una vez tenemos la tabla cargada, vamos a hacer nuestra pequeña función que **calcule el precio del metro cuadrado**. Simple, ¿no?. Para ello vamos al editor de expresiones, y vamos a la pestaña de funciones. Aquí es donde vamos a trabajar a partir de ahora.

![EJERCICIO PRÁCTICO CON PYTHON - 2](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/04/Captura-de-pantalla-2016-04-29-a-las-16.19.37-1024x420.png)

Editor de funciones de QGIS

Para explicar el editor de funciones por encima, sólo hay que saber que permite realizar pequeñas funciones con códigos que vas a usar a menudo. El resultado lo verás en la pestaña de funciones ya existentes, como la de calcular área, las condicionales, etc.

En mi caso la he llamado “Geomarketing” por si quiero agrupar en un futuro otras funciones similares. Bien, el código de la función es el siguiente:

![EJERCICIO PRÁCTICO CON PYTHON - 3](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/04/Captura-de-pantalla-2016-04-29-a-las-17.14.43.png)

Código Python de la función que se utilizará

Realmente sólo estamos trabajando con una línea, explicado, la sintaxis de Python sería:

1. Es la cabecera de la función, en ella le indicas, el número de **argumentos** que quieres que reciba la función, en este caso se ha dejado en auto, para que coja los argumentos que se le pasan automáticamente, y luego se le especifica el grupo con el que quieres que aparezca en el menú, como he dicho, lo he llamado **_Geomarketing_**.
2. _def_ es la palabra que usa Python para definir funciones, _calculaPrecio_ es el nombre como quieres llamar a la función, y las tres palabras dentro del paréntesis son los parámetros. **Los parámetros son los valores que le pasas a la función**, y con los que trabajará. Es importante saber que el editor de funciones de QGIS siempre necesita el parámetro _feature, _para referirse a todos los campos de la tabla, y el parámetro _parent_, que usa para mostrar los errores, por lo que serán obligatorios. Por tanto, como se puede intuir, yo sólo le estoy pasando el parámetro _precio_.
3. Este es **el cuerpo de la función**. Lo primero que hay que ver es el **indentado** de la línea, si te has aproximado a Python ya, sabrás que trabaja con indentados, por tanto, todo lo que esté cuatro espacios a la derecha de la definición de la función, estará dentro de la función.  
_Return_ es la palabra que usa Python (como muchos otros lenguajes) para devolver los datos. Y seguidamente le especificaremos qué ha de devolver. Pues bien, como es obvio, para calcular el precio por metro cuadrado, ha de devolver el precio, dividido por el área de cada polígono.  
Como vemos, “precio” es el nombre de la variable que **recibe como parámetro**, y el área la calcula a partir del otro parámetro obligatorio, _feature_. Feature será la llamada “entidad”, que tendrá una función (también llamado método) propia para calcular su geometría. Y esta a su vez, tendrá otra para calcular el área.

Pues así de sencilla resultaría la función para calcular el precio por metro cuadrado. Pulsaremos el triángulo de ejecutar, y ya la tendremos agregada a nuestro repositorio de funciones.

Para utilizar la función vamos a hacerla en dos sitios diferentes, así podremos ver el ámbito: **en el etiquetado**, y **en el coloreado del mapa**.

- **Etiquetado:**

Vamos a crear una etiqueta para las parcelas que muestre su precio.

Entramos en el etiquetador de QGIS sobre la capa de manzanas, y en el campo de expresiones, estableceremos el texto de la función, con el parámetro del campo de precio. Además aprovecharemos para redondear el valor, y darle un formato más atractivo.

![EJERCICIO PRÁCTICO CON PYTHON - 4](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/04/Captura-de-pantalla-2016-04-29-a-las-16.46.04-1024x100.png)

Código para etiquetar la capa

- **Coloreado del mapa:**

Estableceremos una regla para que, si el campo calculado por la función es mayor de 20€/m, será rojo, si no, será verde. Es más, no hará falta ni calcular un campo, simplemente estableciendo la regla con la función, obtendrá los valores.

![EJERCICIO PRÁCTICO CON PYTHON - 5](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/04/Captura-de-pantalla-2016-04-29-a-las-17.04.51-1024x216.png)

Reglas utilizadas para los estilos.

Por tanto, un ejemplo de cómo podría quedar nuestro mapa utilizando las funciones podría ser el de la imagen.

![EJERCICIO PRÁCTICO CON PYTHON - 6](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/04/Captura-de-pantalla-2016-04-29-a-las-17.03.09-942x1024.png)

Funciones en QGIS: Resultado tras aplicar la función

Con este artículo** hemos visto cómo con unas pequeñas nociones de código Python, con las funciones propias de PyQGIS, y el propio QGIS podemos crear soluciones que nos simplifican mucho nuestra tarea rutinaria con los GIS, incluso mejorar muchos elementos que no vienen de “serie”**.