Title: Crear un mapa 2.5D con QGIS
Date: 2010-12-03 10:20
Category: GIS
Tags: qgis, geoinnova, cartography
Slug: 2_5_d_qgis
Summary: Creando un maa 2.5D con QGIS

###Crear un mapa 2.5D con QGIS

En su última versión, y gracias a una iniciativa de Matthias Kuhn, uno de sus principales desarrolladores, ha añadido la funcionalidad de crear **mapas en 2.5D**.


### Pero, ¿qué es un mapa 2.5D?

### 

Gracias a esta **visualización 2.5D, o perspectiva 3/4**, podemos obtener una vista algo diferente a nuestros mapas, dotándolos fácilmente de un sombreado y un efecto de altura a los edificios, estructuras, etc.

Por tanto, con esta perspectiva, como veremos, seremos capaces con suma facilidad de crear visualizaciones diferentes a nuestras representaciones cartográficas.

En este ejemplo voy a mostrar una manera rápida de **cómo crear un mapa 2.5D de edificios para un callejer**o.

### Los datos:

### 

Lo principal que necesitamos, como siempre, será una **fuente de datos cartográfica adecuada** para llevar a cabo esta demostración.

La característica más importante que ha de tener esta fuente, en este caso,  será un **campo que marque la altura del edificio**. Para este ejemplo he utilizado los **datos de [OSM](http://www.openstreetmap.es/)**, que **cuenta con este campo con el atributo “_heigth_“. (altura)**

![Cartografía con altura del OSM, convertir mapa 2.5D](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/06/mapa2.png)

Extracto de datos de OSM, antes de aplicarle el estilo de 2.5D

Es **muy importante que los datos estén proyectados en un sistema de metros** (si vamos a usar la altura en metros, claro). En mi caso está proyectada en **ETRS89**, y la altura está en metros.

### Visualización del mapa 2.5D

### 

Una vez tenemos los** datos proyectados y con el campo de altura**, sólo tendremos que ir a las**propiedades del mapa**, y seleccionar **“2.5 D”**, como se ve en la imagen.

![Estilos para implementar la visualización de un mapa 2.5D](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/06/Captura-de-pantalla-2016-06-13-a-las-1.24.17-1024x522.png)

Estilos para implementar la visualización en 2.5D

Como vemos, tras el resultado se creará un estilo propio y una serie de reglas en el dibujado de las entidades que **simularán las tres dimensiones**.

![Visualización tras la representación en 2.5D](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/06/mapa1.png)

Visualización tras la representación en 2.5D

Sólo nos queda cambiar un poco las **opciones para realizar el mapa a nuestro gusto**. Con esta capacidad, y jugando un poco con las capas a mostrar, podremos crear mapas tan originales como éste.

![Ejemplo de mapa 2.5D por Nicholas Duggan](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/06/Ejemplo-de-mapa-2.5D-por-Nicholas-Duggan-1024x519.png)

Ejemplo de mapa 2.5D por Nicholas Duggan.