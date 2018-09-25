#Bot Clean in partially observable environment - can only "sense" 3 x 3 squares
def find_nearest_target_dirt(robLoc, dLoc):
    for i in range(len(dLoc)):
        if i == 0:
            target_dLoc = dLoc[i]
        x1 = abs(robLoc[0] - dLoc[i][0])
        x2 = abs(robLoc[0] - target_dLoc[0])
        y1 = abs(robLoc[1] - dLoc[i][1])
        y2 = abs(robLoc[1] - target_dLoc[1])
        if x1 + y1 < x2 + y2:
            target_dLoc = dLoc[i]
    for j in range(len(dLoc)):
        if target_dLoc != dLoc[j]:
            write_memory(dLoc[j])
    return target_dLoc

def check_memory():
    filename = "memory.txt"
    f =  open(filename, "r")
    line = f.readline()
    f.close()
    if line != "":
        line = [int(line[1]), int(line[4])]
    return line

def check_positions():
    filename = "positions.txt"
    f =  open(filename, "r")
    lines = f.readlines()
    positions = []
    f.close()
    for line in lines:
        line = [int(line[1]), int(line[4])]
        positions.append(line)
    return positions

def check_clean_positions():
    filename = "clean_positions.txt"
    f =  open(filename, "r")
    lines = f.readlines()
    clean_positions = []
    f.close()
    for line in lines:
        line = [int(line[1]), int(line[4])]
        clean_positions.append(line)
    return clean_positions

def write_memory(dLoc):
    filename = "memory.txt"
    f = open(filename, "w")
    s = str(dLoc) + "\n"
    f.write(s)

    f.close()

def write_position(robLoc):
    filename = "positions.txt"
    f = open(filename, "w")
    s = str(robLoc) + "\n"
    f.write(s)
    
    f.close()

def write_clean_position(cleanLoc):
    filename = "clean_positions.txt"
    f = open(filename, "w")
    s = str(cleanLoc) + "\n"
    f.write(s)

    f.close()


def delete_memory(target_dLoc):
    filename = "memory.txt"
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    f =  open( filename , "w")
    for line in lines:
        if line != str(target_dLoc) + "\n":
            f.write(line)
    f.close()

def next_move(posx, posy, board):
    robLoc = [posx, posy]
    write_position(robLoc)
    dLoc = []
    
    for i in range(len(board)):
        if 'd' in str(''.join(board[i])):
            indices = [i for i, x in enumerate(str(''.join(board[i]))) if x == "d"]
            for j in range(len(indices)):
                dLoc.append([i, indices[j]])
        if '-' in str(''.join(board[i])):
            indices = [i for i, x in enumerate(str(''.join(board[i]))) if x == '-']
            for k in range(len(indices)):
                write_clean_position([i, indices[k]])
    # if not dLoc = no dirt in sight
    if not dLoc:
        if check_memory() == "":
            positions = check_positions()
            clean_positions = check_clean_positions()
            for x, y in zip(range(5), range(5)):
                if [x, y] not in positions and [x,y] not in clean_positions:
                    target = [x, y]
        else:
            target = check_memory()
    else:
        target = find_nearest_target_dirt(robLoc, dLoc)
    
        
        

    if robLoc[0] == int(target[0]) and robLoc[1] == int(target[1]):
        delete_memory(target)
        print("CLEAN")
        return
    if robLoc[0] < int(target[0]):
        print("DOWN")
        return
    elif robLoc[0] > int(target[0]):
        print("UP")
        return
    elif robLoc[1] < int(target[1]):
        print("RIGHT")
        return
    else:
        print("LEFT")
        return

if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]  
    next_move(pos[0], pos[1], board)