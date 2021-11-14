#!/usr/bin/env python
# coding: utf-8

# In[9]:


class NQueens:
    def __init__(self, size):
        
        self.size = size
        self.solutions = 0
        self.solve()

    def solve(self):
        
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        print("Found", self.solutions, "solutions.")

    def put_queen(self, positions, target_row):
        
        if target_row == self.size:
            self.show_full_board(positions)
           
            self.solutions += 1
        else:
           
            for column in range(self.size):
               
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)


    def check_place(self, positions, ocuppied_rows, column):

        for i in range(ocuppied_rows):
            if positions[i] == column or                 positions[i] - i == column - ocuppied_rows or                 positions[i] + i == column + ocuppied_rows:

                return False
        return True

    def show_full_board(self, positions):
        
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += " 1 "
                else:
                    line += " 0 "
            print(line)
        print("\n")

    def show_short_board(self, positions):
        
        line = ""
        for i in range(self.size):
            line += str(positions[i]) + " "
        print(line)

def main():
   #Enter number of queens
    NQueens(4)

class NQueens:
    def __init__(self, size):
        
        self.size = size
        self.solutions = 0
        self.solve()

    def solve(self):
        
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        print("Found", self.solutions, "solutions.")

    def put_queen(self, positions, target_row):
        
        if target_row == self.size:
            self.show_full_board(positions)
           
            self.solutions += 1
        else:
           
            for column in range(self.size):
               
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)


    def check_place(self, positions, ocuppied_rows, column):

        for i in range(ocuppied_rows):
            if positions[i] == column or                 positions[i] - i == column - ocuppied_rows or                 positions[i] + i == column + ocuppied_rows:

                return False
        return True

    def show_full_board(self, positions):
        
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += " 1 "
                else:
                    line += " 0 "
            print(line)
        print("\n")

    def show_short_board(self, positions):
        
        line = ""
        for i in range(self.size):
            line += str(positions[i]) + " "
        print(line)

def main():
   #Enter number of queens
    NQueens(4)

if __name__ == "__main__":

    main()


# In[ ]:





# In[10]:


global N
N = 4
from typing import List # For annotations

boardcnt = 0
solutionCount = 0

def IsBoardOk (chessboard : List, row : int, col : int) :

   # Check if there is a queen '1' positioned to the left of column col on the same row.
   for c in range(col) :
       if (chessboard[row][c] == '1') :
           return False

   # Check if there is queen '1' positioned on the upper left diagonal
   for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)) :
       if (chessboard[r][c] == '1') :
           return False

   # Check if there is queen '1' positioned on the lower left diagonal
   for r, c in zip(range(row+1, len(chessboard), 1), range(col-1, -1, -1)) :
      if (chessboard[r][c] == '1') :
          return False

   return True

def DisplayBoard (chessboard : List) :

    for row in chessboard :
        print(row)

def PlaceNQueens (chessboard : List, col : int) :

    # If all the columns have a queen '1', a solution has been found.
    global boardcnt

    if (col >= len(chessboard)) :

        boardcnt += 1

        print("Solution " + str(boardcnt))
        DisplayBoard(chessboard)
        print("\n")

    else :

        # Else try placing the queen on each row of the column and check if the chessboard remains OK.
        for row in range(len(chessboard)) :

            chessboard[row][col] = '1'

            if (IsBoardOk(chessboard, row, col) == True) :
                # Chess board was OK, hence try placing the queen '1' in the next column.
                PlaceNQueens(chessboard, col + 1)

            chessboard[row][col] = '0'; # As previously placed queen was not valid, restore '0'

def main() :

   chessboard = []

   for i in range(N) :
       row = ["0"] * N
       chessboard.append(row)

   # Start placing the queen '1' from the 0'th column.
   PlaceNQueens(chessboard, 0)

if __name__ == "__main__" :
    main()


# In[ ]:




