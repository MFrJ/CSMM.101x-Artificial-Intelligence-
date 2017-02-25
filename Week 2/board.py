

class board:
        def __init__(self, values):
            self.values = values


        def move(self, direction): #directions = [U,D,L,R]
            new_values = list(self.values)
            if direction == 0: #up
                if new_values.index(0) + 3 <= 8: #blank space not in bottom row
                    i = new_values.index(0)
                    temp = new_values[i + 3]
                    new_values[i + 3] = 0
                    new_values[i] = temp
                else:
                    pass
            elif direction == 1: #down
                if new_values.index(0) - 3 >= 0: #blank space not in top row
                    i = new_values.index(0)
                    temp = new_values[i - 3]
                    new_values[i - 3] = 0
                    new_values[i] = temp
                else:
                    pass
            elif direction == 2: #left
                if (new_values.index(0) + 1) % 3 != 0: #blank space not in right column
                    i = new_values.index(0)
                    temp = new_values[i + 1]
                    new_values[i + 1] = 0
                    new_values[i] = temp
                else:
                    pass
            elif direction == 3: #right
                if new_values.index(0) % 3 != 0: #blank space not in left column
                    i = new_values.index(0)
                    temp = new_values[i - 1]
                    new_values[i - 1] = 0
                    new_values[i] = temp
                else:
                    pass
            return new_values

        def print_board(self):
                for i in range(9):
                    print(self.values[i], end="  ")
                    if (i+1) % 3 == 0:
                        print("\n", end="")
