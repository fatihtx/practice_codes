class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        new_matrix = copy.deepcopy(A)
        for row in range(len(A)):
            for column_t in range(len(A[row])-1,-1,-1):
                new_matrix[row][len(A[row])-1-column_t] = 0 if A[row][column_t] else 1 
        return new_matrix
