def horizontal_lines(matrix):
    bingo=False
    for i in range(len(matrix)):
        if bingo==False:
            for j in range(5):
                if matrix[i][j]=="X":
                    bingo=True
                else:
                    bingo=False
                    break
        else: 
            break
    return bingo


def vertical_lines(matrix):
    