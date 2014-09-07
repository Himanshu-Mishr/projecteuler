
import matrix
x = matrix.a

ctlr = 80
def main():
    recursion(0, 0)

def recursion(x, y):
    print(x, y)

    # this controls the recursion
    if x < ctlr and y < ctlr: pass
    else:
        return "DONE"

    # this controls the moves
    recursion(x, y+1)
    recursion(x+1, y)
if __name__ == '__main__':
    main()
