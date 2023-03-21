# CONTROL DE VERSIONES

🚨 Este material fue creado por la Dra. Ana Julia Velez Rueda y Dra. Liliane Conteville para [Women in Bioinformatics and Data Science LA](https://github.com/WomenBioinfoDataScLA/Workshops) y se encuentra bajo 
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

¡Si te gustó dale una ⭐ y un `follow` a [nuestra organización](https://github.com/WomenBioinfoDataScLA)!

##  Introducción

[¿Qué es un sistema de control de versiones?](#control-de-versiones)
Un sistema de control de versiones es una herramienta que realiza un seguimiento de los cambios de un documento o directorio de forma automática, creando efectivamente diferentes versiones de nuestros archivos. Los sistemas de control de versiones comienzan con una versión base del documento y luego registran los cambios que realiza en cada paso del camino. Existen múltiples programas que nos permiten realizar un control de versiones de nuetsros prosyectos, pero en este tutorial veremos cómo utilizar [Git](https://git-scm.com/downloads), uno de los más populares en la actualidad.

Para comprender mejor qué hace Git se podría pensar que es un artista que intenta crear una película de [`stop motion`](https://es.wikipedia.org/wiki/Animaci%C3%B3n_en_volumen). Como bien sabrán, la construcción de estas películas requiere de muchas fotos que resgistren los movimientos de los personajes al detalle. Pensemos entonces que Git toma fotos instantáneas de los cambios durante la vida de un proyecto, para construir su película. Se podría pensar al proyecto entonces como un video: sobre el que se puede retroceder para comenzar en el documento inicial y reproducir cada estado o cambio que realizó, hasta llegar finalmente a su versión más reciente.

Cada registro de estos cambios se denomina `commit` y mantiene metadatos (referencias temporales y de autorías, etc) útiles sobre ellos. El historial completo de `commits` para un proyecto en particular y sus metadatos forman un `repositorio`. 

![Git commits img](https://raw.githubusercontent.com/WomenBioinfoDataScLA/Workshops/master/Git_%26GitHub/assets/%5BES%5DCONTROL_DE_VERSIONES_schema1.png)

Siguiendo con la analogía del video, podemos pensar cada `commit` como un fotograma en nuestro video, siendo este el historial completo de cambios de un archivo o directorio. Pero antes de tomar la foto, no sería mala idea preparar a nuestros personajes y apuntar la cámara adecuadamente para que sea capaz de capturar estos cambios adecuadamente. Entonces, al hacer `git add` lo que hacemos es especificar qué movimientos de los personajes quedarán registrados en la próxima foto (colocando las cosas en el área `index` de Git), algo así como gritar `cheeese` para que nadie salga con mala cara. Y luego, cuando hacemos `git commit` le indicamos a Git que es momento de tomar la foto y registrar de forma permanente los movimientos o cambios en el estado de nuestros personajes.

![Git areas](https://raw.githubusercontent.com/WomenBioinfoDataScLA/Workshops/master/Git_%26GitHub/assets/%5BES%5DCONTROL_DE_VERSIONES_git_areas.png)

En resumen, Git tiene un área de preparación `index` a la que podemos agregar elementos con `git add`. Los cambios no se documentan de forma permanentehasta que los confirmamos con `git commit`. Los cambios se gestionan como una unidad, al generar un `commit`, y quedan registrados al hacer `git commit`. Esto nos permite enviar grupos específicos de archivos al mismo tiempo o separados, según lo que deseemos.

📑 [**NOTA**]: Es muy importante especificar los cambios realizados en cada `commit`, esto nos ayudará a rastrear cualquier cambio al querer volver atrás.

Ahora bien ¿Qué pasa si alguno de los cambios que hicimos no nos sirve? Bueno, como en pasa en la vida real, las cosas pueden "malir sal" y vamos a necesitar volver a empezar. Pero por su puesto que no vamos a comenzar desde cero si llevamos buen rato trabajando en el proyecto.. ehem! ¡mejor dicho, en la película! Es por eso que quizás nos venga bien guardar las fotos que nos pueden servir en un futuro en una cajita que llamaremos `stash`, haciendo `git stash`. Pero ojo, que siempre se puede reutilizar aquello que dejamos `stasheado` haciendo `git stash apply`. 

## Git al infinito y más allá...

Git trabaja con un repositorio local que está en tu computadora, donde vas a ir agregando tus commits y uno remoto (en la nube) en el cual podes subir tus commits, compartirlos con alguien más o bajarte los commits que haya subido alguien.

Existen varios servicios para almacenar repositorios remotamente:

- [Github](https://github.com) 
- [Bitbucket](https://bitbucket.com)
- [Gitlab](https://gitlab.com/)

Para usarlos deberás registrarte y crear una cuenta. 

>
>🏅 Desafío I: Creá tu cuenta en [GitHub](https://github.com/) ¡Tené a mano tu nombre de usuarie y contraseña, lo vas a necesitar!
>
>🏅 Desafío II: Configurá e instalá tu [Git](https://github.com/WomenBioinfoDataScLA/Workshops/blob/master/Git_%26GitHub/%5BES%5D1.Git_and_GitHub_setup.md) en tu computadora!
>

Una vez creado un repositorio localmente, este podrá ser continuamente sincronizado con un repositorio remoto análogo al creado localmente. Esta sincornización se suele hacer desde el repositorio local utilizando los comandos:
- `git clone`: para clonar o descargar un repositorio remoto a nuestra computadora. Este comando se usa una única vez, una vez descargado se podrá actualizar usando los comandos detallados abajo.

- `git push`: para empujar los `commits` hechos localmente hasta el momento 

- `git pull`: para bajar los cambios que puedan existir en el repositorio remoto (`origin`).

Pero como `mejor que decir es hacer`, ¡vamos a ponernos manos a la obra con algunos ejercicios [prácticos](https://github.com/WomenBioinfoDataScLA/Workshops/blob/master/Git_%26GitHub/%5BES%5D2.Practica.md)!