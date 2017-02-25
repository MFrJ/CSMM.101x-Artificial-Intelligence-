class board:
        def __init__(self, values):
            self.values = values

        def swap(a,b):
            a,b = b,a

        def move(self, direction): #directions = [U,D,L,R]
            if direction == 0: #up
                if self.values.index(0) + 3 <= 8: #blank space not in bottom row
                    i = self.values.index(0)
                    temp = self.values[i + 3]
                    self.values[i + 3] = 0
                    self.values[i] = temp
                else:
                    pass
            elif direction == 1: #down
                if self.values.index(0) - 3 >= 0: #blank space not in top row
                    i = self.values.index(0)
                    temp = self.values[i - 3]
                    self.values[i - 3] = 0
                    self.values[i] = temp
                else:
                    pass
            elif direction == 2: #left
                if (self.values.index(0) + 1) % 3 != 0: #blank space not in right column
                    i = self.values.index(0)
                    temp = self.values[i + 1]
                    self.values[i + 1] = 0
                    self.values[i] = temp
                else:
                    pass
            elif direction == 3: #right
                if self.values.index(0) % 3 != 0: #blank space not in left column
                    i = self.values.index(0)
                    temp = self.values[i - 1]
                    self.values[i - 1] = 0
                    self.values[i] = temp
                else:
                    pass

        def print_board(self):
                for i in range(9):
                    print(self.values[i], end="  ")
                    if (i+1) % 3 == 0:
                        print("\n", end="")

def main():
        l = [int(x) for x in "1,2,5,3,4,0,6,7,8".split(",")]
        b = board(l)
        dirs = {"up": 0, "down":1, "left": 2, "right": 3}
        b.print_board()
        print("")
        b.move(0)
        b.print_board()
        print("")
        b.move(dirs["right"])
        b.print_board()
        print("")
        b.move(dirs["right"])
        b.print_board()
        print("")
        b.move(dirs["left"])
        b.print_board()
        print("")
        b.move(dirs["up"])
        b.print_board()
        print("")
        b.move(dirs["up"])
        b.print_board()
        print("")
        b.move(dirs["down"])
        b.print_board()
        print("")
        b.move(dirs["down"])
        b.print_board()
        print("")
        b.move(dirs["up"])
        b.print_board()
if __name__ == '__main__':
    main()
