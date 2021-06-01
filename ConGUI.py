import curses
from curses.textpad import rectangle

scr = curses.initscr()
# Window
begin_x = 2; begin_y = 1;
height = 13; width = 26;
win = curses.newwin(height, width, begin_y, begin_x)
winS = curses.newwin(height, width, begin_y, begin_x+width)
horLine = "-----(  )-----(  )-----"
verLine = "       |        |      "

def main():
    curses.cbreak()
    curses.curs_set(2)

    scr.addstr(0,0, "Welcome to Sujiko!")


    for i in range(1, 12):
        string = verLine
        if i%4 == 0:
            string = horLine
        win.addstr(i, 1, string)

    win.box()
    scr.refresh()
    win.refresh()

POS = ((2,3), (2, 12), (2, 21), (6,3), (6, 12), (6, 21), (10,3), (10, 12), (10, 21))
def addSums(a, b, c ,d, ind, num):
    win.addstr(4, 7, str(a))
    win.addstr(4, 16, str(b))
    win.addstr(8, 7, str(c))
    win.addstr(8, 16, str(d))

    win.addch(*POS[ind],str(num), curses.A_STANDOUT)
    for i in range(9):
        y = POS[i][0] - 1
        x = POS[i][1] - 2
        win.addch(y,x,chr(i+97), curses.A_DIM)

    win.refresh()

def interact(nums):
    scr.addstr(14, 2, "Press 'q' to exit or 's' to toggle solution", curses.A_ITALIC)
    
    while(True):
        scr.refresh()
        scr.addstr(16, 2, "Enter a letter: ")
        let = scr.getch()
        showSol = False
        if chr(let) >= 'a' and chr(let) <= 'i':
            scr.addstr(16, 2, str("Enter a number for position "+chr(let)+": "))
            num = scr.getch()
            if chr(num) >= '1' and chr(num) <= '9':
                win.addch(*POS[let-97], chr(num), curses.A_BOLD)
            else:
                scr.deleteln()
                curses.beep()
                scr.addstr(16, 2, "Invalid input.")
                scr.refresh()
                curses.napms(3000)
            win.refresh()
            scr.deleteln()
            continue
        elif chr(let) == 'q':
            clear()
            return
        elif chr(let) == 's':
            showSol = not showSol
            scr.deleteln()

            if showSol:
                for i in range(1, 12):
                    string = verLine
                    if i%4 == 0:
                        string = horLine
                    winS.addstr(i, 1, string)
                winS.box()
                for j in range(9):
                    winS.addch(*POS[j], str(nums[j]), curses.A_BOLD)
            else:
                for i in range(14):
                    winS.addstr(i,1, "                                ")
                    winS.refresh()
            winS.refresh()
            scr.refresh()
        else:
            scr.deleteln()
            curses.beep()
            scr.addstr(16, 2, "Invalid input.")
            scr.refresh()
            curses.napms(3000)
            continue

def clear():
    scr.erase()
    scr.refresh()
    curses.endwin()

if __name__ == "__main__":
    main()