#    ____ ___  _   _ _   _ _____ ____ _____     _  _
#  / ___/ _ \| \ | | \ | | ____/ ___|_   _|   | || |
# | |  | | | |  \| |  \| |  _|| |     | |_____| || |_
# | |__| |_| | |\  | |\  | |__| |___  | |_____|__   _|
#  \____\___/|_| \_|_| \_|_____\____| |_|        |_|
#
# Arte ascii hecho con PyFiglet (referirse a Importe de librerias)
# Este es el codigo fuente de un proyecto para mi universidad, t odo el codigo
# Ha sido escrito por mi (Katherine / Kanwi)
#
#  (c) COPYRIGHT 2022 Katherine C.M. / twitter: @Kanwi_
#  Este codigo esta licenciado sobre la licencia MIT (referise a LICENSE.txt)
#

# Importes de librerias
# Random: para la eleccion al azar del jugador
# Json: para el manejo del guardado de puntajes
# Os: Para el coloreo dentro de la terminal
# PyFiglet: Para el titulo principal
# - Fuente: https://github.com/pwaller/pyfiglet

import random
import json
import os
import pyfiglet

# Parte necesaria para usar el sistema de coloreado dentro de la terminal

os.system("")


# Clase creada para el sistema de deteccion de victoria
class vector2:
    def __init__(self, x_component, y_component):
        self.x = x_component
        self.y = y_component


# Lista de estilos para la terminal (colores, negrita, etc...)
class Style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


# Clase principal del jugador, donde guardamos su identificacion, la ficha con la que va a jugar
# el nombre y el puntaje maximo que consiguio, para el calculo final del puntaje
class Player:
    def __init__(self, iden):
        self.name = str(input(f"Hola jugador {Style.RED}{str(iden + 1)}{Style.RESET}, porfavor indica tu nombre: "))
        self.token = None
        self.iden = iden
        self.maxscore = 0


# Funcion para la asignacion de fichas a los jugadores
def tokencall(name):
    token = ""
    while not (token.capitalize() == "X" or token.capitalize() == "O"):
        token = str(input(
            f"Hola {Style.YELLOW}{name}{Style.RESET}, porfavor escoge una ficha entre {Style.RED}'X'{Style.RESET} y {Style.BLUE}'O'{Style.RESET}: "))
    return token.capitalize()


# Funcion principal del juego
def game():
    # Metodo para limpiar la consola
    os.system('cls' if os.name == 'nt' else 'clear')
    # Se declara la cuadricula del juego, llena en todas partes del caracter "•"
    rows, cols = (6, 7)
    grid = [["•" for i in range(cols)] for j in range(rows)]

    # Se define una lista vacia con 2 items que van a ser los jugadores
    player = [None, None]

    # Definimos 2 jugadores vacios, ya usando nuestra clase de jugador
    for i in range(2):
        player[i] = Player(i)
    # Le preguntamos al primer jugador su preferencia de ficha
    player[0].token = tokencall(player[0].name)

    # Asignamos al segundo jugador la ficha restante
    if player[0].token == "X":
        player[1].token = "O"
    else:
        player[1].token = "X"

    # Se imprime la primera parte del loop del juego donde se dice que ficha juega el jugador 2
    # y quien va a empezar el juego
    print(
        f"{Style.YELLOW}{player[1].name}{Style.RESET}, vas a jugar con la ficha {Style.MAGENTA}[{str(player[1].token)}]{Style.RESET} \n")
    print("Lanzando una moneda al aire para determinar quién inicia la partida...")
    current_player = random.randint(0, 1)
    print(f"la partida la inicia {Style.YELLOW}{player[current_player].name}{Style.RESET} \n")
    input("presiona enter para comenzar")

    # Definimos el metodo para imprimir el tablero cada vez que sea necesario
    def printboard():

        # Imprime la linea superior e inferior del tablero
        def printlines():
            print("         +", end="")
            for dum in range(len(grid[0])):
                print("-", end="")
            print("+")

        print("")
        print(f"          {Style.UNDERLINE}1234567{Style.RESET} ")
        # Imprime la linea que cubre el tablero al inicio
        printlines()
        for i in range(len(grid)):
            # Borde izquierdo
            print("         |", end="")
            for j in range(len(grid[0])):
                # Imprime el interior del tablero y determina los colores si la posicion actual
                # tiene una ficha
                if grid[i][j] == "X":
                    print(Style.RED + str(grid[i][j]) + Style.RESET, end="")
                elif grid[i][j] == "O":
                    print(Style.BLUE + str(grid[i][j]) + Style.RESET, end="")
                else:
                    print(grid[i][j], end="")
            # Borde derecho
            print("|")
        # Imprime la linea que cubre el tablero al final
        printlines()
        print("")
        if player[0].token == "X":
            print(
                f'      {player[0].name}: {Style.RED}{player[0].token}{Style.RESET} | {player[1].name}: {Style.BLUE}{player[1].token}{Style.RESET}')
        else:
            print(
                f'      {player[0].name}: {Style.BLUE}{player[0].token}{Style.RESET} | {player[1].name}: {Style.RED}{player[1].token}{Style.RESET}')
        return

    # Id de la ronda, se usa para terminal el juego una vez que el tablero este lleno
    roundid = 0

    # Metodo para determinar si el juego ha terminado por victoria
    def checkwin(row, column):
        # se revisan 8 direcciones al rededor de la ficha actual
        cases = [vector2(1, 1), vector2(1, 0), vector2(1, -1), vector2(0, -1),
                 vector2(-1, -1), vector2(-1, 0), vector2(-1, 1), vector2(0, 1)]
        direction_check = [0, 0, 0, 0]
        directions = []
        checkcases = []
        # en este loop descartamos aquellas posiciones que esten afuera del tablero
        for i in range(8):
            try:
                grid[row + cases[i].x][column + cases[i].y]
            except:
                pass
            else:
                if row + cases[i].x != -1 and column + cases[i].y != -1:
                    checkcases.append(cases[i])
                    directions.append(i % 4)
        # variable que nos da informacion de cuantas fichas estan en linea
        maxcheck = 0
        # Si en algun momento de la verificacion salimos del tablero, o encontramos una ficha que
        # es diferente que la del jugador actual, entonces vamos a descartar esta verificacion con
        # un Break, de lo contrario an~adimos a la direccion de verificacion
        for i in range(len(checkcases)):
            for j in range(1, 4):
                try:
                    grid[row + checkcases[i].x * j][column + checkcases[i].y * j]
                except:
                    break
                else:
                    if (row + checkcases[i].x * j == -1) or (column + checkcases[i].y * j == -1):
                        break
                    if grid[row + checkcases[i].x * j][column + checkcases[i].y * j] != player[current_player].token:
                        break
                    else:
                        direction_check[directions[i]] += 1
                        continue
            # si tenemos 3 o mas fichas iguales a las del jugador en la direccion
            # que estamos verificando entonces tenemos un 4 en linea
            if direction_check[directions[i]] >= maxcheck:
                maxcheck = direction_check[directions[i]]
        # si tenemos un 4 en linea entonces vamos a devolver true
        return maxcheck >= 3, maxcheck

    # son 2 variables que sirven para informacion al final del juego
    game_won = False
    winning_player = None

    # Loop principal del juego, mientras el tablero no este lleno o nadie halla ganado
    while roundid <= (len(grid) * len(grid[0])) and not game_won:
        os.system('cls' if os.name == 'nt' else 'clear')
        # Variable de input del jugador y la columna que va a jugar
        myinput = None
        colum = 0
        # Primera impresion del tablero
        printboard()
        # Verificamos que el input sea valido y asignamos un valor de columna a jugar
        while myinput is None:
            print(f"{Style.GREEN}{player[current_player].name}{Style.RESET}, indica un número de columna o \nintroduce "
                  f"[{Style.YELLOW}S{Style.RESET}] para tentar a la suerte: ", end="")
            myinput = str(input())
            if myinput.isnumeric():
                if 1 <= int(myinput) < 8:
                    colum = int(myinput)
                    break
                else:
                    continue
            elif myinput.capitalize() == "S":
                colum = random.randint(1, 7)
                while grid[0][colum - 1] != "•":
                    colum = random.randint(1, 7)
                break
            else:
                continue
        # verificamos que la columna este llena, si es el caso entonces se repite el turno actual
        if grid[0][colum - 1] != "•":
            input(f"Esta columna esta llena {Style.BLUE}(presiona enter para continuar){Style.RESET}: ")
            continue
        # Insertamos la ficha del jugador en su posicion y verificamos si esta ficha hizo que el
        # jugador ganara
        for i in range(len(grid)):
            if grid[len(grid) - i - 1][colum - 1] == "•":
                grid[len(grid) - i - 1][colum - 1] = player[current_player].token
                print(player[current_player].token)
                won, localscore = checkwin(len(grid) - i - 1, colum - 1)
                if localscore > player[current_player].maxscore:
                    player[current_player].maxscore = localscore
                if won:
                    game_won = True
                    winning_player = current_player
                break
        # Avanzamos al siguiente jugador y cambiamos de ronda
        current_player = (current_player + 1) % 2
        roundid += 1

    # Metodo que va a calcular los puntos en base a los espacios restantes y a la maxima cantidad de
    # fichas que el jugador oponente pudo juntar
    #
    # 1 punto por cada espacio libre de la fila superior, 2 por la de abajo y asi hasta la ultima
    # se resta 20% si el oponente pudo juntar 3 fichas y 10% si pudo juntar solo 2
    def checkscore(points):
        score = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "•":
                    score += i
        score -= 0.1 * points * score
        score = round(score)
        return score

    # El metodo que maneja los puntajes y el archivo de guardado (cfsd.json) o "connect four save data.json"
    # Revisa si el archivo existe, de lo contrario crea uno vacio, despues verifica que el ultimo puesto del
    # Podio sera mayor que el puntaje del juego, de no ser asi, este sera cambiado por el puntaje actual
    # y luego reordenamos las listas para obtener el nuevo podio
    # fuente del codigo de reordenado
    # https://stackoverflow.com/questions/9764298/how-to-sort-two-lists-which-reference-each-other-in-the-exact-same-way
    def score_handling(score, name):
        # checking if the save file exists
        try:
            savefile = open('cfsd.json', 'r')
            json.loads(savefile.read())
        except:
            print("Archivo de guardado inexsistene!, creando uno...")
            savefile = open('cfsd.json', 'w')
            json.dump([[0, 0, 0, 0, 0, 0], ["", "", "", "", "", ""]], savefile)
            savefile.close()

        save_file = open('cfsd.json', 'r')
        with open('cfsd.json', 'r') as j:
            save_data = json.loads(j.read())
        save_scores = save_data[0]
        save_names = save_data[1]
        save_file.close()

        if score > save_scores[0]:
            save_scores[0] = score
            save_names[0] = name

            zipped = list(zip(save_scores, save_names))
            zipped.sort()

            res_score = [i for (i, s) in zipped]
            res_names = [s for (i, s) in zipped]

            print("Felicidades!, tu puntaje esta en el podio. \n")
            save_file = open('cfsd.json', 'w')
            json.dump([res_score, res_names], save_file)
            save_file.close()

        with open('cfsd.json', 'r') as j:
            save_data = json.loads(j.read())
        save_scores = save_data[0]
        save_names = save_data[1]
        save_file.close()

        # Imprimimos el podio
        print('Mejores puntajes:')
        for i in range(6):
            print(f'{i + 1}. {save_names[5 - i]}: {Style.YELLOW}{save_scores[5 - i]}{Style.RESET}')

    os.system('cls' if os.name == 'nt' else 'clear')
    printboard()
    # Fin del juego, si el jugador gana se muestra el podio, su puntaje y si este puntaje esta dentro del
    # podio, ademas se pregunta si se desea jugar denuevo
    if game_won:
        print(f'Felicidades {player[winning_player].name}!, Has ganado el juego.\n')
        losing_player = (winning_player + 1) % 2
        winning_score = checkscore(player[losing_player].maxscore)
        print(f'Tu puntaje es de: {Style.YELLOW}{winning_score}{Style.RESET} puntos!')
        score_handling(winning_score, player[winning_player].name)
    playagain = None
    while playagain is None:
        print(f"Desea jugar otra vez? [{Style.GREEN}Y{Style.RESET}]/[{Style.RED}N{Style.RESET}]: ", end="")
        sto1 = input()
        if sto1.capitalize() == "Y":
            playagain = True
        elif sto1.capitalize() == "N":
            playagain = False
        print("")
    if playagain:
        game()


# La pantalla de inicio del juego, donde se presenta el nombre del juego y mi nombre (Katherine), la creadora
starting_logo = pyfiglet.figlet_format("CONNECT-4")
print(Style.MAGENTA, end="")
print(starting_logo)
print(Style.RESET, end="")
print("Creado por: Katherine (@Kanwi_) ©2022 Todos los derechos reservados")
input("Presiona enter para empezar")
game()
