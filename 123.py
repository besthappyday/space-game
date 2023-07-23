 
# 迷宮地圖
# 迷宮地圖
import time

# 迷宮地圖
# 迷宮地圖
map = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

# 迷宮遊戲角色
player = 'S'  # 初始位置
end = 'E'  # 終點位置

# 找到玩家的初始位置
player_row, player_col = None, None
for row in range(len(map)):
    for col in range(len(map[row])):
        if map[row][col] == player:
            player_row, player_col = row, col
            break

# 遊戲迴圈
while True:
    # 顯示迷宮地圖
    for row in map:
        print(' '.join(row))
    print()

    # 讓玩家輸入移動方向
    move = input("請輸入移動方向（w:上, s:下, a:左, d:右）：")

    # 根據玩家的移動方向更新位置
    new_player_row, new_player_col = player_row, player_col
    if move == 'w':  # 上
        new_player_row -= 1
    elif move == 's':  # 下
        new_player_row += 1
    elif move == 'a':  # 左
        new_player_col -= 1
    elif move == 'd':  # 右
        new_player_col += 1

    # 檢查是否可以移動到新位置
    if map[new_player_row][new_player_col] != '#':
        # 更新玩家位置
        map[player_row][player_col] = ' '
        player_row, player_col = new_player_row, new_player_col
        map[player_row][player_col] = player

    # 檢查遊戲是否結束
    if map[player_row][player_col] == end:
        print("winning")
        break