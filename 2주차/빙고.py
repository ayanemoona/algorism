# 빙고판 입력
bingo_board = [list(map(int, input().split())) for _ in range(5)]

# 사회자가 부르는 숫자 입력
called_numbers = []
for _ in range(5):
    called_numbers.extend(list(map(int, input().split())))

# 빙고판의 숫자를 제거하고 빙고 개수를 확인하는 함수
def check_bingo(board):
    bingo_count = 0
    
    # 행 빙고
    for row in board:
        if sum(row) == 0:
            bingo_count += 1

    # 열 빙고
    for col in range(5):
        if sum(board[row][col] for row in range(5)) == 0:
            bingo_count += 1

    # 대각선 빙고
    if sum(board[i][i] for i in range(5)) == 0:
        bingo_count += 1
    if sum(board[i][4 - i] for i in range(5)) == 0:
        bingo_count += 1

    return bingo_count

# 사회자의 숫자를 하나씩 부르며 빙고판 갱신
for idx, number in enumerate(called_numbers, 1):
    # 빙고판에서 숫자 제거
    for row in range(5):
        for col in range(5):
            if bingo_board[row][col] == number:
                bingo_board[row][col] = 0
    
    # 빙고 개수 확인
    if check_bingo(bingo_board) >= 3:
        print(idx)  # 몇 번째 호출에서 빙고가 완성되었는지 출력
        break
