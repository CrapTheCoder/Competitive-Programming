"""
1 : Move left
2 : Move right
3 : Pick up box
4 : Drop box
0 : Quit

"""

class VideoGame:
    def __init__(self, stacks, rows, columns):
        self.stacks = stacks
        self.rows = rows
        self.columns = columns
        self.cur_row = 0
        self.box_in_hand = False

        self.commands = {'1': self.move_left, '2': self.move_right,
                         '3': self.pick_up_box, '4': self.drop_box,
                         '0': self.quit}

    def command_parser(self, command):
        self.commands[command]()

    def move_right(self):
        if self.cur_row == self.rows - 1:
            return
        self.cur_row += 1

    def move_left(self):
        if self.cur_row == 0:
            return
        self.cur_row -= 1

    def pick_up_box(self):
        if (self.box_in_hand or
                self.stacks[self.cur_row] == 0):
            return
        self.stacks[self.cur_row] -= 1
        self.box_in_hand = True

    def drop_box(self):
        if (not self.box_in_hand or
                self.stacks[self.cur_row] == self.columns):
            return
        self.stacks[self.cur_row] += 1
        self.box_in_hand = False

    def quit(self):
        print(*self.stacks)
        exit()

r, c = map(int, input().split())
s = list(map(int, input().split()))
commands = input().split()

video_game = VideoGame(s, r, c)

for cmd in commands:
    video_game.command_parser(cmd)