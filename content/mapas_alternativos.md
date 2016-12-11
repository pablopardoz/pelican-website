Title: Top 5 de los mejores mapas de QGIS
Date: 2010-12-03 10:20
Category: GIS
Tags: qgis, geoinnova, cartography
Slug: mejores_mapas_qgis
Summary: Como sabemos,a la hora de trabajar con la información geográfica en un SIG, no basta con incorporar, analizar y calcular datos, sino que tendremos que terminar el trabajo diseñando su salida gráfica (el mapa) para mostrar sus resultados. 

## Los Top 5 en mapas alternativos elaborados con QGIS

## 

Como sabemos,** a la hora de trabajar con la información geográfica en un SIG, no basta con incorporar, analizar y calcular datos, sino que tendremos que terminar el trabajo diseñando su salida gráfica (el mapa) para mostrar sus resultados**. Para eso, en numerosas ocasiones nos vamos a encontrar con que no tendremos que pensar mucho en este tema, es decir, la mayoría de veces ya sea el cliente, el organismo a quien pertenece, o la propia utilidad del mapa, [nos va a marcar una serie de estilos](http://geoinnova.org/blog-territorio/nueva-edicion-del-libro-guia-designing-better-maps-de-esri/) de los cuales será difícil salir.

Esto por un lado puede ser bueno, de hecho lo es, porque **estandariza los estilos** haciéndolos uniformes (el mundo sería un caos si los mapas mostraran los ríos en verde, o si cada geólogo mostrara las leyendas como quisiera).

Pero… ¿**qué ocurre cuando nos dan carta libre en este aspecto**? ¿Cuándo un cartógrafo, diseñador, analista de datos, o por qué no, un aficionado a los mapas, decide olvidar por un momento los estilos clásicos dejando volar su imaginación en lo que podemos definir como _**mapas alternativos**_ al marcado diseño estandarizado?

**Muchos de estos mapas alternativos no cuentan con escala gráfica, o con leyenda, o con ninguno de los elementos del mapa clásico**. Es más, **están más cerca del diseño gráfico que de la cartografía**. Seguro que podrían definirse como bonitos o feos, pero lo que no cabe duda es que son diferentes, curiosos, y que además… **¡están hechos con [QGIS](http://geoinnova.org/cursos/qgis-sistemas-de-informacion-geografica/)!**

He preparado una pequeña **selección de mis mapas alternativos hechos con QGIS preferidos**, para que veáis la potencialidad que tiene este software en la creación, no sólo de mapas clásicos, sino también en esta suerte de _mapas alternativos_.

#### Toponymic map of Great Britain, de Steven Kay.

## 

![mapas alternativos-qgis-steven-kay2](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/05/mapas-qgis-steven-kay2-1024x652.jpg)

Toponymic map of Great Britain, de Steven Kay

Este mapa me ha gustado porque muestra uno de los elementos que más me gusta: las **rejillas exagonales** para la muestra de información. Consiste en **mostrar datos vectoriales (información puntual, generalmente) en una rejilla, con la particularidad de ser hexagonal en lugar de la clásica cuadrada**.

#### Countries, scaled according to population, también de Steven Kay.

## 

![mapas alternativos-qgis-steven-kay1](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/05/mapas-qgis-steven-kay1-1024x724.jpg)

Countries, scaled according to population, también de Steven Kay

Este mapa lo he seleccionado porque también muestra dos elementos que llaman la atención, y no están muy vistos en la elaboración de cartografía.  
– Los **polígonos acordes a su área**: Esta particularidad se resolvería con un **cartograma**, pero **por el momento QGIS no dispone de esta funcionalidad**, por lo que **el autor lo ha resuelto mediante buffers acordes a un campo**. Una manera muy sencilla de resolverlo.  
– **Fondos en PNG**: Por otro lado, ha rellenado cada “país” con su bandera. Esto **QGIS** lo permite mediante la **creación de estilos de relleno propios**, junto con la **calculadora de campos,** que permite escoger un archivo u otro en función de un campo.

#### NY building ages, de Andy Tice.

## 

![mapas alternativos-qgis-andy-tice](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/05/mapas-qgis-andy-tice-1024x720.png)

NY building ages, de Andy Tice

Creo que no hay ningún **mapa de Manhattan** que no me guste, pero este me gusta especialmente. Realmente este mapa no tiene nada “especial” salvo su **paleta de colores**. En concreto, **se muestra la edad de cada edificio de Manhattan**. Es una buena muestra de lo que se puede hacer **con buenos datos, y buenos colores desde QGIS**.

#### Undersea internet cables of the world, de Tim Sutton

## 

![mapas alternativos-qgis-timlinux](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/05/mapas-qgis-timlinux-1024x532.png)

Undersea internet cables of the world, de Tim Sutton

Según dice, Tim Sutton (uno de los colaboradores en la creación el core de QGIS, así como presidente de su fundación) creó este mapa para mostrar algunas de las funcionalidades nuevas cuando añadieron la **creación de etiquetas personalizadas**. Es un buen ejemplo de lo que se puede hacer con esta funcionalidad, **creando un mapa de aspecto divertido**.

### Connected World, de Steven Lee.

## 

![mapas alternativos qgis-setphen-lee](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/05/mapas-qgis-setphen-lee-1024x717.png)

Connected World de Steven Lee

Dejo para el final este mapa porque me gusta especialmente. Como elementos que trae, muestra una**[proyección ortográgfica](https://es.wikipedia.org/wiki/Proyecci%C3%B3n_ortogr%C3%A1fica)** (¡**con QGIS también se puede**!) y otra de mis debilidades en un mapa, **las lineas que unen los puntos**.  
Con una nuena selección de colores para lograr un estilo “**lightbright**“, este mapa necesita poco más que un título o una descripción para comprender lo que nos pretende mostrar.

Esta no es más que una pequeña selección, extraída del [grupo de flickr](https://www.flickr.com/groups/qgis/pool/with/23879657709/) de **usuarios de QGIS**, donde numerosos autores suben sus **mapas** creados con este software. **Con este post se pretende dar a conocer las potencialidades de este software, no sólo para la creación de los “mapas más clásicos”, sino también para, como digo, la visualización de datos geográficos**.