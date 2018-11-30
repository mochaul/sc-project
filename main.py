import tkinter as tk                # python3
from tkinter import font  as tkfont # python3

TOP = "ABCDEFGHIJ"
SIDE = "0123456789"
SHIP = "S"
HIT = "X"
MISS = "O"
EMPTY = " "
ships = [["Martadinata", 5, 1], ["Fatahilla", 4, 1], ["Cakra", 3, 1], ["Boa", 3, 1], ["Andau", 2, 1]]
ships_ai = [["Kapal Liar", 5], ["Kapal Liar", 4], ["Kapal Liar", 3], ["Kapal Liar", 3], ["Kapal Liar", 2]]
arr_ship_player =100 * [" "]
arr_ship_ai = 100 * [" "]
arr_arr_ship_ai = []
diff = ""

global grid_convert, inv_gridconvert, gen_pos_list, onboard, \
    check_diagonal, grid_pick_tile, get_dirs, getdirs_ext

def grid_convert(location):
        "Turns A0 coordinates into grid numbers"
        location = TOP.find(location[0]) + (SIDE.find(location[1]) * 10)
        return location

def inv_gridconvert(location):
    "Turns grid numbers into A0 coordinates"
    location = TOP[location % 10] + SIDE[int(location / 10)]
    return location

def gen_pos_list(location, length):
    "Turns [1, 2] coordinates and length into list of grid numbers"
    direction = location[1] - location[0]
    if abs(direction) >= 10:
        if direction < 0:
            direction = -10
        else:
            direction = 10
    else:
        if direction < 0:
            direction = -1
        else:
            direction = 1
    location = [location[0], location[0] + direction]

    pos_list = []
    for pos in range(location[0], location[0] + (length * direction), direction):
        pos_list += [pos]
        
    return pos_list

def onboard(coords):
    "Checks if A0 coordinates are on the board"
    if coords[0] in TOP and coords[1] in SIDE:
        return True
    else:
        return False

def check_diagonal(location):
    "Returns True if [0, 1] coordinates are diagonal"
    if location[0] % 10 == location[1] % 10 or \
    int(location[0] / 10) == int(location[1] / 10):
        return False
    else:
        return True

def grid_pick_tile():
    "Chooses a tile from grid"
    from random import randrange
    target = randrange(0, 91, 10)
    target += randrange((target // 10) % 2, 10, 2)
    return target

def get_dirs(pos):
    "Returns avaliable directions from pos"
    output = []
    if pos % 10 != 9: output += [1]
    if pos % 10 != 0: output += [-1]
    if pos < 90: output += [10]
    if pos > 9: output += [-10]
    return output

def getdirs_ext(pos):
    "Returns extended available directions from pos"
    from itertools import combinations
    output = get_dirs(pos)
    for comb in combinations(output, 2):
        if sum(comb) != 0:
            output += [sum(comb)]
    return output

class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("Tenggelamkan!: The Game")
        self.geometry("1000x800")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (KapalSatu, KapalDua, KapalTiga, KapalEmpat, KapalLima, GameStart):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("KapalSatu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        
class KapalSatu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #label00 = tk.Label(self, text=user_board.render())

        label_0 = tk.Label(self, text="WELCOME TO TENGGELAMKAN!", font=("bold", 15))
        label_11 = tk.Label(self, text="Format penulisan 'X sampai X' (misal A4 sampai A9)", font=("bold", 10))
        label_0.place(x=70, y=53)
        label_11.place(x=90, y=100)
        self.board = 100 * [" "]
        label_1 = tk.Label(self, text="Kapal Martadinata (5)", width=20, font=("bold", 10))
        label_1.place(x=80, y=130)
        self.label_6 = tk.Label(self, text=self.render())
        self.label_6.place(x=80, y=430)
        self.entry_1 = tk.Entry(self)
        self.entry_1.place(x=240, y=130)

        self.button = tk.Button(self, text="check", command=self.on_button)
        self.button_2 = tk.Button(self, text="next", command= lambda : controller.show_frame("KapalDua"))
        self.button.place(x=130, y = 380)
        self.button_2.place(x= 240, y = 380)

    def on_button(self):
        pos_1 = self.entry_1.get()
        self.entry_1.delete(0, 'end')

        if (pos_1[0] in TOP and pos_1[1] in SIDE and pos_1[-1] in SIDE and pos_1[-2] in TOP ):
#            arr_of_ships.append(["Kapal Martadinata", 5, 1, pos_1]) :
            location = TOP.find(pos_1[0]) + (SIDE.find(pos_1[1])*10)
            location_1 = TOP.find(pos_1[-2]) + (SIDE.find(pos_1[-1])*10)
            if (abs(location-location_1) == 4 or abs(location-location_1) == 40):
                if location % 10 == location_1 % 10 or \
                        int(location / 10) == int(location_1 / 10):
                    direction = location_1 - location
                    if abs(direction) >= 10:
                        if direction < 0:
                            direction = -10
                        else:
                            direction = 10
                    else:
                        if direction < 0:
                            direction = -1
                        else:
                            direction = 1
                    location = [location, location + direction]

                    pos_list = []
                    # generate posisi kapal
                    for pos in range(location[0], location[0] + (5 * direction), direction):
                        pos_list += [pos]
                    # add ship
                    for x in pos_list:
                        arr_ship_player[x] = SHIP
                else:
                    print("kapal tidak boleh diagonal")
                    return True
            else :
                print ("harus 5 kotak terisi")

        output = "      |  "
        output += "  |   ".join(i for i in TOP)
        for row in range(10):
            output += "\n" + (55 * "-") + "\n" + SIDE[row] + " "
            for col in range(10):
                x = row * 10 + col
                output += "    | %s " % arr_ship_player[x]
        output += "\n" + (55 * "-")
        self.label_6.configure(text=output)

    def render(self):
        output = "      |  "
        output += "  |   ".join(i for i in TOP)
        for row in range(10):
            output += "\n" + (55* "-") + "\n" + SIDE[row] + " "
            for col in range(10):
                x = row*10 + col
                output += "    | %s " % arr_ship_player[x]
        output += "\n" + (55 * "-")
        return output

class KapalDua(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label_0 = tk.Label(self, text="WELCOME TO TENGGELAMKAN!", font=("bold", 15))
        label_11 = tk.Label(self, text="Format penulisan 'X sampai X' (misal A4 sampai A9)", font=("bold", 10))
        label_0.place(x=70, y=53)
        label_11.place(x=90, y=100)
        self.board = 100 * [" "]
        label_1 = tk.Label(self, text="Kapal Fatahillah (4)", width=20, font=("bold", 10))
        label_1.place(x=80, y=130)
        self.label_6 = tk.Label(self, text=self.render())
        self.label_6.place(x=80, y=430)
        self.entry_1 = tk.Entry(self)
        self.entry_1.place(x=240, y=130)

        self.button = tk.Button(self, text="check", command=self.on_button)
        self.button_2 = tk.Button(self, text="next", command= lambda : controller.show_frame("KapalTiga"))
        self.button.place(x=130, y = 380)
        self.button_2.place(x= 240, y = 380)

    def on_button(self):
        pos_1 = self.entry_1.get()
        self.entry_1.delete(0, 'end')
        flag = True
        if (pos_1[0] in TOP and pos_1[1] in SIDE and pos_1[-1] in SIDE and pos_1[-2] in TOP ):
            location = TOP.find(pos_1[0]) + (SIDE.find(pos_1[1]) * 10)
            location_1 = TOP.find(pos_1[-2]) + (SIDE.find(pos_1[-1]) * 10)
            if (abs(location-location_1)==3 or abs(location-location_1)==30):
                if location % 10 == location_1 % 10 or \
                        int(location / 10) == int(location_1 / 10):
                    direction = location_1 - location
                    if abs(direction) >= 10:
                        if direction < 0:
                            direction = -10
                        else:
                            direction = 10
                    else:
                        if direction < 0:
                            direction = -1
                        else:
                            direction = 1
                    location = [location, location + direction]

                    pos_list = []
                    # generate posisi kapal
                    for pos in range(location[0], location[0] + (4 * direction), direction):
                        pos_list += [pos]
                    #check ship
                    for x in pos_list:
                        if (arr_ship_player[x]==SHIP):
                            print ("sudah ada kapal di posisi itu")
                            flag = False

                    if (flag):
                        # add ship
                        for i in pos_list:
                            arr_ship_player[i] = SHIP
                    print(arr_ship_player)
                else:
                    print("kapal tidak boleh diagonal")
                    return True
            else :
                print("harus 4 kotak terisi")
        output = "      |  "
        output += "  |   ".join(i for i in TOP)
        for row in range(10):
            output += "\n" + (55 * "-") + "\n" + SIDE[row] + " "
            for col in range(10):
                x = row * 10 + col
                output += "    | %s " % arr_ship_player[x]
        output += "\n" + (55 * "-")
        self.label_6.configure(text=output)


    def render(self):
        output = "      |  "
        output += "  |   ".join(i for i in TOP)
        for row in range(10):
            output += "\n" + (55* "-") + "\n" + SIDE[row] + " "
            for col in range(10):
                x = row * 10 + col
                output += "    | %s " % self.board[x]
        output += "\n" + (55 * "-")
        return output

class KapalTiga(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label_0 = tk.Label(self, text="WELCOME TO TENGGELAMKAN!", font=("bold", 15))
        label_11 = tk.Label(self, text="Format penulisan 'X sampai X' (misal A4 sampai A9)", font=("bold", 10))
        label_0.place(x=70, y=53)
        label_11.place(x=90, y=100)
        self.board = 100 * [" "]
        label_1 = tk.Label(self, text="Kapal Cakra (3)", width=20, font=("bold", 10))
        label_1.place(x=80, y=130)
        self.label_6 = tk.Label(self, text=self.render())
        self.label_6.place(x=80, y=430)
        self.entry_1 = tk.Entry(self)
        self.entry_1.place(x=240, y=130)

        self.button = tk.Button(self, text="check", command=self.on_button)
        self.button_2 = tk.Button(self, text="next", command= lambda : controller.show_frame("KapalEmpat"))
        self.button.place(x=130, y = 380)
        self.button_2.place(x= 240, y = 380)

    def on_button(self):
        pos_1 = self.entry_1.get()
        self.entry_1.delete(0, 'end')

        if (pos_1[0] in TOP and pos_1[1] in SIDE and pos_1[-1] in SIDE and pos_1[-2] in TOP ):
            #arr_of_ships.append(["Kapal Cakra", 3, 1, pos_1])
            location = TOP.find(pos_1[0]) + (SIDE.find(pos_1[1]) * 10)
            location_1 = TOP.find(pos_1[-2]) + (SIDE.find(pos_1[-1]) * 10)
            if (abs(location - location_1) == 2 or abs(location - location_1) == 20):
                location = TOP.find(pos_1[0]) + (SIDE.find(pos_1[1]) * 10)
                location_1 = TOP.find(pos_1[-2]) + (SIDE.find(pos_1[-1]) * 10)
                if location % 10 == location_1 % 10 or \
                        int(location / 10) == int(location_1 / 10):
                    direction = location_1 - location
                    if abs(direction) >= 10:
                        if direction < 0:
                            direction = -10
                        else:
                            direction = 10
                    else:
                        if direction < 0:
                            direction = -1
                        else:
                            direction = 1
                    location = [location, location + direction]

                    pos_list = []
                    # generate posisi kapal
                    flag3 = True
                    for pos in range(location[0], location[0] + (3 * direction), direction):
                        pos_list += [pos]
                    # check ship
                    for x in pos_list:
                        if (arr_ship_player[x] == SHIP):
                            print("sudah ada kapal di posisi itu")
                            flag3 = False

                    if (flag3):
                        # add ship
                        for i in pos_list:
                            arr_ship_player[i] = SHIP
                    print(arr_ship_player)
        else :
            print("harus 3 kotak terisi")
        output = "      |  "
        output += "  |   ".join(i for i in TOP)
        for row in range(10):
            output += "\n" + (55 * "-") + "\n" + SIDE[row] + " "
            for col in range(10):
                x = row * 10 + col
                output += "    | %s " % arr_ship_player[x]
        output += "\n" + (55 * "-")
        self.label_6.configure(text=output)

    def render(self):
        output = "      |  "
        output += "  |   ".join(i for i in TOP)
        for row in range(10):
            output += "\n" + (55* "-") + "\n" + SIDE[row] + " "
            for col in range(10):
                output += "    | %s " % self.board[row * 10 + col]
        output += "\n" + (55 * "-")
        return output

class KapalEmpat(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label_0 = tk.Label(self, text="WELCOME TO TENGGELAMKAN!", font=("bold", 15))
        label_11 = tk.Label(self, text="Format penulisan 'X sampai X' (misal A4 sampai A9)", font=("bold", 10))
        label_0.place(x=70, y=53)
        label_11.place(x=90, y=100)
        self.board = 100 * [" "]
        label_1 = tk.Label(self, text="Kapal Boa (3)", width=20, font=("bold", 10))
        label_1.place(x=80, y=130)
        self.label_6 = tk.Label(self, text=self.render())
        self.label_6.place(x=80, y=430)
        self.entry_1 = tk.Entry(self)
        self.entry_1.place(x=240, y=130)

        self.button = tk.Button(self, text="check", command=self.on_button)
        self.button_2 = tk.Button(self, text="next", command= lambda : controller.show_frame("KapalLima"))
        self.button.place(x=130, y = 380)
        self.button_2.place(x= 240, y = 380)

    def on_button(self):
        pos_1 = self.entry_1.get()
        self.entry_1.delete(0, 'end')

        if (pos_1[0] in TOP and pos_1[1] in SIDE and pos_1[-1] in SIDE and pos_1[-2] in TOP ):
            #arr_of_ships.append(["Kapal Boa", 3, 1, pos_1])
            location = TOP.find(pos_1[0]) + (SIDE.find(pos_1[1]) * 10)
            location_1 = TOP.find(pos_1[-2]) + (SIDE.find(pos_1[-1]) * 10)
            if (abs(location - location_1) == 2 or abs(location - location_1) == 20):
                location = TOP.find(pos_1[0]) + (SIDE.find(pos_1[1]) * 10)
                location_1 = TOP.find(pos_1[-2]) + (SIDE.find(pos_1[-1]) * 10)
                if location % 10 == location_1 % 10 or \
                        int(location / 10) == int(location_1 / 10):
                    direction = location_1 - location
                    if abs(direction) >= 10:
                        if direction < 0:
                            direction = -10
                        else:
                            direction = 10
                    else:
                        if direction < 0:
                            direction = -1
                        else:
                            direction = 1
                    location = [location, location + direction]
                    flag1 = True
                    pos_list = []
                    # generate posisi kapal
                    for pos in range(location[0], location[0] + (3 * direction), direction):
                        pos_list += [pos]
                    # check ship
                    for x in pos_list:
                        if (arr_ship_player[x] == SHIP):
                            print("sudah ada kapal di posisi itu")
                            flag1 = False

                    if (flag1):
                        # add ship
                        for i in pos_list:
                            arr_ship_player[i] = SHIP
                    print(arr_ship_player)
        else:
            print("harus 3 kotak terisi")
        output = "      |  "
        output += "  |   ".join(i for i in TOP)
        for row in range(10):
            output += "\n" + (55 * "-") + "\n" + SIDE[row] + " "
            for col in range(10):
                x = row * 10 + col
                output += "    | %s " % arr_ship_player[x]
        output += "\n" + (55 * "-")
        self.label_6.configure(text=output)

    def render(self):
        output = "      |  "
        output += "  |   ".join(i for i in TOP)
        for row in range(10):
            output += "\n" + (55* "-") + "\n" + SIDE[row] + " "
            for col in range(10):
                output += "    | %s " % self.board[row * 10 + col]
        output += "\n" + (55 * "-")
        return output

class KapalLima(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label_0 = tk.Label(self, text="WELCOME TO TENGGELAMKAN!", font=("bold", 15))
        label_11 = tk.Label(self, text="Format penulisan 'X sampai X' (misal A4 sampai A9)", font=("bold", 10))
        label_0.place(x=70, y=53)
        label_11.place(x=90, y=100)
        self.board = 100 * [" "]
        label_1 = tk.Label(self, text="Kapal Andau (2)", width=20, font=("bold", 10))
        label_1.place(x=80, y=130)
        self.label_6 = tk.Label(self, text=self.render())
        self.label_6.place(x=80, y=430)
        self.entry_1 = tk.Entry(self)
        self.entry_1.place(x=240, y=130)
        self.var  = tk.StringVar(self)
        optionMenu = tk.OptionMenu(self, self.var, "Easy","Medium","Hard")
        optionMenu.place(x=240,y=180)
        self.button = tk.Button(self, text="check", command=self.on_button)
        self.button_2 = tk.Button(self, text="next", command= lambda : controller.show_frame("GameStart"))
        self.button.place(x=130, y = 380)
        self.button_2.place(x= 240, y = 380)
        self.button3 = tk.Button(self, text="print", command= self.click_me())
        self.button3.pack()

    def on_button(self):
        pos_1 = self.entry_1.get()
        self.entry_1.delete(0, 'end')
        diff = self.var.get()
        if (pos_1[0] in TOP and pos_1[1] in SIDE and pos_1[-1] in SIDE and pos_1[-2] in TOP ):
            #arr_of_ships.append(["Kapal Andau", 2, 1, pos_1])
            location = TOP.find(pos_1[0]) + (SIDE.find(pos_1[1]) * 10)
            location_1 = TOP.find(pos_1[-2]) + (SIDE.find(pos_1[-1]) * 10)
            if (abs(location_1-location)==1 or abs(location_1-location)==10):
                if location % 10 == location_1 % 10 or \
                        int(location / 10) == int(location_1 / 10):
                    direction = location_1 - location
                    if abs(direction) >= 10:
                        if direction < 0:
                            direction = -10
                        else:
                            direction = 10
                    else:
                        if direction < 0:
                            direction = -1
                        else:
                            direction = 1
                    location = [location, location + direction]

                    pos_list = []
                    # generate posisi kapal
                    flag2 = True
                    for pos in range(location[0], location[0] + (2 * direction), direction):
                        pos_list += [pos]
                    # check ship
                    for x in pos_list:
                        if (arr_ship_player[x] == SHIP):
                            print("sudah ada kapal di posisi itu")
                            flag2 = False

                    if (flag2):
                        # add ship
                        for i in pos_list:
                            arr_ship_player[i] = SHIP
                    print(arr_ship_player)
        else :
            print("harus 2 kotak terisi")
        output = "      |  "
        output += "  |   ".join(i for i in TOP)
        for row in range(10):
            output += "\n" + (55 * "-") + "\n" + SIDE[row] + " "
            for col in range(10):
                x = row * 10 + col
                output += "    | %s " % arr_ship_player[x]
        output += "\n" + (55 * "-")
        self.label_6.configure(text=output)

    def render(self):
        output = "      |  "
        output += "  |   ".join(i for i in TOP)
        for row in range(10):
            output += "\n" + (55* "-") + "\n" + SIDE[row] + " "
            for col in range(10):
                output += "    | %s " % self.board[row * 10 + col]
        output += "\n" + (55 * "-")
        return output

    def click_me(self):
        output = "      |  "
        output += "  |   ".join(i for i in TOP)
        for row in range(10):
            output += "\n" + (55 * "-") + "\n" + SIDE[row] + " "
            for col in range(10):
                x = row * 10 + col
                output += "    | %s " % arr_ship_player[x]
        output += "\n" + (55 * "-")
        self.label_6.configure(text = output)

class AI:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.mode = "HUNT"
        self.modelist = {"HUNT": self.hunt, "ACQUIRE": self.acquire, "DESTROY": self.destroy}

    def turn(self, end = True):
        result = self.modelist[self.mode]()
        if end:
            if result[0]:
                print("\nComputer hit %s" % inv_gridconvert(result[1]))
            else:
                print("\nComputer missed %s" % inv_gridconvert(result[1]))

    def hunt(self):
        target = self.pick_tile()

        for i in range(self.difficulty):
            if arr_ship_player == SHIP:
                break
            else:
                target = self.pick_tile()

        if arr_ship_player == SHIP:
            self.mode = "ACQUIRE"
            self.acq_list = [target]

            for direction in get_dirs(target):
                if arr_ship_player[target + direction] not in (MISS, HIT):
                    self.acq_list += [direction]

        return self.enemy.fire(target), target

    def acquire(self):
        target = self.acq_list[0] + self.acq_list[1]

        for i in range(self.difficulty):
            if arr_ship_player == SHIP:
                break
            else:
                self.acq_list.pop(1)
                target = self.acq_list[0] + self.acq_list[1]

        if arr_ship_player == SHIP:
            result = self.enemy.fire(target)
            self.dest_list = self.find_ship(self.acq_list[0], self.acq_list[1])
            self.mode = "DESTROY"
        else:
            result = self.enemy.fire(target)
            self.acq_list.pop(1)

        return result, target

    def destroy(self):
        if len(self.dest_list) > 0:
            target = self.dest_list[0]
            self.dest_list.pop(0)
        else:
            self.mode = "HUNT"
            return self.hunt()
        
        return self.enemy.fire(target), target

    def find_ship(self, pos, direction):
        pos_list = []

        for i in range(2):
            ignore, prog_pos = False, pos
            while not ignore:
                if check_diagonal([prog_pos, prog_pos + direction]) or \
                   prog_pos + direction < 0:
                    ignore = True
                    continue
                
                prog_pos += direction
                if arr_ship_player[prog_pos] == HIT:
                    pass
                elif arr_ship_player[prog_pos] == EMPTY:
                    pos_list += [prog_pos]
                    ignore = True
                elif arr_ship_player[prog_pos] == MISS:
                    ignore = True
                else:
                    pos_list += [prog_pos]
            direction *= -1
        return pos_list

    def pick_tile(self):
        target = grid_pick_tile()
        while arr_ship_player in (MISS, HIT):
            target = grid_pick_tile()
        return target

class GameStart(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        left = tk.Frame(self, borderwidth=2, relief="solid")
        right = tk.Frame(self, borderwidth=2, relief="solid")
        self.board = 100 * [" "]
        label2 = tk.Label(left, text="Pembela Tanah Air")
        self.text_tembak = tk.StringVar(self)
        button1 = tk.Button(left, text="Tenggelamkan!", command=self.on_button)
        self.entry_8 = tk.Entry(left, textvariable = self.text_tembak)
        self.label15 = tk.Label(left, text= "tekan tombol refresh")
        label3 = tk.Label(right, text="Nelayan Ilegal")
        self.label14 = tk.Label(right, text="tekan tombol refresh")
        button3 = tk.Button(self,text="refresh",comand=self.refresh())
        button3.pack()
        left.pack(side="left", expand=True, fill="both")
        right.pack(side="right", expand=True, fill="both")
        label2.pack()
        self.entry_8.pack()
        button1.pack()
        self.label15.pack()
        label3.pack()
        self.label14.pack()
        self.setupAI(arr_ship_ai)

    def setupAI(self, arr_ship_ai):
        from random import choice, randint
        for ship in ships_ai:
            length, number = ship[1], ship[2]
            for i in range(number):
                allocated = False
                while not allocated:
                    location = [randint(0, 99), 0]
                    direction = choice(get_dirs(location[0]))
                    location[1] = location[0] + direction

                    location = gen_pos_list(location, length)



                    arr_ship_ai.add_ship(location)
                    arr_ship_ai.ships += length
                    allocated = True
        print(arr_ship_ai)

    def render(self, arr):
        output = "      |  "
        output += "  |   ".join(i for i in TOP)
        for row in range(10):
            output += "\n" + (55* "-") + "\n" + SIDE[row] + " "
            for col in range(10):
                x = row * 10 + col
                output += "    | %s " % arr[x]
        output += "\n" + (55 * "-")
        return output

    def refresh(self):
        self.label15.configure(text =self.render(arr_ship_player))
        self.label14.configure(text= self.render(arr_ship_ai))
		
    def on_button(self):
        pos = self.entry_8.get()

        if (len(pos)!=2):
            print ("input tidak valid masukan input yang valid")
        else :
            if (pos[0].upper() not in TOP):
                print ("input tidak valid masukan input yang valid")
            else :
                if (pos[1] not in SIDE):
                    print("input tidak valid masukan input yang valid")
                else :
                    location = TOP.find(pos[0]) + (SIDE.find(pos[1]) * 10)
                    if (arr_ship_ai[location]=='S'):
                        arr_arr_ship_ai[location] = HIT
                        HP_Enemy=-1
                    elif(arr_ship_ai[location]==' '):
                        arr_arr_ship_ai[location] = MISS
        self.label14.configure(text= self.render(arr_arr_ship_ai))
        print(self.entry_8.get())
        self.entry_8.delete(0, 'end')

def main():
    app = GUI()
    app.mainloop()

main()

# if __name__ == "__main__": 
#     app = GUI() 
#     app.mainloop()