list = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo):
	"""Solves the puzzle."""
	empty = _find_next_empty(bo)
	if not empty:
		return True
	else:
		row, col = empty

	for i in range(1, 10):
		if _validifier(bo, i, (row, col)):
			bo[row][col] = i

			if solve(bo):
				return True
	
			bo[row][col] = 0

	return False

def _validifier(bo, num, pos):
	"""Checks if position is valid."""
	# Checking column.
	for i in range(len(bo[0])):
		if bo[pos[0]][i] == num:
			return False

	# Checking row.
	for i in range(len(bo)):
		if bo[i][pos[1]] == num:
			return False

	# Checking 3x3 box.
	box_x = pos[1] // 3
	box_y = pos[0] // 3

	for i in range((box_y * 3), (box_y * 3) + 3):
		for j in range((box_x * 3), (box_x * 3) + 3):
			if bo[i][j] == num:
				return False

	return True

def _find_next_empty(bo):
	"""Locates the next empty position."""
	for i in range(len(bo)):
		for j in range(len(bo[0])):
			if bo[i][j] == 0:
				return (i, j)
	return False

def _print_board(bo):
	"""Prints the board onto the terminal."""
	for i in range(len(bo)):
		if i % 3 == 0 and i != 0:
			print("- - - - - - - - - - - -")
		for j in range (len(bo[0])):
			if j % 3 == 0 and j != 0:
				print(" | ", end= "")
			
			if j == 8:
				print(bo[i][j])
			else:
				print(str(bo[i][j]) + " ", end= "")

# print("\n~~~ Unsolved Puzzle ~~~\n")
# _print_board(list)
# print("\n\n~~~ Solved Puzzle ~~~\n")
# solve(list)
# _print_board(list)