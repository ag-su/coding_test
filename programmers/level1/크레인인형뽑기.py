def solution(board, moves):
    answer = 0
    lst_result = []
    for j in moves:
        for i in range(len(board)): 
            if board[i][j-1] != 0: 
                lst_result.append(board[i][j-1])
                board[i][j-1] = 0
                if (len(lst_result)>=2) and (lst_result[-2] == lst_result[-1]):
                    del lst_result[-2:]
                    answer += 2
                break  
        
    return answer


# 참고할 만한 풀이 
# def solution(board, moves):
#     cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
#     a, s = 0, [0]

#     for m in moves:
#         if len(cols[m - 1]) > 0:
#             if (d := cols[m - 1].pop(0)) == (l := s.pop()): # python version 3 이상 
#                 a += 2
#             else:
#                 s.extend([l, d])

#     return a    


board =[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board=board, moves=moves)