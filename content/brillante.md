Title: Mapas brillantes con QGIS
Date: 2010-12-03 10:20
Category: GIS
Tags: qgis, geoinnova, cartography
Slug: mapas_brillntes_qgis
Summary: Tutorial para obtener un mapa brillante con QGIS.


El mapa brillante es una manera muy llamativa de presentar los datos geográficos, con unos pequeños trucos de visualización, podremos disponer de mapas muy vistosos.

Antes que nada, como continuación a **[este](http://geoinnova.org/blog-territorio/mapa-de-lineas-con-qgis/)** artículo, en el que enseñaba diversas maneras de visualizar conexiones entre líneas, voy a utilizar los mismos datos, para poder ver una aproximación con datos reales.

#### Aplicando estilos a puntos

## 

Para empezar, si cargamos los datos, vemos cómo **QGIS** los muestra de una manera demasiado estándar, la cuál vamos a ver cómo podemos ir cambiando para mejorar la visualización.![mapa_brillante_qgis1](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/10/Captura-de-pantalla-2016-10-27-a-las-20.19.26-1024x504.png) "brillante"

Al trabajar con tantos datos y a esta escala, podemos ver que tan sólo bajando sustancialmente el tamaño de los puntos obtendremos un resultado mucho más vistoso.

No es lo que buscamos, pero ya es un gran avance. Ésta es una buena práctica cuando no importa clasificar los datos por colores, sino que solo queremos mostrar una nube de puntos.

#### ¿Cómo podríamos mejorarlo?

## 

Bien, el objetivo de este tutorial es aprender a crear una nube de puntos (vectorial, es decir, sin entrar en la herramienta de crear **heatmaps** de QGIS) que visualice los puntos como si fueran brillantes.

Nuestro objetivo en este punto será crear un símbolo que emule a una luz brillante. Una opción sencilla, como se ha dicho, sería utilizar la herramienta de **heatmaps**, otra, también podría ser **crear un símbolo ráster con Gimp o Photoshop y aplicarlo a nuestros puntos**, pero insisto en que el objetivo de este artículo es el de aplicar toda la potencia que nos proporciona QGIS para trabajar con elementos vectoriales.

Para ello vamos a echar mano del editor de estilos de QGIS y vamos a crear los siguientes símbolos.

Primero seleccionaremos “**Marcador de relleno**” junto con relleno **Shapebrust**. Esta opción nos permitirá crear una escala que simulará el brillo de la luz. Para ello seleccionaremos dos colores, en mi caso la degradación irá del verde al mismo verde pero con el alpha al 90%, tal y como se muestra en la imagen.

El siguiente paso será crear un símbolo más, que será un círculo simple, blanco, que situaremos en el centro. Este círculo, sin borde, será el que simule la parte que “deslumbra” del punto.

El resultado de la figura deberá parecerse a la de la imagen, para la cuál también nos haremos servir de la herramienta “Sombrear a una distancia dada”, en mi caso ha sido de 6 milímetros.

Por último, el siguiente** “truco”** para sacar el mapa de brillos será la opción “Modo mezcla de capas”, la cuál situaremos en “Suma”.

Si para acabar ponemos el lienzo del mapa en negro, sí que seremos capaces de ver el verdadero mapa brillante.

Dependiendo de nuestros datos, la cantidad, la escala, o los elementos que queramos mostrar, podremos variar las opciones, lo mejor es ir haciendo pruebas.

#### ¿Y las líneas?

## 

También podemos utilizar estas opciones para estilar una bonita capa de líneas.

Volviendo a los datos del artículo anterior, y tocando las opciones de mezcla de capas y una buena transparencia, como muestra la imagen, podremos dar con un resultado tan sorprendente como el siguiente.

Ahora sabemos cómo hizo Facebook su ya famosísimo mapa de conexiones, y vemos también cómo con un conocimiento algo más profundo en **QGIS**, se pueden realizar trabajos similares. Todo es cuestión de profundizar en sus herramientas, ya que, aunque no sean muy populares, éstas nos permiten realizar salidas gráficas bastante potentes para evitar quedarnos en el mapa estándar.