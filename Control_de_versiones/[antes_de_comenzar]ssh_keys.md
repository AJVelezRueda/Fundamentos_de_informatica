🚨 Este material fue creado por la Dra. Ana Julia Velez Rueda y Dra. Liliane Conteville para [Women in Bioinformatics and Data Science LA](https://github.com/WomenBioinfoDataScLA/Workshops) y se encuentra bajo 
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

¡Si te gustó dale una ⭐ y un `follow` a [nuestra organización](https://github.com/WomenBioinfoDataScLA)!

## Verificación de Cuenta de GitHub via SSH

Vamos a autenticar tu cuenta, para poder crear una conexión entre el `Git` de local y tu cuenta de `Github`.

Primero, verifiquemos si ya tenes una claves SSH en tu máquina:

```bash
ls -al ~/.ssh
```

Este comando arroja un error del estilo de `~/.ssh no existe`, quiere decir que no tenés claves `SSH`, por lo que debemos crear una nueva con el siguiente comando:

```bash
#Tu dirección de correo electrónico debe estar entre comillas
ssh-keygen -t rsa -C "<tu email>"
```

Cuando aparezca el mensaje `Ingrese el archivo en el que guardar la clave`, presioná la tecla `Enter` para aceptar la ubicación predeterminada y para guardar el archivo con la clave. Luego se te pedirá que `Ingreses la frase de contraseña`, y deberás ingresas una clave segura en la terminal.

Entre los mensajes que se mostrarán en la terminal, uno indicará dónde se guardó la clave. Buscá algo como:

```
Your public key has been saved in <ruta al archivo .pub>
```

Ahora abrí el archivo que contiene la clave, **seleccione** todo su contenido y **copialo** en tu **portapapeles**.

```bash
cat <ctura al archivo donde está la clave> 
```

¡Listo! 🥳 Ahora solo necesitamos agregar esta clave a tu cuenta de Github. Para hacer esto, andá a [la configuración de su cuenta de github](https://github.com/settings/profile), hacé click en el botón  `Claves SSH y GPG` que se encuentra a la izquierda, luego `Nueva clave SSH` que se encuentra a la derecha. Agregá una etiqueta a la clave (podés usar algo como "Mi computadora personal") y luego pegá la clave que tenés en portapapeles en la ubicación indicada.

![](https://raw.githubusercontent.com/WomenBioinfoDataScLA/Workshops/master/Git_%26GitHub/assets/paste_ssh_es.png)

🌐 Ahora probemos la conexión, para ver si todo salió bien. En la terminal, ejecutá:

```bash
ssh -T git@github.com
```

Deberías ver una advertencia como esta:

```
> The authenticity of host 'github.com (IP ADDRESS)' can't be established.
> RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
> Are you sure you want to continue connecting (yes/no)?
```

Escribí `yes`. Si dice algo como lo siguiente, funcionó:

```
Hi <su login>! You've successfully authenticated, but Github does not provide shell access.
```
