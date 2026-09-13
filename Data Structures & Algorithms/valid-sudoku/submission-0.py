class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        hash_set_r = collections.defaultdict(set)
        hash_set_c = collections.defaultdict(set)
        hash_set_t = collections.defaultdict(set)
       
    
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue

                if board[r][c] in hash_set_r[r]:
                    return False
                hash_set_r[r].add(board[r][c])

                if board[r][c] in hash_set_c[c]:
                    return False
                hash_set_c[c].add(board[r][c])
               
                if board[r][c] in hash_set_t[r//3,c//3]:
                    return False
                hash_set_t[r//3,c//3].add(board[r][c]) 
                

        return True
               