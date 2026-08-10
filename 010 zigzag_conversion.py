#The string "PAYPALISHIRING" is written in a zigzag 
# pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)
#  P A H N A P L S I I G Y I R And then read line by line: "PAHNAPLSIIGYIR"
#  Write the code that will take a string and make this conversion given a number of ro

class Solution:
    def convert(self, s: str, numRows: int) -> str:
            
        if numRows == 1 or numRows >= len(s):
            return s

        
        rows = [""] * numRows

        currentRow = 0
        direction = 1   

    
        for ch in s:
            rows[currentRow] += ch

        
            if currentRow == 0:
                direction = 1
            elif currentRow == numRows - 1:
                direction = -1

            currentRow += direction

    
        return "".join(rows)