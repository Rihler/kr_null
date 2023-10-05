class Field(object):
    def __init__(self):
        self.field = [["|A1|", "|A2|", "|A3|"], ["|B1|", "|B2|", "|B3|"], ["|C1|", "|C2|", "|C3|"]]
        self.cords = {
            "A1": [0, 0],
            "A2": [0, 1],
            "A3": [0, 2],
            "B1": [1, 0],
            "B2": [1, 1],
            "B3": [1, 2],
            "C1": [2, 0],
            "C2": [2, 1],
            "C3": [2, 2],
        }
        self.sym ={
            "A1": 0,
            "A2": 0,
            "A3": 0,
            "B1": 0,
            "B2": 0,
            "B3": 0,
            "C1": 0,
            "C2": 0,
            "C3": 0,
        }

    def print_field(self):
        print('-' * 14)
        for i in range(3):
            for j in range(3):
                print(self.field[i][j], end=" ")
            print("\n" + '-' * 14)

    def change(self, sym, x):
        while x not in self.cords.keys():
            x = input("Такой координаты нет, введите те, которые доступны на поле: ")
        if self.sym[x] != 'O' or self.sym[x] !="X":
            pass
        else:
            while self.sym[x][-1] == 'O' or self.sym[x][-1] == "X":
                x = input("Данная клетка занята, выберите другую: ")
                while x not in self.sym.keys():
                    x = input("Такой координаты нет, введите те, которые доступны на поле: ")
        self.sym[x] = sym
        x1 = self.cords[x][0]
        y1 = self.cords[x][1]
        self.field[x1][y1] = f"|{sym}|"

def change_sym(name):
    print(f"Выбор символа для {name}")
    ch = ["1", "2"]
    syms = input("1. X\n2. O\n")
    while syms not in ch:
        print("Данного выбора нет, выберите номер символа из предлагаемого списка")
        syms = input("1. X\n2. O\n")
    return "X" if syms == "1" else "O"

def checkWinner(lst, sym):
    winner = 0
    win_lst = [["A1", "A2", "A3"],
               ["B1", "B2", "B3"],
               ["C1", "C2", "C3"]
               ["A1", "B2", "C3"],
               ["A3", "B2", "C1"],
               ["A1","B1", "C1"],
               ["A2","B2", "C2"],
               ["A3", "B3", "C3"]]
    
    for i in range(8):
        if lst[win_lst[i][0]] == lst[win_lst[i][1]] == lst[win_lst[i][2]]\
              and lst[win_lst[i][0]] != 0:
            winner = lst[win_lst[i][0]]
            break
    return winner

def game(name1, name2):
    ex = True
    kr = Field()
    kr.print_field()
    players ={}
    sym1 = change_sym(name1)
    sym2 = "O" if sym1 == "X" else "X"
    players[sym1] = name1
    players[sym2] = name2
    while ex:
        kr.change(sym1, input(f"Введите координату, {name1} : "))
        kr.print_field()
        kr.change(sym2, input(f"Введите координату, {name2}: "))
        kr.print_field()

game(input("Имя 1-го игрока: "), input("Имя 2-го игрока: "))

