from bfs import bfs
from board import board

def main():
        dirs = {"up": 0, "down":1, "left": 2, "right": 3}
        l = [int(x) for x in "1,2,5,3,4,0,6,7,8".split(",")]
        b = board(l)
        g = board([1,2,0,3,4,5,6,7,8])
        bfs(b, g)
        # b.move(dirs["up"])
        # b.print_board()
        # print("")

if __name__ == '__main__':
    main()
