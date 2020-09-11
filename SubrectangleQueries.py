
import copy

class SubrectangleQueries:

    #def __init__(self, rectangle: List[List[int]]):
    def __init__(self, rectangle):
        self.rect = copy.deepcopy(rectangle)

    #def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
    def updateSubrectangle(self, row1, col1, row2, col2, newValue) -> None:
        print (row1)
        print (row2)
        for row in range(row1,row2+1):
            for col in range(col1,col2+1):
                print (f'newValue= {newValue}') 
                print (row)
                print (f'col= {col}') 
                self.rect[row][col] = newValue
        return None

    #def getValue(self, row: int, col: int) -> int:
    def getValue(self, row, col) -> int:
        return self.rect[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
    
rectangle = [[1,2,1],[4,3,4],[3,2,1],[1,1,1]]
obj = SubrectangleQueries(rectangle)

row1,col1,row2,col2,newValue = 0,0,3,2,5
#obj.updateSubrectangle(row1,col1,row2,col2,newValue)

row = 0
col = 2
param_2 = obj.getValue(row,col)
    
'''
row1,col1,row2,col2,newValue = 3, 0, 3, 2, 10
obj.updateSubrectangle(row1,col1,row2,col2,newValue)

#print (obj.getValue(3, 1))

    def __init__(self, rectangle: List[List[int]]):
        self.r = copy.deepcopy(rectangle) # deep copy the input array - credit to @_xavier_
        self.histories = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.histories.append([row1, col1, row2, col2, newValue])

    def getValue(self, row: int, col: int) -> int:
        for his in reversed(self.histories):
            if his[0] <= row <= his[2] and his[1] <= col <= his[3]:
                return his[4]
        return self.r[row][col]
  '''
