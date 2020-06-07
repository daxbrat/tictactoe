cells = []
for cell in range(9):
    cells.append(' ')
marker = 1

def checker():
    count_x = 0
    count_o = 0
    for count in range(9):
        if cells[count] == 'X':
            count_x += 1
        elif cells[count] == 'O':
            count_o += 1
    if (count_x - count_o >= 2) or (count_o - count_x >= 2):
        print("Impossible")
        quit()

    if (cells[0] == cells[1] == cells[2]) or (cells[0] == cells[3] == cells[6]):
        if cells[0] == 'X':
            print("X wins")
            quit()
        elif cells[0] == 'O':
            print('O wins')
            quit()
        elif cells[0] == ' ':
            cell_check()

    elif cells[3] == cells[4] == cells[5]:
        if cells[3] == 'X':
            print('X wins')
            quit()
        elif cells[3] == 'O':
            print('O wins')
            quit()
        elif cells[3] == ' ':
            cell_check()

    elif cells[6] == cells[7] == cells[8]:
        if cells[6] == 'X':
            print('X wins')
            quit()
        elif cells[6] == 'O':
            print('O wins')
            quit()
        elif cells[6] == ' ':
            cell_check()

    elif cells[0] == cells[4] == cells[8]:
        if cells[0] == 'X':
            print('X wins')
            quit()
        elif cells[0] == 'O':
            print('O wins')
            quit()
        elif cells[0] == ' ':
            cell_check()

    elif cells[2] == cells[4] == cells[6]:
        if cells[2] == 'X':
            print('X wins')
            quit()
        elif cells[2] == 'O':
            print('O wins')
            quit()
        elif cells[2] == ' ':
            cell_check()

    elif cells[1] == cells[4] == cells[7]:
        if cells[1] == 'X':
            print('X wins')
            quit()
        elif cells[1] == 'O':
            print('O wins')
            quit()
        elif cells[1] == ' ':
            cell_check()

    elif cells[2] == cells[5] == cells[8]:
        if cells[2] == 'X':
            print('X wins')
            quit()
        elif cells[2] == 'O':
            print('O wins')
            quit()
        elif cells[2] == ' ':
            cell_check()
    elif ' ' not in cells:
        print("Draw")
        quit()
    else:
        cell_check()


def print_cells(cell_list):
    print('---------')
    print('| ' + cells[0] + ' ' + cells[1] + ' ' + cells[2] + ' |')
    print('| ' + cells[3] + ' ' + cells[4] + ' ' + cells[5] + ' |')
    print('| ' + cells[6] + ' ' + cells[7] + ' ' + cells[8] + ' |')
    print('---------')
    checker()

def cell_check():
    global cells
    global marker
    while True:
        coords = input("Enter the coordinates: ")
        if coords == '1 1':
            if cells[6] == 'X' or cells[6] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            elif cells[6] == ' ':
                if marker % 2 == 1:
                    cells[6] = 'X'
                    marker += 1
                    print_cells(cells)
                else:
                    cells[6] = 'O'
                    marker += 1
                    print_cells(cells)
                    #break

        elif coords == '2 1':
            if cells[7] == 'X' or cells[7] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            elif cells[7] == ' ':
                if marker % 2 == 1:
                    cells[7] = 'X'
                    marker += 1
                    print_cells(cells)
                else:
                    cells[7] = 'O'
                    marker += 1
                    print_cells(cells)
                    #break
        elif coords == '3 1':
            if cells[8] == 'X' or cells[8] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            elif cells[8] == ' ':
                if marker % 2 == 1:
                    cells[8] = 'X'
                    marker += 1
                    print_cells(cells)
                else:
                    cells[8] = 'O'
                    marker += 1
                    print_cells(cells)
                    #break
        elif coords == '1 2':
            if cells[3] == 'X' or cells[3] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            elif cells[3] == ' ':
                if marker % 2 == 1:
                    cells[3] = 'X'
                    marker += 1
                    print_cells(cells)
                else:
                    cells[3] = 'O'
                    marker += 1
                    print_cells(cells)
                    #break
        elif coords == '2 2':
            if cells[4] == 'X' or cells[4] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            elif cells[4] == ' ':
                if marker % 2 == 1:
                    cells[4] = 'X'
                    marker += 1
                    print_cells(cells)
                else:
                    cells[4] = 'O'
                    marker += 1
                    print_cells(cells)
                    #break
        elif coords == '3 2':
            if cells[5] == 'X' or cells[5] == 'O':
                print("This cell is occupied! Choose another one!")
                congtinue
            elif cells[5] == ' ':
                if marker % 2 == 1:
                    cells[5] = 'X'
                    marker += 1
                    print_cells(cells)
                else:
                    cells[5] = 'O'
                    marker += 1
                    print_cells(cells)
                    #break
        elif coords == '1 3':
            if cells[0] == 'X' or cells[0] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            elif cells[0] == ' ':
                if marker % 2 == 1:
                    cells[0] = 'X'
                    marker += 1
                    print_cells(cells)
                else:
                    cells[0] = 'O'
                    marker += 1
                    print_cells(cells)
                    #break
        elif coords == '2 3':
            if cells[1] == 'X' or cells[1] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            elif cells[1] == ' ':
                if marker % 2 == 1:
                    cells[1] = 'X'
                    marker += 1
                    print_cells(cells)
                else:
                    cells[1] = 'O'
                    marker += 1
                    print_cells(cells)
                    #break
        elif coords == '3 3':
            if cells[2] == 'X' or cells[2] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            elif cells[2] == ' ':
                if marker % 2 == 1:
                    cells[2] = 'X'
                    marker += 1
                    print_cells(cells)
                else:
                    cells[2] = 'O'
                    marker += 1
                    print_cells(cells)
                    #break
        try:
            int(coords[0])
            int(coords[2])
        except:
            print("You should enter numbers!")
            continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue

print_cells(cells)
