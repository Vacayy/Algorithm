# 문제: 숙제하기 싫을 때 (골드 4)
'''
1 4 6 3 1 4 6 3 .. 
                      5


1 ~ 6까지 각각 상하좌우 입력해놓기
'''
import sys
input = sys.stdin.readline()

square = {1: [5, 2, 4, 3],
          2: [1, 6, 4, 3],
          3: [5, 2, 1, 6],
          4: [6, 1, 2, 5],
          5: []}

