# Connect-4
### El clasico juego de [Connect Four] de toda la vida, en CLI, escrito en [python]

Programado por Katherine / Kanwi, [Stats].

## Sobre el juego:
- es una rendicion moderna del conocido juego [Connect Four], que se juega en la interfaz de consola de tu dispositivo.
- esta disponible en Windows, MacOS y en Linux.
- el juego esta disponible unicamente en español.

## Instalación

Para instalar el juego tienes que descargar el archivo correspondiente
de la pestaña de [Releases] y escoge el adecuado respecto a tu sistema operativo
y busca la ultima.

- Windows: `C4v{version}.zip`
- MacOS: `C4v{version}.zip`
- Linux: `C4v{version}.tar`

una vez descargado, descomprime el archivo en la locación de tu preferencia y
ejecuta el archivo llamado `connect4` en Linux y MacOS, o `connect4.exe` en Windows.

## Objetivo del proyecto

Es la entrega final de un curso de universidad donde el objetivo era recrear exactamente este juego
con la reglamentación dada, me reservo el derecho de brindar mas detalles para manterner mi imagen privada.

## Instrucciones de juego

Al comenzar vas a encontrar una pestaña con el nombre del juego y mi nombre, para empezar debes presionar `enter` o el boton que tengas configurado en tu terminal para enviar un comando.

### Inicio del juego

Para iniciar tienes que ingresar los nombres de los 2 jugadores que van a participar y despues con que token va a jugar el jugador 1, despues es posible enviar (presionar `enter`) para comenzar el juego.

### Durante el juego

El juego funciona por turnos, en la pantalla estara disponible el jugador actual, el tablero de juego y que ficha corresponde a cada jugador.

puedes:
- escoger una de las 7 columnas 
- usar el comando `$ s` o `$ S` para jugar una columa al azar 
la columa que escojas determinara donde caera tu ficha.

### Para ganar

para ganar, tienes que juntar por lo menos 4 fichas en linea una sola vez, independiente de la dirección de la linea, tambien puede acabar el juego si el tablero se llena completamente; una vez el juego termina, se mostrara el puntaje del jugador ganador, y el podio de puntajes.

### Sobre los archivos de guardado

El juego al terminar creara un archivo de guardado `cfsd.json` que va a contener los datos de los mejores puntajes, y este va a ser creado en la carpeta donde el juego principal este instalado.

## Mantenimiento y Contribuciones

Es posible que el juego vuelva a ser actualizado para el arreglo de bugs, pero no existen planes actualmente de seguir actualizando el juego, si deseas contribuir estas bienvenidx a crear un fork propio y crear tus propios cambios.

Quedas completamente bienvenidx a reportar erorres en la pestaña de `issues` que estos seran revisados.

### PROTEJAMOS LAS VIDAS TRANS 🏳️‍⚧️ - Katie

[comment]: # (referencias:)

[Stats]: <https://github.com/anuraghazra/github-readme-stats>
[Releases]: <https://github.com/KanwiNeko/ConnectFour/releases>
[python]: <https://www.python.org/psf/>
[Connect Four]: <https://shop.hasbro.com/es-419/product/the-classic-game-of-connect-4/80FB5BCA-5056-9047-F5F4-5EB5DF88DAF4>
