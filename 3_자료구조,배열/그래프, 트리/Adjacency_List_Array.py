'''
그래프를 표현하는 기법 중 인접 리스트, 인접 행렬법을 각각 연습해본다.
(Introduction to Algorithms의 p.602 - 그림 22.1, 22.2 참고)
'''


# 인접 리스트법을 통한 무방향 그래프 표현 (그림 22.1)
graph = {1: [2, 5],
         2: [1, 5, 3, 4],
         3: [2, 4],
         4: [2, 5, 3],
         5: [4, 1, 2]}

# 인접 리스트법을 통한 방향 그래프 표현 (그림 22.2)
graph = {1: [2, 4],
         2: [5],
         3: [5, 6],
         4: [2],
         5: [4],
         6: [6]}



# 인접 행렬법을 통한 무방향 그래프 표현 (그림 22.1)
graph = [[0, 1, 0, 0, 1],
         [1, 0, 1, 1, 1],
         [0, 1, 0, 1, 0],
         [0, 1, 1, 0, 1],
         [1, 1, 0, 1, 0]]

# 인접 행렬법을 통한 방향 그래프 표현 (그림 22.2)
graph = [[0, 1, 0, 1, 1, 0],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1],
         [0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1]]






