from cube import Cube


STATE_0 = {
	'B': [['r', 'g', 'o'], ['w', 'o', 'o'], ['r', 'w', 'g']],
    'D': [['w', 'r', 'b'], ['o', 'y', 'o'], ['r', 'b', 'y']],
    'F': [['b', 'y', 'g'], ['y', 'r', 'r'], ['b', 'y', 'o']],
    'L': [['y', 'r', 'r'], ['b', 'g', 'o'], ['w', 'g', 'o']],
    'R': [['w', 'b', 'b'], ['b', 'b', 'g'], ['y', 'w', 'g']],
    'U': [['g', 'r', 'y'], ['w', 'w', 'y'], ['w', 'g', 'o']]
}

STATE_1 = {
	'B': [['y', 'o', 'g'], ['o', 'o', 'r'], ['r', 'y', 'g']],
    'D': [['b', 'o', 'y'], ['y', 'y', 'y'], ['w', 'g', 'w']],
    'F': [['y', 'r', 'r'], ['r', 'r', 'o'], ['o', 'y', 'b']],
    'L': [['r', 'g', 'o'], ['g', 'g', 'b'], ['o', 'r', 'w']],
    'R': [['g', 'b', 'r'], ['g', 'b', 'b'], ['o', 'b', 'b']],
    'U': [['w', 'w', 'b'], ['w', 'w', 'w'], ['g', 'w', 'y']]
}

STATE_2 = {
	'B': [['o', 'o', 'o'], ['g', 'o', 'b'], ['y', 'g', 'r']],
    'D': [['b', 'r', 'g'], ['y', 'y', 'b'], ['y', 'y', 'o']],
    'F': [['r', 'r', 'r'], ['y', 'r', 'b'], ['y', 'g', 'r']],
    'L': [['g', 'g', 'g'], ['o', 'g', 'r'], ['b', 'o', 'o']],
    'R': [['b', 'b', 'b'], ['r', 'b', 'o'], ['y', 'y', 'g']],
    'U': [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
}

STATE_3 = {
	'B': [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'g', 'y']],
    'D': [['r', 'b', 'y'], ['o', 'y', 'y'], ['b', 'y', 'g']],
    'F': [['r', 'r', 'r'], ['r', 'r', 'r'], ['g', 'y', 'b']],
    'L': [['g', 'g', 'g'], ['g', 'g', 'g'], ['r', 'y', 'y']],
    'R': [['b', 'b', 'b'], ['b', 'b', 'b'], ['o', 'r', 'y']],
    'U': [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
}

STATE_4 = {
	'B': [['o', 'o', 'o'], ['o', 'o', 'o'], ['g', 'b', 'r']],
    'D': [['g', 'y', 'o'], ['y', 'y', 'y'], ['y', 'y', 'y']],
    'F': [['r', 'r', 'r'], ['r', 'r', 'r'], ['y', 'o', 'y']],
    'L': [['g', 'g', 'g'], ['g', 'g', 'g'], ['b', 'g', 'r']],
    'R': [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'r', 'o']],
    'U': [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
}

STATE_5 = {
	'B': [['o', 'o', 'o'], ['o', 'o', 'o'], ['g', 'o', 'y']],
    'D': [['o', 'y', 'r'], ['y', 'y', 'y'], ['o', 'y', 'r']],
    'F': [['r', 'r', 'r'], ['r', 'r', 'r'], ['y', 'r', 'b']],
    'L': [['g', 'g', 'g'], ['g', 'g', 'g'], ['b', 'g', 'g']],
    'R': [['b', 'b', 'b'], ['b', 'b', 'b'], ['y', 'b', 'y']],
    'U': [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
}

STATE_6 = {
	'B': [['o', 'o', 'o'], ['o', 'o', 'o'], ['y', 'o', 'o']],
    'D': [['g', 'y', 'r'], ['y', 'y', 'y'], ['y', 'y', 'b']],
    'F': [['r', 'r', 'r'], ['r', 'r', 'r'], ['y', 'r', 'b']],
    'L': [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'r']],
    'R': [['b', 'b', 'b'], ['b', 'b', 'b'], ['y', 'b', 'o']],
    'U': [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
}


TEST_STATE = {
	'B': [['b', 'g', 'g'], ['b', 'o', 'y'], ['o', 'r', 'g']],
    'D': [['w', 'b', 'o'], ['y', 'y', 'r'], ['y', 'y', 'b']],
    'F': [['o', 'b', 'g'], ['o', 'r', 'o'], ['r', 'y', 'w']],
    'L': [['o', 'r', 'y'], ['g', 'g', 'g'], ['r', 'o', 'b']],
    'R': [['r', 'o', 'y'], ['b', 'b', 'r'], ['g', 'g', 'w']],
    'U': [['y', 'w', 'r'], ['w', 'w', 'w'], ['b', 'w', 'w']]
}



def test_solve_white_edges(cube):

	print('stage: ', cube.get_cur_stage());
	print('confirm 0: ', True)

	cube.solve_white_edges()

	print('stage: ', cube.get_cur_stage());
	print('confirm 1: ', cube.is_stage_finish_white_edges())

	cube.print_cube()


def test_solve_white_corners(cube):

	print('stage: ', cube.get_cur_stage());
	print('confirm 1: ', cube.is_stage_finish_white_edges())

	cube.solve_white_corners()

	print('stage: ', cube.get_cur_stage());
	print('confirm 2: ', cube.is_stage_finish_white_corners())

	cube.print_cube()


def test_solve_middle_layer(cube):

	print('stage: ', cube.get_cur_stage());
	print('confirm 2: ', cube.is_stage_finish_white_corners())

	cube.solve_middle_layer()

	print('stage: ', cube.get_cur_stage());
	print('confirm 3: ', cube.is_stage_finish_middle_layer())

	cube.print_cube()


def test_solve_yellow_cross(cube):

	print('stage: ', cube.get_cur_stage());
	print('confirm 3: ', cube.is_stage_finish_middle_layer())

	cube.solve_yellow_cross()

	print('stage: ', cube.get_cur_stage());
	print('confirm 4: ', cube.is_stage_finish_yellow_cross())

	cube.print_cube()


def test_solve_yellow_edges(cube):

	print('stage: ', cube.get_cur_stage());
	print('confirm 4: ', cube.is_stage_finish_yellow_cross())

	cube.solve_yellow_edges()

	print('stage: ', cube.get_cur_stage());
	print('confirm 5: ', cube.is_stage_finish_yellow_edges())

	cube.print_cube()


def test_solve_position_yellow_corners(cube):

	print('stage: ', cube.get_cur_stage());
	print('confirm 5: ', cube.is_stage_finish_yellow_edges())

	cube.solve_position_yellow_corners()

	print('stage: ', cube.get_cur_stage());
	print('confirm 6: ', cube.is_stage_finish_position_yellow_corners())

	cube.print_cube()


def test_solve_orient_yellow_corners(cube):

	print('stage: ', cube.get_cur_stage());
	print('confirm 6: ', cube.is_stage_finish_position_yellow_corners())

	cube.solve_orient_yellow_corners()

	print('stage: ', cube.get_cur_stage());
	print('confirm 7: ', cube.is_stage_finish_orient_yellow_corners())

	cube.print_cube()



def test_solve_with_known_state():

	cube = Cube(STATE_6)
	cube.print_cube()

	# cube.shuffle(10)
	# cube.print_cube()

	stage = cube.get_cur_stage()
	print(stage)

	if stage == 0:
		test_solve_white_edges(cube)
	elif stage == 1:
		test_solve_white_corners(cube)
	elif stage == 2:
		test_solve_middle_layer(cube)
	elif stage == 3:
		test_solve_yellow_cross(cube)
	elif stage == 4:
		test_solve_yellow_edges(cube)
	elif stage == 5:
		test_solve_position_yellow_corners(cube)
	elif stage == 6:
		test_solve_orient_yellow_corners(cube)
	elif stage == 7:
		print('done')



def test_solve_with_random_state():

	cube = Cube()

	cube.shuffle(50)
	cube.print_cube()

	stage = cube.get_cur_stage()
	print(stage)

	cube.solve()
	cube.print_cube()


def test_solve_with_test_state():

	cube = Cube(TEST_STATE)
	cube.print_cube()

	stage = cube.get_cur_stage()
	print('initial stage: ', stage)

	cube.solve()
	cube.print_cube()



def test_rotate():

	cube = Cube()
	cube.print_cube()

	action = raw_input('action: ')
	while action != 'q':
		cube.rotate(action)
		cube.print_cube()
		action = raw_input('action: ')



if __name__ == '__main__':

	# test_rotate()
	# test_solve_with_test_state()
	test_solve_with_test_state()
