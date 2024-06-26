# Maquetado Web

🚨 Este material fue creado por **Ana Julia Velez Rueda** y como todo el repositorio se encuentra bajo licencia 

[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


### Índice

* [1. HTML Init](#1-HTML)
* [2. Anatomía de un documento HTML](#2-partes_html)
* [3. Sintaxis HTML](#3-sintaxis-html)
* [4. Semántica](#4-semantica)
* [5. Estilado](#5-estilado)
* [6. Ahora con estilo](#6-estilos)

## [1. HTML Init](#1-html)

Para presentar los datos provenientes del servidor del lado del cliente, se utiliza HTML, que no es un lenguaje de programación, sino más bien un sitema de eqtiqueas que está pensado para mostrar contenido. 

HTML es un acrónimo de Hyper Text Markup Language, o lo que es lo mismo, Lenguaje de Marcado de Hyper Texto. El Hyper Texto tampoco es sólo texto… Entre los elementos del hiper texto podemos encontrar videos, imágenes, sonidos, etc.

## [2. Anatomía de un documento HTML](#2-partes_html)

Un documento HTML está formado por partes:

 - Una línea que contiene información sobre la versión de HTML (no siempre),
 
 - Una cabecera (delimitada por el elemento HEAD)

 - Un cuerpo, con el contenido del documento (delimitado por el elemento BODY).

Y todo el documento tiene que ir entre las etiquetas `<html></html>` e inicia con la etiqueta `<!DOCTYPE html>`


## [3. Sintaxis HTML](#3-sintaxis-html)

La sintaxis de HTML basada en etiquetas, le permite al browser interpretar como mostrar el contenido. Típicamente, las etiquetas se escriben entre `<>` y generalmente delimitan el contenido que están identificando. 

Se suelen abrir `<etiqueta>` y cerrar luego de escribir el contenido agregando a la misma etiqueta una barra invertida `</etiqueta>`:

```html
<html>
		contenido
</html>
```

Sin embargo, algunas etiquetas no tienen etiqueta de cierre con la barra invertida, son únicas:

```html
<img src="images/las_de_sistemas.png" alt=””>
``` 

Existen, además, atributos para las etiquetas que le agregan una funcionalidad extra a la etiqueta que lo contiene:

```html
<p style="font-size: 18px;"> Este es mi texto con estilo propio</p>
```

Cómo vimos anteriormente, la cabecera usa la etiqueta `<head>` que contiene información sobre el documento actual, como el título, palabras clave que utilizan los motores de búsqueda, y otros datos que no se consideran parte del contenido del documento ¡Tal y como pasa con los pensamientos en nuestra cabeza, que no son visibles a los demás, el contenido del `<head>` no se visualizan en el navegador! 

La etiqueta `<body>` contendrá el contenido particular de esta página. Es decir, todo lo que deseamos mostrar y es visible al usuario deberá estar contenido dentro de la etiqueta `<body>`.

>
> 🧗🏻‍♀️ Desafio I:  Buscá qué otras etiquetas existen y para qué sirven
>
> 🧗🏻‍♀️ Desafio II :Creá un archivo de texto con la herramienta que tengamos a mano (visual code, editor de texto, bloc de notas,etc) y lo guardamos con el nombre “mi_pagina” con extensión “.html” : “mi_cv.html”
>
> Iniciamos el documento con las etiquetas como sigue:
>
```html
<!DOCTYPE html>
<head>
 		<meta charset="UTF-8">
		<title>Document</title>
</head>
<body>
</body>
</html>
```
>
> 🤔 PARA PENSAR: ¿Cómo podés hacer para visualizar este archivo?
>


## [4. Semántica](#4-semantica)


La semántica hace referencia al significado de las palabras y al significado de las oraciones. HTML nos brinda etiquetas para reforzar el significado de la información de nuestra página web.

El HTML semántico no se trata sólo de utilizar las nuevas etiquetas semánticas, sino de utilizar las etiquetas correctas para cada elemento o sección de tu página web, para que sea fácil de navegar para todos los usuarios.

Algunas de las etiquetas semánticas más usadas son:

```html
<section></section>
<figure></figure>
```

>
> 🧗🏻‍♀️ Desafio IV:  Buscá qué otras etiquetas semánticas y no semánticas existen
>

¿Y cuáles son las ventajas de escribir de este modo nuestro código HTML? Bueno, para empezar hace el código más mantenible, es decir que se puede comprender más fácilmente sus estructuras y de este modo puede solucionarse más fácilmente cualquier problema. Por otro lado: 
 
 - Hace más fácil de encontrar tu página en las búsquedas de Google
 
 - Hace a tu sitio más accesible, ya que permite a los lectores de pantalla leer cada elemento correctamente

## [5. Estilado](#5-estilado)


Los documentos HTML pueden ser estilados, mediante el uso del lenguaje **CSS**. Estos estilos suelen escribirse en lo que se conocen como **hojas de estilo en cascada** (por la sintáxis de **CSS**). En estas se escriben los estilos que se deben aplicar a diferentes las diferentes partes del documentos HTML, es decir a las diferentes etiquetas. Es decir que el estilado de los documentos se escribe de manera centralizada (la fuente, el formato y la visualización) y “en cascada” (porque se leen de arriba hacia abajo).

🤔 ¿Pero cómo se aplica a mi documento HTML?  Para que estos estilos tengan efecto, se debe realizar una conexión con el documento HTML agregando en el `<head>` en enlace a la hoja de estilos:

```html
<link rel="stylesheet" href="style.css">
```

En nuestro archivo **CSS** podemos listar los elementos HTML que hemos usado e indicamos cómo queremos que se vean. 

Hay muchas formas de apuntar a elementos que queremos, y las clases HML son una de esas formas. Las **clases HTML** son atributos que podemos agregar a elementos para referirnos a ellos. Una vez que un elemento tiene un nombre de clase, podemos usarla en nuestro CSS. Para ello debemos agregar a laetiqueta dada el atributo `class`

```html
<section class="clase-etiqueta"> </section>
```

Y luego podremos estilar dicha etiqueta, haciendo referencia a la misma en el archivo css, escribiendo:

```css
.clase-etiqueta {
 background-color: blue;
}
```

Como verás además del nombre `clase_etiqueta`, para determinar que se trata de un nombre de clase agregamos `.` delante. Pero momento, tambien podemos estilar en cascada lo que se encuentra dentro de otra etiqueta. Imaginemos que ahora agregamos una foto a nuestra página:

```html
<section class="clase-etiqueta"> 
  <img alt='mi-imagen' src='mi_imagen.png'>
</section>
```

Podríamos entonces estilar dando un ancho (width) y alto (height) a la imagen dentro de la sección de clase `clase_etiqueta` de la siguiente forma:

```css
.clase-etiqueta img{
    width: 250px;
    height: 150px;
}
```

>
> 🤔 PARA PENSAR: ¿Qué significa `px`?
>


En este caso especificamos la clase de la sección madre y el tipo de etiqueta interior que deseamos estilar separada por un espacio.

## [6. Ahora con estilo](#6-estilos)

Veamos algunos ejemplos de estilados que nos permite hacer `CSS`.

Es muy común querer estilar las tipografía de los textos que se encuentran en nuestro documento. Para ello podemos usar la propiedad `font-family`.

Es una buena práctica usar además de la tipografía queremos mostrar, definiendo esta primero, y luego otras tipografías alternativas ( la misma línea, y separadas por comas después de las comillas). 

De este modo, en caso de que no exista o no se pueda cargar la tipografía deseada se podrán usar las alternativas sugeridas

```css
 body {
       font-family: 'Lato', sans-serif, arial;
   }
```

>
> 🧗🏻‍♀️ Desafio III:  Buscá qué otros atributos existen y dale estilo al documento HTML creado en el Desafío II 
>

