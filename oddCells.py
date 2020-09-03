class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row = n
        column = m
        matrix_i = list()
        for i in range(row):
            row_list = [0] * column
            matrix_i.append(row_list)
        
        for ri,ci in indices:
            for rii, row in enumerate(matrix_i):
                row = matrix_i[rii]
                if rii == ri:
                    row = [x + 1 for x in row ]
                for cii, column in enumerate(row):
                    if cii == ci:
                        row[cii] = row[cii] + 1
                matrix_i[rii] = row
        
        count = 0
        for row in matrix_i:
            count += sum((x%2 for x in row))
        
        return count
