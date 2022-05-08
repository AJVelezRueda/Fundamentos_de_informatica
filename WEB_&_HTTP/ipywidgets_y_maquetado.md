# Maquetado Web

🚨 Este material fue creado por Ana Julia Velez Rueda y como todo el repositorio se encuentra bajo licencia 

[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg



### Índice

* [1. HTML](#1-HTML)
* [2. Anatomía de un documento HTML](#2-partes_html)


## [1. HTML](#1-html)

Para presentar los datos provenientes del servidor del lado del cliente, se utiliza HTML, que no es un lenguaje de programación, sino más bien un sitema de eqtiqueas que está pensado para mostrar contenido. 

HTML es un acrónimo de Hyper Text Markup Language, o lo que es lo mismo, Lenguaje de Marcado de Hyper Texto. El Hyper Texto tampoco es sólo texto… Entre los elementos del hiper texto podemos encontrar videos, imágenes, sonidos, etc.

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

## [2. Anatomía de un documento HTML](#2-partes_html)

Un documento HTML está formado por partes:

 - Una línea que contiene información sobre la versión de HTML (no siempre),
 
 - Una cabecera (delimitada por el elemento HEAD)

 - Un cuerpo, con el contenido del documento (delimitado por el elemento BODY).

Y todo el documento tiene que ir entre las etiquetas `<html></html>` e inicia con la etiqueta `<!DOCTYPE html>`