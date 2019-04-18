# rubiks cube class

'''

	U: white
	D: yellow
	F: red
	B: orange
	L: green
	R: blue

'''

import pprint
import random


ACTIONS = ['U+', 'U-', 'D+', 'D-', 'F+', 'F-', 'B+', 'B-', 'L+', 'L-', 'R+', 'R-']
INITIAL = {'U': [['w', 'w', 'w'],
				 ['w', 'w', 'w'],
				 ['w', 'w', 'w']],
		   'D': [['y', 'y', 'y'],
				 ['y', 'y', 'y'],
				 ['y', 'y', 'y']],
		   'F': [['r', 'r', 'r'],
				 ['r', 'r', 'r'],
				 ['r', 'r', 'r']],
		   'B': [['o', 'o', 'o'],
				 ['o', 'o', 'o'],
				 ['o', 'o', 'o']],
		   'L': [['g', 'g', 'g'],
				 ['g', 'g', 'g'],
				 ['g', 'g', 'g']],
		   'R': [['b', 'b', 'b'],
				 ['b', 'b', 'b'],
				 ['b', 'b', 'b']]}

CLOCKWISE = {
	'+': {
		(0, 0): (0, 2),
		(0, 1): (1, 2),
		(0, 2): (2, 2),
		(1, 0): (0, 1),
		(1, 1): (1, 1),
		(1, 2): (2, 1),
		(2, 0): (0, 0),
		(2, 1): (1, 0),
		(2, 2): (2, 0)
	},
	'-': {
		(0, 0): (2, 0),
		(0, 1): (1, 0),
		(0, 2): (0, 0),
		(1, 0): (2, 1),
		(1, 1): (1, 1),
		(1, 2): (0, 1),
		(2, 0): (2, 2),
		(2, 1): (1, 2),
		(2, 2): (0, 2)
	}
}


FACE2COR = {
	'F': 'r',
	'L': 'g', 
	'B': 'o',
	'R': 'b',
	'U': 'w',
	'D': 'y'
}

COR2FACE = {
	'r': 'F',
	'g': 'L', 
	'o': 'B',
	'b': 'R',
	'w': 'U',
	'y': 'D'
}

class Cube:

	def __init__(self, state = INITIAL):

		self._state = {}
		for face in ['U', 'D', 'F', 'B', 'L', 'R']:
			self._state[face] = [[state[face][i][j] for j in range(3)] for i in range(3)]

		self._actions = []
		self._stage = 0


	def print_cube(self):

		printer = pprint.PrettyPrinter(indent=4)
		print('State: ')
		printer.pprint(self._state)
		print('Actions: ')
		print(self._actions)


	def shuffle(self, n):

		for i in range(n):
			action = random.choice(['U', 'D', 'F', 'L', 'B', 'R']) + random.choice(['+', '-'])
			self.rotate(action)


	def clone_state(self):

		copy = {}

		for face in ['U', 'D', 'F', 'B', 'L', 'R']:
			copy[face] = [[self._state[face][i][j] for j in range(3)] for i in range(3)]

		return copy


	def rotate(self, action):

		copy = self.clone_state()
		self._actions.append(action)

		# action: an action in ACTIONS
		if action == 'U+':
			self._state['F'][0] = [copy['R'][0][j] for j in range(3)]
			self._state['L'][0] = [copy['F'][0][j] for j in range(3)]
			self._state['B'][0] = [copy['L'][0][j] for j in range(3)]
			self._state['R'][0] = [copy['B'][0][j] for j in range(3)]

			'''
			self._state['U'][0][0] = copy['U'][2][0]
			self._state['U'][0][1] = copy['U'][1][0]
			self._state['U'][0][2] = copy['U'][0][0]
			self._state['U'][1][0] = copy['U'][2][1]
			self._state['U'][1][1] = copy['U'][1][1]
			self._state['U'][1][2] = copy['U'][0][1]
			self._state['U'][2][0] = copy['U'][2][2]
			self._state['U'][2][1] = copy['U'][1][2]
			self._state['U'][2][2] = copy['U'][0][2]
			'''

			for pos in CLOCKWISE['+']:
				self._state['U'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['U'][pos[0]][pos[1]]

		elif action == 'U-':
			self._state['F'][0] = [copy['L'][0][j] for j in range(3)]
			self._state['L'][0] = [copy['B'][0][j] for j in range(3)]
			self._state['B'][0] = [copy['R'][0][j] for j in range(3)]
			self._state['R'][0] = [copy['F'][0][j] for j in range(3)]

			'''
			self._state['U'][0][0] = copy['U'][0][2]
			self._state['U'][0][1] = copy['U'][1][2]
			self._state['U'][0][2] = copy['U'][2][2]
			self._state['U'][1][0] = copy['U'][0][1]
			self._state['U'][1][1] = copy['U'][1][1]
			self._state['U'][1][2] = copy['U'][2][1]
			self._state['U'][2][0] = copy['U'][0][0]
			self._state['U'][2][1] = copy['U'][1][0]
			self._state['U'][2][2] = copy['U'][2][0]
			'''

			for pos in CLOCKWISE['-']:
				self._state['U'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['U'][pos[0]][pos[1]]


		elif action == 'D+':
			self._state['F'][2] = [copy['L'][2][j] for j in range(3)]
			self._state['L'][2] = [copy['B'][2][j] for j in range(3)]
			self._state['B'][2] = [copy['R'][2][j] for j in range(3)]
			self._state['R'][2] = [copy['F'][2][j] for j in range(3)]

			for pos in CLOCKWISE['+']:
				self._state['D'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['D'][pos[0]][pos[1]]

		elif action == 'D-':
			self._state['F'][2] = [copy['R'][2][j] for j in range(3)]
			self._state['L'][2] = [copy['F'][2][j] for j in range(3)]
			self._state['B'][2] = [copy['L'][2][j] for j in range(3)]
			self._state['R'][2] = [copy['B'][2][j] for j in range(3)]

			for pos in CLOCKWISE['-']:
				self._state['D'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['D'][pos[0]][pos[1]]


		elif action == 'F+':
			self._state['U'][2] = [copy['L'][2 - i][2] for i in range(3)]

			self._state['L'][0][2] = copy['D'][0][0]
			self._state['L'][1][2] = copy['D'][0][1]
			self._state['L'][2][2] = copy['D'][0][2]

			self._state['D'][0] = [copy['R'][2 - i][0] for i in range(3)]

			self._state['R'][0][0] = copy['U'][2][0]
			self._state['R'][1][0] = copy['U'][2][1]
			self._state['R'][2][0] = copy['U'][2][2]

			for pos in CLOCKWISE['+']:
				self._state['F'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['F'][pos[0]][pos[1]]

		elif action == 'F-':
			self._state['U'][2] = [copy['R'][i][0] for i in range(3)]

			self._state['R'][0][0] = copy['D'][0][2]
			self._state['R'][1][0] = copy['D'][0][1]
			self._state['R'][2][0] = copy['D'][0][0]

			self._state['D'][0] = [copy['L'][i][2] for i in range(3)]

			self._state['L'][0][2] = copy['U'][2][2]
			self._state['L'][1][2] = copy['U'][2][1]
			self._state['L'][2][2] = copy['U'][2][0]

			for pos in CLOCKWISE['-']:
				self._state['F'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['F'][pos[0]][pos[1]]

		elif action == 'B+':
			self._state['U'][0] = [copy['R'][i][2] for i in range(3)]

			self._state['R'][0][2] = copy['D'][2][2]
			self._state['R'][1][2] = copy['D'][2][1]
			self._state['R'][2][2] = copy['D'][2][0]

			self._state['D'][2] = [copy['L'][i][0] for i in range(3)]

			self._state['L'][0][0] = copy['U'][0][2]
			self._state['L'][1][0] = copy['U'][0][1]
			self._state['L'][2][0] = copy['U'][0][0]

			for pos in CLOCKWISE['+']:
				self._state['B'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['B'][pos[0]][pos[1]]

		elif action == 'B-':
			self._state['U'][0] = [copy['L'][2 - i][0] for i in range(3)]

			self._state['L'][0][0] = copy['D'][2][0]
			self._state['L'][1][0] = copy['D'][2][1]
			self._state['L'][2][0] = copy['D'][2][2]

			self._state['D'][2] = [copy['R'][2 - i][2] for i in range(3)]

			self._state['R'][0][2] = copy['U'][0][0]
			self._state['R'][1][2] = copy['U'][0][1]
			self._state['R'][2][2] = copy['U'][0][2]

			for pos in CLOCKWISE['-']:
				self._state['B'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['B'][pos[0]][pos[1]]


		elif action == 'L+':
			for i in range(3):
				self._state['F'][i][0] = copy['U'][i][0]
				self._state['U'][i][0] = copy['B'][2 - i][2]
				self._state['B'][i][2] = copy['D'][2 - i][0]
				self._state['D'][i][0] = copy['F'][i][0]

			for pos in CLOCKWISE['+']:
				self._state['L'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['L'][pos[0]][pos[1]]

		elif action == 'L-':
			for i in range(3):
				self._state['F'][i][0] = copy['D'][i][0]
				self._state['D'][i][0] = copy['B'][2 - i][2]
				self._state['B'][i][2] = copy['U'][2 - i][0]
				self._state['U'][i][0] = copy['F'][i][0]

			for pos in CLOCKWISE['-']:
				self._state['L'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['L'][pos[0]][pos[1]]


		elif action == 'R+':
			for i in range(3):
				self._state['F'][i][2] = copy['D'][i][2]
				self._state['D'][i][2] = copy['B'][2 - i][0]
				self._state['B'][i][0] = copy['U'][2 - i][2]
				self._state['U'][i][2] = copy['F'][i][2]

			for pos in CLOCKWISE['+']:
				self._state['R'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['R'][pos[0]][pos[1]]

		elif action == 'R-':
			for i in range(3):
				self._state['F'][i][2] = copy['U'][i][2]
				self._state['U'][i][2] = copy['B'][2 - i][0]
				self._state['B'][i][0] = copy['D'][2 - i][2]
				self._state['D'][i][2] = copy['F'][i][2]

			for pos in CLOCKWISE['-']:
				self._state['R'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['R'][pos[0]][pos[1]]


	def sequence_algorithm(self, seq):

		for action in seq:
			self.rotate(action)

	# ============================================================================================================================================= #

	'''

		stage:
			0. start: mixed
			1. white edges: white cross have been solved
			2. white corners: white face
			3. middle layer: middle layer solved
			4. yellow cross: yellow cross formed
			5. yellow edges: yellow edges formed
			6. position yellow corners: corner positions are correct
			7. orient yellow corners: corner orientations are correct (done)

	'''
	def is_stage_finish_orient_yellow_corners(self):

		# done
		return self._state == INITIAL


	def is_stage_finish_position_yellow_corners(self):

		if self._state['U'] != INITIAL['U']:
			return False

		if self._state['F'][:2] != INITIAL['F'][:2] or \
		   self._state['L'][:2] != INITIAL['L'][:2] or \
		   self._state['B'][:2] != INITIAL['B'][:2] or \
		   self._state['R'][:2] != INITIAL['R'][:2]:
			return False
		
		if self._state['F'][2][1] != INITIAL['F'][2][1] or \
		   self._state['L'][2][1] != INITIAL['L'][2][1] or \
		   self._state['B'][2][1] != INITIAL['B'][2][1] or \
		   self._state['R'][2][1] != INITIAL['R'][2][1]:
			return False

		if (not self._state['F'][2][0] in ['r', 'g', 'y'] or not self._state['F'][2][2] in ['r', 'b', 'y']) or \
		   (not self._state['L'][2][0] in ['g', 'o', 'y'] or not self._state['L'][2][2] in ['g', 'r', 'y']) or \
		   (not self._state['B'][2][0] in ['o', 'b', 'y'] or not self._state['B'][2][2] in ['o', 'g', 'y']) or \
		   (not self._state['R'][2][0] in ['b', 'r', 'y'] or not self._state['R'][2][2] in ['b', 'o', 'y']) or \
		   (not self._state['D'][0][0] in ['y', 'g', 'r'] or not self._state['D'][0][2] in ['y', 'r', 'b'] or not self._state['D'][2][0] in ['y', 'g', 'o'] or not self._state['D'][2][2] in ['y', 'o', 'b']):
			return False

		if not self._state['D'][1][0] == self._state['D'][0][1] == self._state['D'][2][1] == self._state['D'][1][2] == 'y':
			return False

		return True


	def is_stage_finish_yellow_edges(self):

		if self._state['U'] != INITIAL['U']:
			return False

		if self._state['F'][:2] != INITIAL['F'][:2] or \
		   self._state['L'][:2] != INITIAL['L'][:2] or \
		   self._state['B'][:2] != INITIAL['B'][:2] or \
		   self._state['R'][:2] != INITIAL['R'][:2]:
			return False
		
		if self._state['F'][2][1] != INITIAL['F'][2][1] or \
		   self._state['L'][2][1] != INITIAL['L'][2][1] or \
		   self._state['B'][2][1] != INITIAL['B'][2][1] or \
		   self._state['R'][2][1] != INITIAL['R'][2][1]:
			return False

		if not self._state['D'][1][0] == self._state['D'][0][1] == self._state['D'][2][1] == self._state['D'][1][2] == 'y':
			return False

		return True


	def is_stage_finish_yellow_cross(self):

		if self._state['U'] != INITIAL['U']:
			return False

		if self._state['F'][:2] != INITIAL['F'][:2] or \
		   self._state['L'][:2] != INITIAL['L'][:2] or \
		   self._state['B'][:2] != INITIAL['B'][:2] or \
		   self._state['R'][:2] != INITIAL['R'][:2]:
			return False

		if not self._state['D'][1][0] == self._state['D'][0][1] == self._state['D'][2][1] == self._state['D'][1][2] == 'y':
			return False

		return True


	def is_stage_finish_middle_layer(self):

		if self._state['U'] != INITIAL['U']:
			return False

		if self._state['F'][:2] != INITIAL['F'][:2] or \
		   self._state['L'][:2] != INITIAL['L'][:2] or \
		   self._state['B'][:2] != INITIAL['B'][:2] or \
		   self._state['R'][:2] != INITIAL['R'][:2]:
			return False

		return True


	def is_stage_finish_white_corners(self):

		if self._state['U'] != INITIAL['U']:
			return False

		if self._state['F'][0] != INITIAL['F'][0] or \
		   self._state['L'][0] != INITIAL['L'][0] or \
		   self._state['B'][0] != INITIAL['B'][0] or \
		   self._state['R'][0] != INITIAL['R'][0]:
			return False

		return True


	def is_stage_finish_white_edges(self):

		if not self._state['U'][0][1] == self._state['U'][1][0] == self._state['U'][2][1] == self._state['U'][1][2] == 'w':
			return False

		if self._state['F'][0][1] != INITIAL['F'][0][1] or \
		   self._state['L'][0][1] != INITIAL['L'][0][1] or \
		   self._state['B'][0][1] != INITIAL['B'][0][1] or \
		   self._state['R'][0][1] != INITIAL['R'][0][1]:
			return False

		return True



	def get_cur_stage(self):

		# mixed

		# finish white edges
		if not self._state['U'][0][1] == self._state['U'][1][0] == self._state['U'][2][1] == self._state['U'][1][2] == 'w':
			return 0

		if self._state['F'][0][1] != FACE2COR['F'] or \
		   self._state['L'][0][1] != FACE2COR['L'] or \
		   self._state['B'][0][1] != FACE2COR['B'] or \
		   self._state['R'][0][1] != FACE2COR['R']:
			return 0

		# finish white corners
		if self._state['U'] != INITIAL['U']:
			return 1

		if self._state['F'][0] != INITIAL['F'][0] or \
		   self._state['L'][0] != INITIAL['L'][0] or \
		   self._state['B'][0] != INITIAL['B'][0] or \
		   self._state['R'][0] != INITIAL['R'][0]:
			return 1

		# finish middle layer
		if self._state['F'][:2] != INITIAL['F'][:2] or \
		   self._state['L'][:2] != INITIAL['L'][:2] or \
		   self._state['B'][:2] != INITIAL['B'][:2] or \
		   self._state['R'][:2] != INITIAL['R'][:2]:
			return 2

		# finish yellow cross
		if not self._state['D'][1][0] == self._state['D'][0][1] == self._state['D'][2][1] == self._state['D'][1][2] == 'y':
			return 3

		# finish yellow edges
		if self._state['F'][2][1] != FACE2COR['F'] or \
		   self._state['L'][2][1] != FACE2COR['L'] or \
		   self._state['B'][2][1] != FACE2COR['B'] or \
		   self._state['R'][2][1] != FACE2COR['R']:
			return 4

		# finish position yellow corners
		if not self._state['F'][2][0] in ['r', 'g', 'y'] or not self._state['F'][2][2] in ['r', 'b', 'y'] or \
		   not self._state['L'][2][0] in ['g', 'o', 'y'] or not self._state['L'][2][2] in ['g', 'r', 'y'] or \
		   not self._state['B'][2][0] in ['o', 'b', 'y'] or not self._state['B'][2][2] in ['o', 'g', 'y'] or \
		   not self._state['R'][2][0] in ['b', 'r', 'y'] or not self._state['R'][2][2] in ['b', 'o', 'y'] or \
		   not self._state['D'][0][0] in ['y', 'g', 'r'] or not self._state['D'][0][2] in ['y', 'r', 'b'] or not self._state['D'][2][0] in ['y', 'g', 'o'] or not self._state['D'][2][2] in ['y', 'o', 'b']:
			return 5

		# finish orient yellow corners
		if not self._state == INITIAL:
			return 6

		# done
		return 7

	# solve white edges
	# ============================================================================================================================================= #
	def find_improper_white_edge(self):

		for face in ['D', 'F', 'L', 'B', 'R']:
			for i in range(3):
				for j in range(3):
					if self._state[face][i][j] == 'w' and (i == 1 or j == 1) and not i == j == 1:
						return face, i, j

		for i in range(3):
			for j in range(3):
				if not i == j == 1 and self._state['U'][i][j] == 'w' and (i == 1 or j == 1):
					if ((i, j) == (2, 1) and self._state['F'][0][1] != 'r') or \
					   ((i, j) == (1, 0) and self._state['L'][0][1] != 'g') or \
					   ((i, j) == (0, 1) and self._state['B'][0][1] != 'o') or \
					   ((i, j) == (1, 2) and self._state['R'][0][1] != 'b'):
						
						return 'U', i, j

		return None, None, None

	
	def solve_single_white_edge(self, face, i, j):

		# adjust the white edge to downside
		if face == 'U':

			if (i, j) == (2, 1):
				self.sequence_algorithm(['F+', 'F+'])
			elif (i, j) == (1, 0):
				self.sequence_algorithm(['L+', 'L+'])
			elif (i, j) == (0, 1):
				self.sequence_algorithm(['B+', 'B+'])
			else:
				# (i, j) = (1, 2)
				self.sequence_algorithm(['R+', 'R+'])

		# adjust the white edge to downside
		elif face != 'D':
			# F, L, B, R
			if j == 1:
				if i == 0:
					self.rotate(face + '+')
				else:
					# i = 2
					self.rotate(face + '-')
					
			if face == 'F':
				if j == 0:
					self.sequence_algorithm(['L+', 'D+', 'L-'])
				else:
					# j = 2 or j = 1
					self.sequence_algorithm(['R-', 'D+', 'R+'])
			elif face == 'L':
				if j == 0:
					self.sequence_algorithm(['B+', 'D+', 'B-'])
				else:
					# j = 2 or j = 1
					self.sequence_algorithm(['F-', 'D+', 'F+'])
			elif face == 'B':
				if j == 0:
					self.sequence_algorithm(['R+', 'D+', 'R-'])
				else:
					# j = 2 or j = 1
					self.sequence_algorithm(['L-', 'D+', 'L+'])
			elif face == 'R':
				if j == 0:
					self.sequence_algorithm(['F+', 'D+', 'F-'])
				else:
					# j = 2 or j = 1
					self.sequence_algorithm(['B-', 'D+', 'B+'])

			if j == 1:
				if i == 0:
					self.rotate(face + '-')
				else:
					# i = 2
					self.rotate(face + '+')

		face, i, j = self.find_improper_white_edge()

		if face != 'D':
			print('error')
			self.print_cube()

		pos_map = {
			(1, 0): 'L', 
			(0, 1): 'F', 
			(1, 2): 'R', 
			(2, 1): 'B'
		}

		while self._state[pos_map[(i, j)]][2][1] != FACE2COR[pos_map[(i, j)]]:
			self.rotate('D+')
			(i, j) = CLOCKWISE['+'][(i, j)]
			# will return downside improper white edge first
			# print(face, i, j)

		action = pos_map[(i, j)] + '+'

		self.sequence_algorithm([action, action])


	def solve_white_edges(self):

		face, i, j = self.find_improper_white_edge()

		while face != None:
			# improper white edge must exist
			self.solve_single_white_edge(face, i, j)
			face, i, j = self.find_improper_white_edge()


	# solve white corners
	# ============================================================================================================================================= #
	def find_improper_white_corner(self):

		for face in ['F', 'L', 'B', 'R']:
			for j in [0, 2]:
				if self._state[face][2][j] == 'w':
					return face, 2, j

		for face in ['F', 'L', 'B', 'R']:
			for j in [0, 2]:
				if self._state[face][0][j] == 'w':
					return face, 0, j

		for i in [0, 2]:
			for j in [0, 2]:
				if self._state['U'][i][j] == 'w':
					if ((i, j) == (2, 0) and (self._state['F'][0][0] != 'r' or self._state['L'][0][2] != 'g')) or \
					   ((i, j) == (0, 0) and (self._state['L'][0][0] != 'g' or self._state['B'][0][2] != 'o')) or \
					   ((i, j) == (0, 2) and (self._state['B'][0][0] != 'o' or self._state['R'][0][2] != 'b')) or \
					   ((i, j) == (2, 2) and (self._state['R'][0][0] != 'b' or self._state['F'][0][2] != 'r')):

						return 'U', i, j

		for i in [0, 2]:
			for j in [0, 2]:
				if self._state['D'][i][j] == 'w':
					return 'D', i, j

		return None, None, None


	def find_improper_white_corner_u(self):

		for i in [0, 2]:
			for j in [0, 2]:
				if self._state['U'][i][j] != 'w':
					return (i, j)

				if ((i, j) == (2, 0) and (self._state['F'][0][0] != 'r' or self._state['L'][0][2] != 'g')) or \
				   ((i, j) == (0, 0) and (self._state['L'][0][0] != 'g' or self._state['B'][0][2] != 'o')) or \
				   ((i, j) == (0, 2) and (self._state['B'][0][0] != 'o' or self._state['R'][0][2] != 'b')) or \
				   ((i, j) == (2, 2) and (self._state['R'][0][0] != 'b' or self._state['F'][0][2] != 'r')):

					return (i, j)

		return None


	def solve_single_white_corner(self, face, i, j):

		# print(face, i, j)

		if face in ['F', 'L', 'B', 'R'] and i == 0:
			if face == 'F':
				if j == 0:
					self.sequence_algorithm(['L+', 'D-', 'L-'])
				else:
					# j = 2
					self.sequence_algorithm(['R-', 'D+', 'R+'])
			elif face == 'L':
				if j == 0:
					self.sequence_algorithm(['B+', 'D-', 'B-'])
				else:
					# j = 2
					self.sequence_algorithm(['F-', 'D+', 'F+'])
			elif face == 'B':
				if j == 0:
					self.sequence_algorithm(['R+', 'D-', 'R-'])
				else:
					# j = 2
					self.sequence_algorithm(['L-', 'D+', 'L+'])
			else:
				# face = 'R'
				if j == 0:
					self.sequence_algorithm(['F+', 'D-', 'F-'])
				else:
					# j = 2
					self.sequence_algorithm(['B-', 'D+', 'B+'])


		elif face == 'U':
			if (i, j) == (0, 0):
				self.sequence_algorithm(['L-', 'D-', 'L+'])
			elif (i, j) == (2, 0):
				self.sequence_algorithm(['L+', 'D+', 'L-'])
			elif (i, j) == (0, 2):
				self.sequence_algorithm(['R+', 'D+', 'R-'])
			else:
				# (i, j) = (2, 2)
				self.sequence_algorithm(['R-', 'D-', 'R+'])

		elif face == 'D':
			flexible_u = self.find_improper_white_corner_u()
			pos_map = {
				(0, 0): (2, 0), 
				(2, 0): (0, 0), 
				(0, 2): (2, 2), 
				(2, 2): (0, 2)
			}
			flexible_d = pos_map[flexible_u]
			while (i, j) != flexible_d:
				self.rotate('D+')
				(i, j) = CLOCKWISE['+'][(i, j)]
			if flexible_u == (0, 0):
				self.sequence_algorithm(['L-', 'D+', 'L+'])
			elif flexible_u == (2, 0):
				self.sequence_algorithm(['F-', 'D+', 'F+'])
			elif flexible_u == (2, 2):
				self.sequence_algorithm(['R-', 'D+', 'R+'])
			elif flexible_u == (0, 2):
				self.sequence_algorithm(['B-', 'D+', 'B+'])

		face, i, j = self.find_improper_white_corner()

		# i = 2, face in [F, L, B, R]

		if i != 2 or not face in ['F', 'L', 'B', 'R']:
			print('error')
			print(i, face)
			self.print_cube()

		act_map = {
			0: ['+', '-', {
				'F': 'L', # + '+'
				'L': 'B',
				'B': 'R',
				'R': 'F'
			}],
			2: ['-', '+', {
				'F': 'R', # + '-'
				'R': 'B',
				'B': 'L',
				'L': 'F'
			}]
		}


		if (face == 'F' and j == 0) or (face == 'L' and j == 2):
			(i_d, j_d) = (0, 0)
		elif (face == 'L' and j == 0) or (face == 'B' and j == 2):
			(i_d, j_d) = (2, 0)
		elif (face == 'B' and j == 0) or (face == 'R' and j == 2):
			(i_d, j_d) = (2, 2)
		else:
			# (face == 'R' and j == 0) or (face == 'F' and j == 2)
			(i_d, j_d) = (0, 2)

		dir_map = {
			'+': {
				'F': 'R', 
				'R': 'B',
				'B': 'L',
				'L': 'F'
			},
			'-': {
				'F': 'L',
				'L': 'B',
				'B': 'R',
				'R': 'F'
			}
		}

		while self._state['D'][i_d][j_d] != FACE2COR[face]:
			self.rotate('D+')
			face = dir_map['+'][face]
			(i_d, j_d) = CLOCKWISE['+'][(i_d, j_d)]

		self.sequence_algorithm(['D' + act_map[j][0], act_map[j][2][face] + act_map[j][0], 'D' + act_map[j][1], act_map[j][2][face] + act_map[j][1]])


	def solve_white_corners(self):

		face, i, j = self.find_improper_white_corner()
		while face != None:
			# improper white corner must exist
			self.solve_single_white_corner(face, i, j)
			face, i, j = self.find_improper_white_corner()


	# solve middle layer
	# ============================================================================================================================================= #

	# find improper and solvable middle layer
	def find_improper_middle_layer(self):

		pos_map = {
			'F': (0, 1),
			'L': (1, 0),
			'B': (2, 1),
			'R': (1, 2)
		}

		for face in ['F', 'L', 'B', 'R']:
			if self._state[face][2][1] != 'y' and self._state['D'][pos_map[face][0]][pos_map[face][1]] != 'y':
				return face, 'D', None

		fac_map = {
			0: {
				'F': 'L',
				'L': 'B',
				'B': 'R',
				'R': 'F'
			},
			2: {
				'F': 'R',
				'R': 'B',
				'B': 'L',
				'L': 'F'
			}
		}

		for face in ['F', 'L', 'B', 'R']:
			for j in [0, 2]:
				if self._state[face][1][j] != FACE2COR[face] or self._state[fac_map[j][face]][1][2 - j] != FACE2COR[fac_map[j][face]]:
					return face, fac_map[j][face], j

		return None, None, None


	def solve_single_middle_layer(self, face_1, face_2, j):

		# if the improper middle layer is on the side
		if j != None:
			if j == 0:
				self.sequence_algorithm(['D+', face_2 + '+', 'D-', face_2 + '-', 'D-', face_1 + '-', 'D+', face_1 + '+'])
			else:
				# j = 2
				self.sequence_algorithm(['D-', face_2 + '-', 'D+', face_2 + '+', 'D+', face_1 + '+', 'D-', face_1 + '-'])

			face_1, face_2, j = self.find_improper_middle_layer()
			print('new cube: ')
			self.print_cube()
			print('new position: ', face_1, face_2, j)

		if j != None:
			print('error')
			self.print_cube()


		pos_map = {
			'F': (0, 1),
			'L': (1, 0),
			'B': (2, 1),
			'R': (1, 2)
		}

		fac_map = {
			'+': {
				'F': 'R',
				'R': 'B',
				'B': 'L',
				'L': 'F'
			},
			'-': {
				'F': 'L',
				'L': 'B',
				'B': 'R',
				'R': 'F'
			}
		}

		while self._state[face_1][2][1] != FACE2COR[face_1]:
			self.rotate('D+')
			face_1 = fac_map['+'][face_1]

		(i_d, j_d) = pos_map[face_1]
		face_2 = COR2FACE[self._state['D'][i_d][j_d]]
		if self._state['D'][i_d][j_d] == FACE2COR[fac_map['+'][face_1]]:
			# downside edge matches right edge
			self.sequence_algorithm(['D-', face_2 + '-', 'D+', face_2 + '+', 'D+', face_1 + '+', 'D-', face_1 + '-'])
		else:
			# downside edge matches left edge
			self.sequence_algorithm(['D+', face_2 + '+', 'D-', face_2 + '-', 'D-', face_1 + '-', 'D+', face_1 + '+'])


	def solve_middle_layer(self):

		face_1, face_2, j = self.find_improper_middle_layer()
		while face_1 != None:
			# improper middle layer must exist
			# print(face_1, face_2, j)

			self.solve_single_middle_layer(face_1, face_2, j)
			face_1, face_2, j = self.find_improper_middle_layer()

			# self.print_cube()
			# raw_input('press ENTER')


	# solve yellow cross
	# ============================================================================================================================================= #

	def get_cur_yellow_cross_stage(self):

		# 0: only yellow center, 1: angle, 2: line, 3: solved
		if self._state['D'][1][0] == self._state['D'][0][1] == self._state['D'][1][2] == self._state['D'][2][1] == 'y':
			return 3, None

		elif self._state['D'][1][0] == self._state['D'][1][2] == 'y':
			return 2, 'F'
		elif self._state['D'][0][1] == self._state['D'][2][1] == 'y':
			return 2, 'L'

		elif self._state['D'][1][0] == self._state['D'][0][1] == 'y':
			return 1, 'B'
		elif self._state['D'][0][1] == self._state['D'][1][2] == 'y':
			return 1, 'L'
		elif self._state['D'][1][2] == self._state['D'][2][1] == 'y':
			return 1, 'F'
		elif self._state['D'][2][1] == self._state['D'][1][0] == 'y':
			return 1, 'R'
		
		else:
			return 0, 'F'


	def solve_yellow_cross(self):

		fac_map = {
			'F': 'L',
			'L': 'B',
			'B': 'R',
			'R': 'F'
		}

		# check whether yellow cross has been solved
		local_stage, face = self.get_cur_yellow_cross_stage()
		while face != None:
			# solve current state
			if local_stage == 0:
				# not solved but to the next stage
				self.sequence_algorithm([face + '+', fac_map[face] + '+', 'D+', fac_map[face] + '-', 'D-', face + '-'])
			elif local_stage == 1:
				# solved
				self.sequence_algorithm([face + '+', fac_map[face] + '+', 'D+', fac_map[face] + '-', 'D-', face + '-'])
				self.sequence_algorithm([face + '+', fac_map[face] + '+', 'D+', fac_map[face] + '-', 'D-', face + '-'])
			else:
				# local_stage = 2
				# solved
				self.sequence_algorithm([face + '+', fac_map[face] + '+', 'D+', fac_map[face] + '-', 'D-', face + '-'])

			local_stage, face = self.get_cur_yellow_cross_stage()



	# solve yellow edges
	# ============================================================================================================================================= #

	def find_adjacent_solved_yellow_edges(self):

		fac_map = {
			'F': 'L',
			'L': 'B',
			'B': 'R',
			'R': 'F'
		}

		for i in range(4):
			for face in ['F', 'L', 'B', 'R']:
				if self._state[face][2][1] == FACE2COR[face] and self._state[fac_map[face]][2][1] == FACE2COR[fac_map[face]]:
					# face, fac_map[face] are the adjacent faces
					return face

		while self._state['F'][2][1] != FACE2COR['F']:
			self.rotate('D+')

		return None


	def is_yellow_edges_solved(self):

		for i in range(4):
			for face in ['F', 'L', 'B', 'R']:
				if self._state[face][2][1] != FACE2COR[face]:
					return False

		return True


	def solve_yellow_edges(self):

		face_1 = self.find_adjacent_solved_yellow_edges()
		while face_1 == None:
			self.sequence_algorithm(['L+', 'D+', 'L-', 'D+', 'L+', 'D+', 'D+', 'L-'])
			face_1 = self.find_adjacent_solved_yellow_edges()

			# self.print_cube()
			# print(face_1)
			# raw_input('press ENTER')

		if not self.is_yellow_edges_solved():
			self.sequence_algorithm([face_1 + '+', 'D+', face_1 + '-', 'D+', face_1 + '+', 'D+', 'D+', face_1 + '-', 'D+'])

		
	# solve position yellow corners
	# ============================================================================================================================================= #

	def find_yellow_corner_with_incorrect_position(self):

		fac_map = {
			(0, 0): [('D', 0, 0), ('F', 2, 0), ('L', 2, 2)],
			(0, 2): [('D', 0, 2), ('F', 2, 2), ('R', 2, 0)],
			(2, 0): [('D', 2, 0), ('L', 2, 0), ('B', 2, 2)],
			(2, 2): [('D', 2, 2), ('R', 2, 2), ('B', 2, 0)]
		}

		for pos in fac_map:
			cor_set = [FACE2COR[face_pos[0]] for face_pos in fac_map[pos]]
			for face_pos in fac_map[pos]:
				if not self._state[face_pos[0]][face_pos[1]][face_pos[2]] in cor_set:
					return pos

		return None


	def find_yellow_corner_with_correct_position(self):

		fac_map = {
			(0, 0): [('D', 0, 0), ('F', 2, 0), ('L', 2, 2)],
			(0, 2): [('D', 0, 2), ('F', 2, 2), ('R', 2, 0)],
			(2, 0): [('D', 2, 0), ('L', 2, 0), ('B', 2, 2)],
			(2, 2): [('D', 2, 2), ('R', 2, 2), ('B', 2, 0)]
		}

		for pos in fac_map:
			correct = True
			cor_set = [FACE2COR[face_pos[0]] for face_pos in fac_map[pos]]
			for face_pos in fac_map[pos]:
				if not self._state[face_pos[0]][face_pos[1]][face_pos[2]] in cor_set:
					correct = False
			if correct:
				return pos

		return None

	def solve_position_yellow_corners(self):

		correct_pos = self.find_yellow_corner_with_correct_position()
		while not correct_pos:
			self.sequence_algorithm(['D+', 'L+', 'D-', 'R-', 'D+', 'L-', 'D-', 'R+'])
			correct_pos = self.find_yellow_corner_with_correct_position()

		fac_map = {
			(0, 0): ['L', 'R'],
			(0, 2): ['F', 'B'],
			(2, 2): ['R', 'L'],
			(2, 0): ['B', 'F']
		}

		actions = fac_map[correct_pos]

		incorrect_pos = self.find_yellow_corner_with_incorrect_position()
		while incorrect_pos:
			self.sequence_algorithm(['D+', actions[0] + '+', 'D-', actions[1] + '-', 'D+', actions[0] + '-', 'D-', actions[1] + '+'])
			incorrect_pos = self.find_yellow_corner_with_incorrect_position()


	# solve orient yellow corners
	# ============================================================================================================================================= #

	def find_yellow_corner_with_incorrect_orientation(self, initial = False):

		fac_map = {
			(0, 0): [('D', 0, 0), ('F', 2, 0), ('L', 2, 2)],
			(0, 2): [('D', 0, 2), ('F', 2, 2), ('R', 2, 0)],
			(2, 0): [('D', 2, 0), ('L', 2, 0), ('B', 2, 2)],
			(2, 2): [('D', 2, 2), ('R', 2, 2), ('B', 2, 0)]
		}

		for pos in fac_map:
			if initial:
				for face_pos in fac_map[pos]:
					# print(pos, face_pos)

					if self._state[face_pos[0]][face_pos[1]][face_pos[2]] != FACE2COR[face_pos[0]]:
						return pos
			else:
				if self._state['D'][pos[0]][pos[1]] != 'y':
					return pos


		return None


	def solve_orient_yellow_corners(self):

		fac_map = {
			(0, 0): 'L',
			(0, 2): 'F',
			(2, 2): 'R',
			(2, 0): 'B'
		}

		initial = True
		pos = self.find_yellow_corner_with_incorrect_orientation(initial)
		
		init_pos = pos
		while pos != None:
			if initial:
				initial = False
			else:
				# turn the critial pos to the init_pos
				while pos != init_pos:
					# print(pos, init_pos)
					self.rotate('D+')
					pos = CLOCKWISE['+'][pos]
			while self._state['D'][init_pos[0]][init_pos[1]] != 'y':
				self.sequence_algorithm([fac_map[init_pos] + '-', 'U-', fac_map[init_pos] + '+', 'U+'])

			pos = self.find_yellow_corner_with_incorrect_orientation(initial)

			# print(pos, pos != None)
			# self.print_cube()
			# raw_input('press ENTER')

		while self._state['F'][0][1] != FACE2COR['F']:
			self.rotate('U+')
		while self._state['F'][2][1] != FACE2COR['F']:
			self.rotate('D+')


	# solve all
	# ============================================================================================================================================= #
	'''

		stage:
			0. start: mixed
			1. white edges: white cross have been solved
			2. white corners: white face
			3. middle layer: middle layer solved
			4. yellow cross: yellow cross formed
			5. yellow edges: yellow edges formed
			6. position yellow corners: corner positions are correct
			7. orient yellow corners: corner orientations are correct (done)

	'''

	def solve(self):

		self._actions = []

		actions = {
			0: self.solve_white_edges,
			1: self.solve_white_corners,
			2: self.solve_middle_layer,
			3: self.solve_yellow_cross,
			4: self.solve_yellow_edges,
			5: self.solve_position_yellow_corners,
			6: self.solve_orient_yellow_corners
		}

		stage = self.get_cur_stage()
		while stage != 7:
			actions[stage]()
			stage = self.get_cur_stage()
			# self.print_cube()
			print('stage: ', stage)

			# self.print_cube()
			# input('press ENTER')

		print('>>>>>>> Solved in ' + str(len(self._actions)) + ' moves <<<<<<<')
		# self.print_cube()