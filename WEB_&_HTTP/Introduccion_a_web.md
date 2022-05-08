# Tutorial WEB
>
> En este recorrido:
> - se basa en el material [http-tutorial](https://github.com/AJVelezRueda/http-tutorial/tree/master/tutorial/es) de los autores Franco Leonardo Bulgarelli y Ana Julia Velez Rueda
>
> - Retoma el material teórico [Introducción a la arquitectura Web](https://docs.google.com/document/d/1LBqAhXPzn-aeN5BIRZBmIrU5RKiYvySyWH-2Jkn-kJw/edit#heading=h.kx1xmbyu1do6) generado por Franco Leonardo Bulgarelli
>

# Introducción a WEB
[Contenido del recorrido](#1-Web)
  * [1. Internet](#1-interntet)
  * [2. La Web](#2-web)
  * [3. Introducción al concepto de CLoud Computing](#3-Cloud-computing)
  * [4. Arquitectura Web](#4-arquitectura-web)
  * [5. Protocolos de comunicación](#5-protocolos)

## [1. Internet](#1-interntet)

Internet se podría definir como la red de redes de computadoras, conectadas por medio de un cableado físico que permite intercambiar información entre todos sus usuarios. 

Para acceder al servicio que ofrece la información, debemos tener dos programas que se ejecutan en dos computadoras diferentes y que nos permiten compartir recursos. 

A la computadora que ejecuta el programa que proporciona el recurso o información se la denomina **servidor** y a la computadora que consume un recurso o información se la denomina **cliente**. En la computadora del cliente se ejecutará entonces el programa que le permite utilizar el recurso o leer la información.

Pero ¿Qué tipo de recursos pueden brindarse o consimirse a través de internet? Por medio de Internet podemos enviar mensajes, programas ejecutables, archivos de texto, consultar bases de datos, etc.

## [2. La Web](#2-web)
La Web en particular, diminutivo de World Wide Web, es un conjunto de páginas interconectadas por las cuales podemos navegar.

Estas páginas web están pensadas para consumir contenido hipertextual, es decir  contenido que contiene vínculos o enlaces a otros contenidos.

## [3. Introducción al concepto de CLoud Computing](#2-Cloud-computing)

La computación en la nube o Cloud Computing es el consumo o prestación bajo demanda de recursos tecnologicos a través de Internet. 

En lugar de comprar y mantener servidores y centros de datos físicos(es decir una super duper máquina en tu casa), podés consumir los servicios tecnológicos, como potencia informática, almacenamiento y bases de datos, según te sea necesario, en el momento que te sea necesario, de un proveedor.

## [4. Arquitectura Web](#4-arquitectura-web)

Los sistemas Web hoy en día presentan en genarl una arquitectura distribuida, es decir que sus componentes están distribuidos en dos tipos de nodos: **clientes** (muchos) y **servidores** (uno). En esta arquitectura, llamada `cliente-servidor`, los clientes se comunican con el servidor siguiendo un protocolo de pedido-respuesta en el que: 

* Un cliente hace un pedido, 
* El servidor procesa el pedido y responde.
* El cliente se encarga de presentar (renderizar) la respuesta al usuario final

Esta comunicación ocurre a través de redes Intranets o la misma Internet, empleando un protocolo llamado HTTP, sobre el cuál hablaremos en el punto siguiente.

Entonces en la arquitectura web `cliente-servidor`, los servidores son quienes almacenan y proveen la información o recursos dados, y los clientes son responsables de presentar la información al usuario, empleando tecnologías específicas de la Web. 


>
> 🤔 Para pensar: ¿qué tecnologías se usan en la Web? ¿En qué se desarrolla un cliente? ¿Y un servidor?
>
>📚 Para indagar antes de empezar: ¿Cuál es la diferencia entre un sitio Web y una API web?


## [5. Protocolos de comunicación](#5-protocolos)

¿Alguna vez te preguntaste cómo es que logramos comunicarnos los seres humanos? ¿Cómo es que las palabras pueden estructurarse en conversaciones ordenadas? Bueno tal y como explica el Dr. Juan Eduardo Bonnin, <a href="https://www.youtube.com/watch?v=jrA70HwWnts&t=9s">en su video</a>, los seres humanos somos capaces de estructurar las palabras, y estas en oraciones que devienen en conversaciones. En este proceso se pone en juego no solo cuestiones ficiológicas, sino también cuestiones culturales y personales, como: la lengua, las normas sociales, los valores culturales, los intereses y propósitos individuales. Por tanto, lo que pensamos como un simple intercambio de palabras, se convierte en una actividad compleja, matizada con el ritmo de todo esta información extra...o meta 😝

Los protocolos, como verás, forman parte de nuestras vidas más de lo que pensábamos. Y estos pueden variar según el entorno en el que nos movemos. Cada ámbito posee sus propias reglas para la comunicación. No nos expresamos de igual modo cuando estamos en un recital, que cuando estamos en la facultad ¿No? 🙏

Este conjunto de reglas de comunicación, implícitas o explícitas, se denomina protocolo y en Internet hay uno específico para establecer la comunicación entre servidores y clientes. Este protocolo fue creado para la transferencia de archivos hipertextuales y se llama justamente HTTP, por las siglas en inglés de protocolo de transferencia de hipertexto (HyperText Transfer Protocol).


📝 [NOTA] Sobre esto hablaremos en el recorrido de [HTTTP y REST](https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/WEB_%26_HTTP/HTTP_%26_REST.md)

