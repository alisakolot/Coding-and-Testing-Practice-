class TicTacToe:
    def __init__(self):
        self.board = []

    def create_board(self, columns=4, rows=3):
        for k in range(0, rows-1): #[0,1,2]
            self.board.append([]) 
            for n in range(0, rows): # [0,1,2,3]
                self.board[k][n] = '*'
        
        return self.board

    def print_board(self):
        # [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']]
        for lst in self.board:
            j = 0
            k = ''
            while j in range(len(lst)):
                k += lst[j] + ' '
                j += 1
                if j == len(lst):
                    print(k)
                    

    # empty_board = create_board()
    # print_board(empty_board)

    def move(self, x, y, char='x'):
        #x item inside the nested list
        #y the index inside the master list

        #position = x,y
        print(self.board[x])
        print(self.board[x][y])
        self.board[x][y] = char
        print('after:', print(self.board[x][y]))
        self.print_board()

        
       
    
new_game = TicTacToe()
new_game.create_board()
new_game.print_board()
    






