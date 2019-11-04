def main():
    N, M, B = map(int, input().split())
    game_map = [[0] * N for _ in range(N)]
    goal_position = list(map(int, input().split()))
    game_map[goal_position[0]][goal_position[1]] = 5
    robot_positions = []
    robot_directions = []
    for _ in range(M):
        input_value = input().split()
        robot_positions.append([int(input_value[0]), int(input_value[1])])
        robot_directions.append(input_value[2])
        game_map[int(input_value[0])][int(input_value[1])] = 1

    block_positions = []
    for _ in range(B):
        input_value = list(map(int, input().split()))
        block_positions.append([int(input_value[0]), int(input_value[1])])
        game_map[input_value[0]][input_value[1]] = 9


if __name__ == '__main__':
    main()
