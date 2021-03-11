# *Introducción a Python*

En este recorrido aprenderemos los conceptos básicos de programación y la sintáxis de [Python](https://www.python.org.ar/). Para ello vas a necesitar instalarte [Python](http://ufq.unq.edu.ar/sbg/archivos/guias_talleres/Guia_Instalacion_Python_2020.pdf) y algún [IDE](https://code.visualstudio.com/) que te sea útil para programar. 

¡Agradecemos a al Proyecto de Extensión [La Bioinformática Va a La Escuela](http://ufq.unq.edu.ar/sbg/education.html) por prestarnos su material, que tomaremos como base para las presentes guías! 🤗



# Guias de Trabajo
  * [1. Pensamiento computacional](#1-PC)
  * [1. Internte](#1-interntet)

[1. Pensamiento computacional](#1-PC) 🧠

Si nunca programaste tal vez la programación pueda parecerte algo muy abstracto o lejano, hasta puede que te de miedo intentar aprender a programar, pero lo cierto es que las habilidades que utilizamos para programar son por demás cotidianas. ¿No me crees? ¡Vamos a hacer una prueba!

Pensemos en una actividad cotidiana como la de preparar mate 🧉 (#ArgentinianMood) ¡Una actividad muy programadoril!. Al realizar este ritual tan Argento, sin darte cuenta estás aplicando una serie de pasos lógico-prácticos simlares a los que se utilizan para programar: 
    - Primero, definir el problema que queres resolver. En nuestro caso: preparar mate 🧉 
    - Una vez definido el problema debemos plantear los pasos a seguir de una manera sencilla (no es sería recomendable intentar preparar mate patas para arriba). Empezamos buscando el mate y la yerba. Luego verificamos si el mate está vació o lleno, en el caso de estar vacío procedemos a llenarlo. Si está lleno, buscamos la primer maceta que tengamos a mano para vaciar su contenido y llenarlo con yerba.

Ahora que tenemos un idea de los pasos a seguir para resolver el problema, vamos a escribir nuestra guía para preparar un mate en 20 mil simples pasos (mentira solo son 8! 😝):
    Paso 1) Seleccionar el mate
    Paso 2) Buscar el yerbero
    Paso 3) Verificar si el mate está vacío:
        Momento decisivo:
            Paso 4) Si el mate está vacío, llenarlo con la yerba del yerbero.
            Paso 5) Si el mate está lleno:
                    Paso 7) Vaciarlo en una maceta
                    Paso 8) Llenarlo con la yerba del yerbero.

Hemos podido hacer un recorrido simplificado de la actividad, con las posibles situaciones a las que nos podemos enfrentar y sus soluciones posibles, para resolver el problema que nos habíamos propuesto: preparar mate 🧉

Veamos como se vería nuestra guía para preparar mate escrita en un lenguaje similar al que una computadora puede entender (pseudocódigo):
    
    mate = mate seleccionado
    yerbero = lata de yerba
    maceta = maceta con cactus del balcón 

    if mate está vacio:
        llenar mate con yerba del yerbero
    de lo contrario:
        vaciar mate en maceta
        llenar mate con yerba del yerbero

Moraleja, programar es como hacer mate...Bueno, no taaanto ¡pero casi! 😝

> 🧗‍♀️Desafío I: ¿Qué pasos nos faltaron? ¿Podes pensar otras posibles situaciones que no estemos contemplando (como por ejemplo que no haya yerba en el yerbero)?  Agregá a la guía para preparar mate(script) los pasos, problemas posibles y las soluciones que se te ocurran en sentencias u ordenes sencillas (ejemplo; verificar si hay yerba en el yerbero. Si no hay agregar, si hay lenar el mate)  

