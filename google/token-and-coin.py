def token_and_coin(board):
    n = len(board)
    result = 0
    for start in range(0, 3):
        has_token = False
        for i in range(start, n, 3):
            if board[i] == 'T':
                has_token = True
            elif has_token == True and board[i] == 'C':
                result += 1
    return result

board = "TT.T.CCCCC"
print(token_and_coin(board))
'''
start = 0
i = 
has_token = True
result = 2
C T . T . C C C C C
0 1 2 3 4 5 6 7 8 9
'''
        