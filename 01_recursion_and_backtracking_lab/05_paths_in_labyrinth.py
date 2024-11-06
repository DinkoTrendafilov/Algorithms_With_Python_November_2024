def paths_in_labyrinth(row, col, direction, lab, path):
    if row < 0 or row >= len(lab) or col < 0 or col >= len(lab[0]):
        return

    if lab[row][col] == "*":
        return

    path.append(direction)

    if lab[row][col] == "e":
        print("".join(path))

    elif lab[row][col] == "-":
        lab[row][col] = "v"
        paths_in_labyrinth(row, col + 1, "R", lab, path)
        paths_in_labyrinth(row, col - 1, "L", lab, path)
        paths_in_labyrinth(row + 1, col, "D", lab, path)
        paths_in_labyrinth(row - 1, col, "U", lab, path)
        lab[row][col] = "-"

    path.pop()


rows = int(input())
columns = int(input())
lab = [[el for el in input()] for _ in range(rows)]
paths_in_labyrinth(0, 0, "", lab, [])
