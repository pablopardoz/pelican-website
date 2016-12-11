Title: Unir líneas con puntos en QGIS
Date: 2010-12-03 10:20
Category: GIS
Tags: qgis, geoinnova, cartography
Slug: lineas_puntos_qgis
Summary: ¿Cómo trabaja QGIS con las proyecciones de las capas?

## ¿Cómo unir puntos con líneas desde QGIS?

Para este artículo he querido investigar un poco más en la metodología que se podría seguir para crear algunos [mapas como los que se vieron previamente en este blog](http://geoinnova.org/blog-territorio/qgis-top-5-mapas-alternativos/). Para ello esta vez he optado por explicar algunas maneras de crear un mapa de conexión de puntos mediante líneas, viendo algunas maneras para crear este tipo de mapas.

### Mapas de líneas

### 

Todos hemos visto el [mapa que conectaba las relaciones de Facebook](https://thenextweb.com/wp-content/blogs.dir/1/files/2013/06/107569098.jpg)(siguiente imagen) que dió la vuelta al mundo, si nos interesan los mapas, seguro que nos hemos topado con muchos otros, pero es cierto que** la creación de estos mapas no es algo que se suela explicar** (al menos no se muy a menudo), por eso he pensado hacer un pequeño tutorial sobre cómo podríamos utilizar QGIS para unir puntos con líneas y crear la base de un mapa de este estilo.

![unir mapas con lineas](https://thenextweb.com/wp-content/blogs.dir/1/files/2013/06/107569098.jpg)

El mapa de las conexiones de Facebook muestra la unión de puntos con líneas.

Para este reto, igual que para cualquier problema en esta vida, existirán diversas maneras de hacerlo, y seguro que ninguna es “la buena”, sino que **la mejor forma de unir puntos con líneas dependerá de muchos factores, como nuestras preferencias, con qué nos sentimos más cómodos, o incluso de los datos que tengamos, ya sea la cantidad, el formato, etc.**

Es por eso por lo que voy a intentar explorar varias maneras de resolver este problema, aunque en todas se emplee QGIS, van a ser muy distintas, ya que** en una utilizaré PostGIS, mientras que en otra utilizaré herramientas de interfaz de usuario**.

### Los datos

### 

Como sabemos, lo primero que necesitaremos para realizar cualquier estudio con GIS será los datos (con calidad a ser posible). Para ello **necesitaremos dos tablas primordiales, la de entidades, que será la tabla que guarde las geometrías (puntos) así como sus atributos. Y la de rutas, que será la que relacione dos puntos con líneas.** Esta segunda tabla no necesariamente tendrá geometría. Tan sólo será necesario un Id origen y un Id destino, así como un Id único para la ruta, aunque éste último no será necesario.

![tabla para unir puntos con qgis](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/05/Captura-de-pantalla-2016-05-31-a-las-23.47.04.png)

Tabla de entidades y tabla de origen-destino

Estos datos, como prueba, podemos conseguirlos de [openflights.com](http://openflights.org/data.html), **base de datos libre que relaciona los vuelos comerciales mundiales**.

Os pregntaréis “_¿por qué no tenemos dos tablas de puntos?_” Si no estamos familiarizados con los modelos de datos podemos pensar que la mejor manera de tener estos datos es con dos tablas, una que se llame orígenes, con los puntos y los atributos de los orígenes, y otra que se llame destinos, con los puntos y los atributos de los destinos, pero lo cierto es que **cuando creamos un buen modelo de datos, lo primero que hay que hacer es abstraer todas las entidades iguales en una sola tabla, para evitar así redundancia en los datos.** _¿Qué sentido tiene tener dos tablas iguales, pero con datos diferentes?_ Y lo que es peor, si trabajamos** con grandes volúmenes de datos, el peso de la tabla se duplicará, lo cuál puede ser muy pesado para nuestro servidor**.

Por tanto, esta manera de presentar los datos no sólo debemos aplicarla cuando organicemos nuestras bases de datos, sino que debemos tenerla presente cuando trabajemos con datos externos, pues lo más seguro es que vengan así estructurados.

Una vez entendido esto, somos capaces de saber que tenemos una tabla con todos los puntos, y otra con la relación entre ellos. Ahora **tendremos que relacionarlas ambas, para sacar la geometría de los puntos de la tabla de viajes.**

Estos datos, si bien es cierto que no son pocos, tampoco podemos decir que lleguen a ser [**Big Data**](http://geoinnova.org/blog-territorio/postgre-sql-big-data/). Muchos de los mapas de los que se ha hablado han sido elaborado con una cantidad ingente de datos (¡millones de puntos!) pero por temas técnicos y didácticos, voy a trabajar con una parte de éstos. Si bien es cierto, que mediante este método, el estudio se puede escalar sin ningún problema. Es decir, que **utilizando esta misma metodología podremos aplicarla a la cantidad de datos que queramos**.

### Primera aproximación para unir puntos con líneas: “The PostGIS way”

### 

Para la primera aproximación para unir puntos con líneas y crear un mapa en QGIS, he decidido utilizar[**PostGIS**](http://geoinnova.org/blog-territorio/postgis-la-mejor-opcion-para-el-analisis-espacial/), ya que es en mi opinión mi manera preferida de resolver esto, y así puedo explicar algunos conceptos que me parecen interesantes, ya no de PostGIS, sino de su integración con QGIS.

Como ya sabemos, PostGIS es el complemento para bases de datos espaciales de [Postgres](http://geoinnova.org/blog-territorio/el-secreto-de-las-bases-de-datos-espaciales/) y QGIS se lleva muy bien con él, por lo que **es muy fácil conectar QGIS con nuestra base de datos**. No voy a centrarme ahora en cómo conectarlo, pero seguro que recordaréis [este tutorial para conectar POSTGIS a QGIS](http://geoinnova.org/blog-territorio/tutorial-gis-conectar-postgis-desde-qgis/) de este mismo blog, que lo muestra claramente.

Por tanto, **una vez conectada nuestra base de datos, accederemos a nuestras tablas**.

Como sabemos, necesitamos una tabla con la geometría de ambas columnas id de la tabla de viajes, y que debemos sacarla de la tabla de entidades, por lo que,** en SQL este problema se resolverá fácilmente con una relación reflexiva o “_self join_“**.

Este concepto puede sonar extraño si no estamos familiarizados con él, pero si lo entendemos podemos ver que **tan sólo estamos “duplicando” una tabla, y simulando que hay dos**. Una irá relacionada con la columna de orígenes, y otra con la de destinos. Con un ejemplo se puede entender más claramente:

![código de programación en SQL postgis-líneas-select](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/06/Captura-de-pantalla-2016-06-04-a-las-9.58.00.png)

Código de consulta en SQL

Esta consulta será la encargada de devolvernos los campos que queremos, **la clave está en el alias del “_FROM”, e_**s decir, **de la tabla rutas, seleccionamos los campos Id y Nombre de origen, y los Id y Nombre de los destinos**.

En el _FROM_, es donde haremos la “trampa” y diremos que tabla1 y tabla2 son la tabla de geometrías, es decir, la duplicaremos. En segundo lugar, **relacionaremos con “**_WHERE_**” la tabla de rutas con las dos tablas de poblaciones.** Como sabemos que sus ID son iguales, diremos que _tabla1=origen_, y_tabla2_ a _destino_.

Para el siguiente paso **necesitaremos la función de postgis _st_makeline()_**, a la que le pasaremos las geometrías de los puntos, para que cree las líneas entre ellos. **También insertaremos la fórmula_row_number()_ con las que nos sacará un ID único para cada entidad**, esto nos ayudará a representarlo en QGIS. Y en el último AND, un pequeño filtro para que nos muestre sólo los vuelos que van a Madrid Barajas (MAD).

Siguiendo estas líneas,** ejecutaremos la consulta en la consola de Postgres de QGIS**, lo cual nos permitirá no sólo ejecutarla, sino que **también podremos visualizarla como una capa**.

El resultado sería algo similar a esto:

![postgis-select-líneas-result](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/06/Captura-de-pantalla-2016-06-04-a-las-10.03.28-1024x549.png)

Mapa donde se muestran las líneas creadas por nuestra consulta, que unen los aeropuertos seleccionados.

Por último, quedaría para este método la creación de líneas curvas [ortodrómicas](https://es.wikipedia.org/wiki/Ortodr%C3%B3mica), ya que es el mejor método para visualizar los datos de vuelos, pero lo dejaremos para un siguiente tutorial.

### Segunda aproximación: MMQGIS

### 

Si no te gusta PostGIS, o no te sientes agusto con el SQL, he elegido otra forma de resolver este problema en la que sólo se utilice la interfaz de usuario de QGIS.

Para ello **necesitaremos el plugin MMQGIS**. MMQGIS **es un plugin para QGIS bastante completo, de los mejores en mi opinión, que se encarga de manejar datos vectoriales.** Tiene infinidad de herramientas que otro día pasaré a documentar por si alguien no las conoce, pero ahora vamos a centrarnos en su funcionalidad para este proceso.

Por tanto, para abordar esta tarea, **una vez instalado el plugin podremos acceder al menú MMQGIS &gt; Create &gt; Hub Lines**.

Cabe señalar que **para este método sí necesitaremos dos tablas** (no valdrá, como hemos hecho, con simularlas) por lo que tendremos los datos duplicados. Lo ideal para ello es un _ESRI Shapefile_ de orígenes, y otro de destinos, que serán los que seleccionaremos en nuestro formulario.

![mmqgis-unir-ptos1](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/06/Captura-de-pantalla-2016-06-01-a-las-0.17.31.png)

MMQGIS: Puntos a líneas.

**El proceso se encargará de crear una salida de líneas que una nuestras dos capas de puntos.**Tan simple como eso.

### Conclusiones

### 

Si has hecho el mismo trabajo con ambos métodos habrás podido ver la diferencia de tiempo que hay entre ambos. Por eso me decanto por **el método PostGIS, ya que, aunque parezca algo más complejo, el tiempo de respuesta y los recursos que maneja serán mucho menores**.

Por tanto, podemos concluir este estudio diciendo que **de una manera bastante sencilla podemos representar una información puntual de un modo diferente, uniendo con líneas nuestros nodos, pero que, a pesar de su simplicidad, no pierde información**.

Este tipo de mapas de líneas se está popularizando en los últimos años en disciplinas como la visualización de datos o el “Big Data”, ya sea por los avances técnicos para gestionar datos, o incluso por el auge de recopilación de datos geolocalizados que estamos viviendo.

Así que **con esta manera puedes tener una aproximación de la potencialidad de QGIS o de QGIS+PostGIS como primera aproximación para realizar este tipo de estudios y unir puntos con líneas.** A partir de aquí, se podría perfectamente generar algunos mapas tan visuales como este, también hecho con QGIS.

![Mapa de líneas con QGIS - unir puntos con líneas](http://geoinnova.org/blog-territorio/wp-content/uploads/2016/06/li%CC%81neas_demo-1024x418.png)

Mapa de líneas con QGIS. Por Steven Lee.