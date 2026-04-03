class Solutions:
    def captureMatrix(self, board):
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        for x in range(rows):
            for y in range(cols):
                if (x == 0 or x == rows - 1 or y == 0 or y == cols - 1) and board[x][y] == "O":
                    self.dfs(x, y, board)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
                
        print(board)

    
    def dfs(self, x, y, board):
        rows = len(board)
        cols = len(board[0])

        if x < 0 or x >= rows or y < 0 or y >= cols or board[x][y] != "O":
            return
        
        board[x][y] = "A"
        self.dfs(x + 1, y, board)
        self.dfs(x - 1, y, board)
        self.dfs(x, y + 1, board)
        self.dfs(x, y - 1, board)
        return
    

board = [["X","X","X","X"],
["X","O","O","X"],
["X","X","O","X"],
["X","O","X","X"]]

sol = Solutions()
sol.captureMatrix(board)

