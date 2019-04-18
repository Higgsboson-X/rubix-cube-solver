from capture import CaptureCube
from display import DisplayCube

from cube import *
from test import *

def run_solver():

	capture_cube = CaptureCube()
	capture_cube.capture_cube()

	capture_state = capture_cube._cube

	state = {}
	for face in ['U', 'D', 'F', 'B', 'L', 'R']:
		state[face] = [[capture_state[face][(i, j)] for j in range(3)] for i in range(3)]

	display_cube = DisplayCube(state)
	display_cube.display_pieces()
	print('>>>>>>> Initial State <<<<<<<')
	display_cube.print_cube()
	display_cube.solve()
	display_cube.print_cube()

	display_cube.display_sequence_algorithm(display_cube._actions)



def test_display_cube_solve():

	display_cube = DisplayCube(TEST_STATE)
	display_cube.display_pieces()
	print('>>>>>>> Initial State <<<<<<<')
	display_cube.print_cube()
	display_cube.solve()
	display_cube.print_cube()

	display_cube.display_sequence_algorithm(display_cube._actions)



if __name__ == '__main__':

	# test_display_cube_solve()
	run_solver()