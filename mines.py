from random import randint

mode1 = ((9, 9), 10)
mode2 = ((16, 16), 40)
# mode3 = ((16, 30), 99)    

window_width = 1280
window_height = 720

global_mode = mode1

class coords():
    def __init__(self, 
                 x: int, 
                 y: int, 
                 string: str):
        self.x = x
        self.y = y
        self.string = string
    
    def __str__(self):
        return (self.x , self.y, self.string)
    
    def __hash__(self):
        return hash((self.x, self.y, self.string))


def makemines(mode):
    mines = set()
    while len(mines) < mode[1]:
        if randint(1, 2) == 2:
            mines.add((randint(1, mode[0][0]), randint(1, mode[0][1])))
    return mines

def setboxes(mines, mode):
    box_list = [coords(x, y, 'U')
                 if (x, y) not in mines 
                 else coords(x, y, 'X') 
                 for x in range(1, mode[0][0] + 1) for y in range(1, mode[0][1] + 1)
                 ]
    return box_list

# mines = makemines(global_mode)
# print(mines)
# box_list = setboxes(mines, global_mode)
# print(box_list)