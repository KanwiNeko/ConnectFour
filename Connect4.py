import random
import os

# for coloring inside the code
os.system("")


class vector2:
    def __init__(self, x_component, y_component):
        self.x = x_component
        self.y = y_component


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


class Player:
    def __init__(self, iden):
        self.name = str(input(f"Hola jugador {str(iden + 1)}, porfavor indica tu nombre: "))
        self.token = None
        self.iden = iden


def tokencall(name):
    token = ""
    while not (token.capitalize() == "X" or token.capitalize() == "O"):
        token = str(input(f"Hola {name}, porfavor escoge una ficha entre 'X' y 'O': "))
    return token


def game():
    os.system('cls' if os.name == 'nt' else 'clear')
    rows, cols = (6, 7)
    grid = [["•" for i in range(cols)] for j in range(rows)]

    player = [None, None]

    for i in range(2):
        player[i] = Player(i)
    player[0].token = tokencall(player[0].name)

    if player[0].token == "X":
        player[1].token = "O"
    elif player[0].token == "O":
        player[1].token = "X"

    print(f"{player[1].name}, vas a jugar con la ficha [{str(player[1].token)}] \n")
    print("Lanzando una moneda al aire para determinar quién inicia la partida...")
    current_player = random.randint(0, 1)
    print(f"la partida la inicia {player[current_player].name} \n")

    def printboard():
        def printlines():
            print("         +", end="")
            for i in range(len(grid[0])):
                print("-", end="")
            print("+")

        print("")
        print("          1234567 ")
        # print the line on the top of the board
        printlines()
        for i in range(len(grid)):
            print("         |", end="")
            for j in range(len(grid[0])):
                if grid[i][j] == "X":
                    print(Style.RED + str(grid[i][j]) + Style.RESET, end="")
                elif grid[i][j] == "O":
                    print(Style.BLUE + str(grid[i][j]) + Style.RESET, end="")
                else:
                    print(grid[i][j], end="")
            print("|")
        # print the line on the bottom of the board
        printlines()
        print("")

    roundid = 0

    def checkwin(row, column):
        cases = [vector2(1, 1), vector2(1, 0), vector2(1, -1), vector2(0, -1),
                 vector2(-1, -1), vector2(-1, 0), vector2(-1, 1), vector2(0, 1)]
        checkcases = []
        for i in range(8):
            try:
                grid[row + cases[i].x][column + cases[i].y]
            except:
                pass
            else:
                if row + cases[i].x != -1 and column + cases[i].y != -1:
                    checkcases.append(cases[i])
        maxcheck = 0
        for i in range(len(checkcases)):
            currentcheck = 0
            for j in range(1, 4):
                try:
                    grid[row + checkcases[i].x*j][column + checkcases[i].y*j]
                except:
                    break
                else:
                    if (row + checkcases[i].x*j == -1) or (column + checkcases[i].y*j == -1):
                        break
                    if grid[row + checkcases[i].x*j][column + checkcases[i].y*j] != player[current_player].token:
                        break
                    else:
                        currentcheck += 1
                        continue
            if currentcheck > maxcheck:
                maxcheck = currentcheck
        return maxcheck == 3

    game_won = False
    winning_player = None

    while roundid <= (len(grid) * len(grid[0])) and not game_won:
        os.system('cls' if os.name == 'nt' else 'clear')
        myinput = None
        colum = 0
        printboard()
        while myinput is None:
            print(f"{Style.GREEN}{player[current_player].name}{Style.RESET}, indica un número de columna o introduce "
                  f"[S] para tentar a la suerte: ", end="")
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
        if grid[0][colum - 1] != "•":
            print("Esta columna esta llena (presiona enter para continuar): ")
            a = input()
            continue
        for i in range(len(grid)):
            if grid[len(grid) - i - 1][colum - 1] == "•":
                grid[len(grid) - i - 1][colum - 1] = player[current_player].token
                if checkwin(len(grid) - i - 1, colum - 1):
                    game_won = True
                    winning_player = current_player
                break
        current_player = (current_player + 1) % 2
        roundid += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    printboard()
    if game_won:
        print(f'Felicidades {player[winning_player].name}!, Has ganado el juego.')
    playagain = None
    while playagain is None:
        print("Desea jugar otra vez? [Y]/[N]: ")
        sto1 = input()
        if sto1.capitalize() == "Y":
            playagain = True
        elif sto1.capitalize() == "N":
            playagain = False
    if playagain:
        game()


game()
