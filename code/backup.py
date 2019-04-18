from cube import Cube
from cube import *

import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.collections import PatchCollection, PolyCollection

import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors
import pylab as pl
import scipy as sp

'''
	colors:
		w: white
		#ffcf00: orange
		#00008f: blue
		#009f0f: green
		#cf0000: red
		yellow: yellow
'''


class DisplayCube(Cube):

	_piece_colors = {
		'r': '#cf0000',
		'g': '#009f0f',
		'o': 'orange',
		'b': '#00008f',
		'w': 'w',
		'y': 'yellow',
		'n': 'gray'
	}
	_face_anchors = {
		'F': [3, 1.5, 1.5],
		'L': [1.5, 0, 1.5],
		'B': [0, 1.5, 1.5],
		'R': [1.5, 3, 1.5],
		'U': [1.5, 1.5, 3],
		'D': [1.5, 1.5, 0]
	}

	_n = 10
	_time = 0.0001

	_view_vertical = 15
	_view_horizontal = 15

	def __init__(self, state=INITIAL):

		Cube.__init__(self, state)

		self._pieces = {}
		self._inner_pieces = {}
		x, y, z = np.indices((3, 3, 3))

		# add inner pieces
		for face in ['U', 'D', 'F', 'B', 'L', 'R']:
			for i in range(3):
				for j in range(3):
					if face == 'U':
						self._inner_pieces['i' + face + str(i) + str(j)] = [
							[i, j, 2.1],
							[i, j + 1, 2.1],
							[i + 1, j + 1, 2.1],
							[i + 1, j, 2.1]
						]
						self._inner_pieces['m' + face + str(i) + str(j)] = [
							[i, j, 1.9],
							[i, j + 1, 1.9],
							[i + 1, j + 1, 1.9],
							[i + 1, j, 1.9]
						]
					elif face == 'D':
						self._inner_pieces['i' + face + str(i) + str(j)] = [
							[3 - i, j, 0.9],
							[3 - i, j + 1, 0.9],
							[2 - i, j + 1, 0.9],
							[2 - i, j, 0.9]
						]
						self._inner_pieces['m' + face + str(i) + str(j)] = [
							[3 - i, j, 1.1],
							[3 - i, j + 1, 1.1],
							[2 - i, j + 1, 1.1],
							[2 - i, j, 1.1]
						]
					elif face == 'F':
						self._inner_pieces['i' + face + str(i) + str(j)] = [
							[2.1, j, 3 - i],
							[2.1, j + 1, 3 - i],
							[2.1, j + 1, 2 - i],
							[2.1, j, 2 - i]
						]
						self._inner_pieces['m' + face + str(i) + str(j)] = [
							[1.9, j, 3 - i],
							[1.9, j + 1, 3 - i],
							[1.9, j + 1, 2 - i],
							[1.9, j, 2 - i]
						]
					elif face == 'L':
						self._inner_pieces['i' + face + str(i) + str(j)] = [
							[j, 0.9, 3 - i],
							[j + 1, 0.9, 3 - i],
							[j + 1, 0.9, 2 - i],
							[j, 0.9, 2 - i]
						]
						self._inner_pieces['m' + face + str(i) + str(j)] = [
							[j, 1.1, 3 - i],
							[j + 1, 1.1, 3 - i],
							[j + 1, 1.1, 2 - i],
							[j, 1.1, 2 - i]
						]
					elif face == 'B':
						self._inner_pieces['i' + face + str(i) + str(j)] = [
							[0.9, 3 - j, 3 - i],
							[0.9, 2 - j, 3 - i],
							[0.9, 2 - j, 2 - i],
							[0.9, 3 - j, 2 - i]
						]
						self._inner_pieces['m' + face + str(i) + str(j)] = [
							[1.1, 3 - j, 3 - i],
							[1.1, 2 - j, 3 - i],
							[1.1, 2 - j, 2 - i],
							[1.1, 3 - j, 2 - i]
						]
					else:
						# face = 'R'
						self._inner_pieces['i' + face + str(i) + str(j)] = [
							[3 - j, 2.1, 3 - i],
							[2 - j, 2.1, 3 - i],
							[2 - j, 2.1, 2 - i],
							[3 - j, 2.1, 2 - i]
						]
						self._inner_pieces['m' + face + str(i) + str(j)] = [
							[3 - j, 1.9, 3 - i],
							[2 - j, 1.9, 3 - i],
							[2 - j, 1.9, 2 - i],
							[3 - j, 1.9, 2 - i]
						]


		for face in ['U', 'D', 'F', 'B', 'L', 'R']:
			for i in range(3):
				for j in range(3):
					if face == 'U':
						self._pieces[face + str(i) + str(j)] = [
							[i, j, 3],
							[i, j + 1, 3],
							[i + 1, j + 1, 3],
							[i + 1, j, 3]
						]
					elif face == 'D':
						self._pieces[face + str(i) + str(j)] = [
							[3 - i, j, 0],
							[3 - i, j + 1, 0],
							[2 - i, j + 1, 0],
							[2 - i, j, 0]
						]
					elif face == 'F':
						self._pieces[face + str(i) + str(j)] = [
							[3, j, 3 - i],
							[3, j + 1, 3 - i],
							[3, j + 1, 2 - i],
							[3, j, 2 - i]
						]
					elif face == 'L':
						self._pieces[face + str(i) + str(j)] = [
							[j, 0, 3 - i],
							[j + 1, 0, 3 - i],
							[j + 1, 0, 2 - i],
							[j, 0, 2 - i]
						]
					elif face == 'B':
						self._pieces[face + str(i) + str(j)] = [
							[0, 3 - j, 3 - i],
							[0, 2 - j, 3 - i],
							[0, 2 - j, 2 - i],
							[0, 3 - j, 2 - i]
						]
					else:
						# face = 'R'
						self._pieces[face + str(i) + str(j)] = [
							[3 - j, 3, 3 - i],
							[2 - j, 3, 3 - i],
							[2 - j, 3, 2 - i],
							[3 - j, 3, 2 - i]
						]


		self._display_state = {}
		for face in ['U', 'D', 'F', 'B', 'L', 'R']:
			self._display_state[face] = [[state[face][i][j] for j in range(3)] for i in range(3)]


	def update_pieces(self):

		self._pieces = {}
		self._inner_pieces = {}
		x, y, z = np.indices((3, 3, 3))

		# add inner pieces
		for face in ['U', 'D', 'F', 'B', 'L', 'R']:
			for i in range(3):
				for j in range(3):
					if face == 'U':
						self._inner_pieces['i' + face + str(i) + str(j)] = [
							[i, j, 2.5],
							[i, j + 1, 2.5],
							[i + 1, j + 1, 2.5],
							[i + 1, j, 2.5]
						]
						self._inner_pieces['m' + face + str(i) + str(j)] = [
							[i, j, 1.5],
							[i, j + 1, 1.5],
							[i + 1, j + 1, 1.5],
							[i + 1, j, 1.5]
						]
					elif face == 'D':
						self._inner_pieces['i' + face + str(i) + str(j)] = [
							[3 - i, j, 0.5],
							[3 - i, j + 1, 0.5],
							[2 - i, j + 1, 0.5],
							[2 - i, j, 0.5]
						]
						self._inner_pieces['m' + face + str(i) + str(j)] = [
							[3 - i, j, 1.5],
							[3 - i, j + 1, 1.5],
							[2 - i, j + 1, 1.5],
							[2 - i, j, 1.5]
						]
					elif face == 'F':
						self._inner_pieces['i' + face + str(i) + str(j)] = [
							[2.5, j, 3 - i],
							[2.5, j + 1, 3 - i],
							[2.5, j + 1, 2 - i],
							[2.5, j, 2 - i]
						]
						self._inner_pieces['m' + face + str(i) + str(j)] = [
							[1.5, j, 3 - i],
							[1.5, j + 1, 3 - i],
							[1.5, j + 1, 2 - i],
							[1.5, j, 2 - i]
						]
					elif face == 'L':
						self._inner_pieces['i' + face + str(i) + str(j)] = [
							[j, 0.5, 3 - i],
							[j + 1, 0.5, 3 - i],
							[j + 1, 0.5, 2 - i],
							[j, 0.5, 2 - i]
						]
						self._inner_pieces['m' + face + str(i) + str(j)] = [
							[j, 1.5, 3 - i],
							[j + 1, 1.5, 3 - i],
							[j + 1, 1.5, 2 - i],
							[j, 1.5, 2 - i]
						]
					elif face == 'B':
						self._inner_pieces['i' + face + str(i) + str(j)] = [
							[0.5, 3 - j, 3 - i],
							[0.5, 2 - j, 3 - i],
							[0.5, 2 - j, 2 - i],
							[0.5, 3 - j, 2 - i]
						]
						self._inner_pieces['m' + face + str(i) + str(j)] = [
							[1.5, 3 - j, 3 - i],
							[1.5, 2 - j, 3 - i],
							[1.5, 2 - j, 2 - i],
							[1.5, 3 - j, 2 - i]
						]
					else:
						# face = 'R'
						self._inner_pieces['i' + face + str(i) + str(j)] = [
							[3 - j, 2.5, 3 - i],
							[2 - j, 2.5, 3 - i],
							[2 - j, 2.5, 2 - i],
							[3 - j, 2.5, 2 - i]
						]
						self._inner_pieces['m' + face + str(i) + str(j)] = [
							[3 - j, 1.5, 3 - i],
							[2 - j, 1.5, 3 - i],
							[2 - j, 1.5, 2 - i],
							[3 - j, 1.5, 2 - i]
						]

		for face in ['U', 'D', 'F', 'B', 'L', 'R']:
			for i in range(3):
				for j in range(3):
					if face == 'U':
						self._pieces[face + str(i) + str(j)] = [
							[i, j, 3],
							[i, j + 1, 3],
							[i + 1, j + 1, 3],
							[i + 1, j, 3]
						]
					elif face == 'D':
						self._pieces[face + str(i) + str(j)] = [
							[3 - i, j, 0],
							[3 - i, j + 1, 0],
							[2 - i, j + 1, 0],
							[2 - i, j, 0]
						]
					elif face == 'F':
						self._pieces[face + str(i) + str(j)] = [
							[3, j, 3 - i],
							[3, j + 1, 3 - i],
							[3, j + 1, 2 - i],
							[3, j, 2 - i]
						]
					elif face == 'L':
						self._pieces[face + str(i) + str(j)] = [
							[j, 0, 3 - i],
							[j + 1, 0, 3 - i],
							[j + 1, 0, 2 - i],
							[j, 0, 2 - i]
						]
					elif face == 'B':
						self._pieces[face + str(i) + str(j)] = [
							[0, 3 - j, 3 - i],
							[0, 2 - j, 3 - i],
							[0, 2 - j, 2 - i],
							[0, 3 - j, 2 - i]
						]
					else:
						# face = 'R'
						self._pieces[face + str(i) + str(j)] = [
							[3 - j, 3, 3 - i],
							[2 - j, 3, 3 - i],
							[2 - j, 3, 2 - i],
							[3 - j, 3, 2 - i]
						]


	def display_pieces(self):

		ax = a3.Axes3D(pl.figure())
		ax.autoscale(enable=True, tight=None)

		ax.view_init(self._view_vertical, self._view_horizontal)

		for piece in self._inner_pieces:
			vtx = 0.2 * np.array(self._inner_pieces[piece])
			tri = a3.art3d.Poly3DCollection([vtx])
			tri.set_color(self._piece_colors['n'])
			tri.set_edgecolor('k')
			ax.add_collection3d(tri)

		for piece in self._pieces:
			vtx = 0.2 * np.array(self._pieces[piece])
			tri = a3.art3d.Poly3DCollection([vtx])
			tri.set_color(self._piece_colors[self._display_state[piece[0]][int(piece[1])][int(piece[2])]])
			tri.set_edgecolor('k')
			ax.add_collection3d(tri)

		pl.show()


	def print_cube(self):

		printer = pprint.PrettyPrinter(indent=4)
		print('State: ')
		printer.pprint(self._state)
		print('Display State: ')
		printer.pprint(self._display_state)
		print('Actions: ')
		print(self._actions)


	def clone_state(self, display=False):

		copy = {}

		if display:
			state = self._display_state
		else:
			state = self._state

		for face in ['U', 'D', 'F', 'B', 'L', 'R']:
			copy[face] = [[state[face][i][j] for j in range(3)] for i in range(3)]

		return copy


	def shuffle(self, n):

		for i in range(n):
			action = random.choice(['U', 'D', 'F', 'L', 'B', 'R']) + random.choice(['+', '-'])
			self.rotate(action)
			self.rotate(action, display=True)


	def rotate(self, action, display=False):

		if display:
			state = self._display_state
		else:
			state = self._state

		copy = self.clone_state(display)

		if not display:
			self._actions.append(action)

		# action: an action in ACTIONS
		if action == 'U+':
			state['F'][0] = [copy['R'][0][j] for j in range(3)]
			state['L'][0] = [copy['F'][0][j] for j in range(3)]
			state['B'][0] = [copy['L'][0][j] for j in range(3)]
			state['R'][0] = [copy['B'][0][j] for j in range(3)]


			for pos in CLOCKWISE['+']:
				state['U'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['U'][pos[0]][pos[1]]

		elif action == 'U-':
			state['F'][0] = [copy['L'][0][j] for j in range(3)]
			state['L'][0] = [copy['B'][0][j] for j in range(3)]
			state['B'][0] = [copy['R'][0][j] for j in range(3)]
			state['R'][0] = [copy['F'][0][j] for j in range(3)]

			for pos in CLOCKWISE['-']:
				state['U'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['U'][pos[0]][pos[1]]


		elif action == 'D+':
			state['F'][2] = [copy['L'][2][j] for j in range(3)]
			state['L'][2] = [copy['B'][2][j] for j in range(3)]
			state['B'][2] = [copy['R'][2][j] for j in range(3)]
			state['R'][2] = [copy['F'][2][j] for j in range(3)]

			for pos in CLOCKWISE['+']:
				state['D'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['D'][pos[0]][pos[1]]

		elif action == 'D-':
			state['F'][2] = [copy['R'][2][j] for j in range(3)]
			state['L'][2] = [copy['F'][2][j] for j in range(3)]
			state['B'][2] = [copy['L'][2][j] for j in range(3)]
			state['R'][2] = [copy['B'][2][j] for j in range(3)]

			for pos in CLOCKWISE['-']:
				state['D'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['D'][pos[0]][pos[1]]


		elif action == 'F+':
			state['U'][2] = [copy['L'][2 - i][2] for i in range(3)]

			state['L'][0][2] = copy['D'][0][0]
			state['L'][1][2] = copy['D'][0][1]
			state['L'][2][2] = copy['D'][0][2]

			state['D'][0] = [copy['R'][2 - i][0] for i in range(3)]

			state['R'][0][0] = copy['U'][2][0]
			state['R'][1][0] = copy['U'][2][1]
			state['R'][2][0] = copy['U'][2][2]

			for pos in CLOCKWISE['+']:
				state['F'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['F'][pos[0]][pos[1]]

		elif action == 'F-':
			state['U'][2] = [copy['R'][i][0] for i in range(3)]

			state['R'][0][0] = copy['D'][0][2]
			state['R'][1][0] = copy['D'][0][1]
			state['R'][2][0] = copy['D'][0][0]

			state['D'][0] = [copy['L'][i][2] for i in range(3)]

			state['L'][0][2] = copy['U'][2][2]
			state['L'][1][2] = copy['U'][2][1]
			state['L'][2][2] = copy['U'][2][0]

			for pos in CLOCKWISE['-']:
				state['F'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['F'][pos[0]][pos[1]]

		elif action == 'B+':
			state['U'][0] = [copy['R'][i][2] for i in range(3)]

			state['R'][0][2] = copy['D'][2][2]
			state['R'][1][2] = copy['D'][2][1]
			state['R'][2][2] = copy['D'][2][0]

			state['D'][2] = [copy['L'][i][0] for i in range(3)]

			state['L'][0][0] = copy['U'][0][2]
			state['L'][1][0] = copy['U'][0][1]
			state['L'][2][0] = copy['U'][0][0]

			for pos in CLOCKWISE['+']:
				state['B'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['B'][pos[0]][pos[1]]

		elif action == 'B-':
			state['U'][0] = [copy['L'][2 - i][0] for i in range(3)]

			state['L'][0][0] = copy['D'][2][0]
			state['L'][1][0] = copy['D'][2][1]
			state['L'][2][0] = copy['D'][2][2]

			state['D'][2] = [copy['R'][2 - i][2] for i in range(3)]

			state['R'][0][2] = copy['U'][0][0]
			state['R'][1][2] = copy['U'][0][1]
			state['R'][2][2] = copy['U'][0][2]

			for pos in CLOCKWISE['-']:
				state['B'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['B'][pos[0]][pos[1]]


		elif action == 'L+':
			for i in range(3):
				state['F'][i][0] = copy['U'][i][0]
				state['U'][i][0] = copy['B'][2 - i][2]
				state['B'][i][2] = copy['D'][2 - i][0]
				state['D'][i][0] = copy['F'][i][0]

			for pos in CLOCKWISE['+']:
				state['L'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['L'][pos[0]][pos[1]]

		elif action == 'L-':
			for i in range(3):
				state['F'][i][0] = copy['D'][i][0]
				state['D'][i][0] = copy['B'][2 - i][2]
				state['B'][i][2] = copy['U'][2 - i][0]
				state['U'][i][0] = copy['F'][i][0]

			for pos in CLOCKWISE['-']:
				state['L'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['L'][pos[0]][pos[1]]


		elif action == 'R+':
			for i in range(3):
				state['F'][i][2] = copy['D'][i][2]
				state['D'][i][2] = copy['B'][2 - i][0]
				state['B'][i][0] = copy['U'][2 - i][2]
				state['U'][i][2] = copy['F'][i][2]

			for pos in CLOCKWISE['+']:
				state['R'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['R'][pos[0]][pos[1]]

		elif action == 'R-':
			for i in range(3):
				state['F'][i][2] = copy['U'][i][2]
				state['U'][i][2] = copy['B'][2 - i][0]
				state['B'][i][0] = copy['D'][2 - i][2]
				state['D'][i][2] = copy['F'][i][2]

			for pos in CLOCKWISE['-']:
				state['R'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['R'][pos[0]][pos[1]]


	def sequence_algorithm(self, seq, display=False):

		for action in seq:
			self.rotate(action, display)


	def display_rotate(self, action):

		ax = a3.Axes3D(pl.figure())
		ax.autoscale(enable=True, tight=None)

		pic_map = {
			'F': ['U20', 'U21', 'U22', 'L02', 'L12', 'L22', 'D00', 'D01', 'D02', 'R00', 'R10', 'R20'],
			'L': ['U00', 'U10', 'U20', 'B02', 'B12', 'B22', 'D20', 'D10', 'D00', 'F20', 'F10', 'F00'],
			'B': ['U00', 'U01', 'U02', 'R02', 'R12', 'R22', 'D22', 'D21', 'D20', 'L00', 'L10', 'L20'],
			'R': ['U22', 'U12', 'U02', 'F02', 'F12', 'F22', 'D02', 'D12', 'D22', 'B00', 'B10', 'B20'],
			'U': ['F00', 'F01', 'F02', 'L00', 'L01', 'L02', 'B00', 'B01', 'B02', 'R00', 'R01', 'R02'],
			'D': ['F20', 'F21', 'F22', 'L20', 'L21', 'L22', 'B20', 'B21', 'B22', 'R20', 'R21', 'R22']
		}
		axs_map = {
			'F': [1, 2], 'B': [1, 2],
			'L': [0, 2], 'R': [0, 2],
			'U': [0, 1], 'D': [0, 1]
		}

		[x_ax, y_ax] = axs_map[action[0]]
		axis_anchor = self._face_anchors[action[0]]

		for face in pic_map:
			new_pieces = pic_map[face].copy()
			for piece in pic_map[face]:
				new_pieces.append('i' + piece)
				new_pieces.append('m' + piece)
			pic_map[face] = new_pieces

		for face in pic_map:
			for i in range(3):
				for j in range(3):
					pic_map[face].append(face + str(i) + str(j))
					pic_map[face].append('i' + face + str(i) + str(j))

		theta = np.pi / (2 * self._n)

		for i in range(self._n):
			ax.clear()
			ax.view_init(self._view_vertical, self._view_horizontal)
			for piece_id in pic_map[action[0]]:
				piece = self._inner_pieces[piece_id] if (piece_id[0] in ['i', 'm']) else self._pieces[piece_id]
				for vertex in piece:
					x_rel = vertex[x_ax] - axis_anchor[x_ax]
					y_rel = vertex[y_ax] - axis_anchor[y_ax]

					if (action[1] == '+' and (action[0] in ['F', 'L', 'U'])) or (action[1] == '-' and (action[0] in ['D', 'B', 'R'])):
						x_rel_new = x_rel * np.cos(theta) + y_rel * np.sin(theta)
						y_rel_new = y_rel * np.cos(theta) - x_rel * np.sin(theta)
					else:
						x_rel_new = x_rel * np.cos(theta) - y_rel * np.sin(theta)
						y_rel_new = y_rel * np.cos(theta) + x_rel * np.sin(theta)

					vertex[x_ax] = x_rel_new + axis_anchor[x_ax]
					vertex[y_ax] = y_rel_new + axis_anchor[y_ax]

			for piece in self._inner_pieces:
				vtx = 0.2 * np.array(self._inner_pieces[piece])
				tri = a3.art3d.Poly3DCollection([vtx])
				tri.set_color(self._piece_colors['n'])
				tri.set_edgecolor('k')
				ax.add_collection3d(tri)

			for piece in self._pieces:
				vtx = 0.2 * np.array(self._pieces[piece])
				tri = a3.art3d.Poly3DCollection([vtx])
				tri.set_color(self._piece_colors[self._display_state[piece[0]][int(piece[1])][int(piece[2])]])
				tri.set_edgecolor('k')
				ax.add_collection3d(tri)

			pl.draw()
			pl.pause(self._time)

		self.rotate(action, display=True)

		pl.show()

		self.update_pieces()

	def display_sequence_algorithm(self, seq):

		ax = a3.Axes3D(pl.figure())
		ax.autoscale(enable=True, tight=None)

		pic_map = {
			'F': ['U20', 'U21', 'U22', 'L02', 'L12', 'L22', 'D00', 'D01', 'D02', 'R00', 'R10', 'R20'],
			'L': ['U00', 'U10', 'U20', 'B02', 'B12', 'B22', 'D20', 'D10', 'D00', 'F20', 'F10', 'F00'],
			'B': ['U00', 'U01', 'U02', 'R02', 'R12', 'R22', 'D22', 'D21', 'D20', 'L00', 'L10', 'L20'],
			'R': ['U22', 'U12', 'U02', 'F02', 'F12', 'F22', 'D02', 'D12', 'D22', 'B00', 'B10', 'B20'],
			'U': ['F00', 'F01', 'F02', 'L00', 'L01', 'L02', 'B00', 'B01', 'B02', 'R00', 'R01', 'R02'],
			'D': ['F20', 'F21', 'F22', 'L20', 'L21', 'L22', 'B20', 'B21', 'B22', 'R20', 'R21', 'R22']
		}
		axs_map = {
			'F': [1, 2], 'B': [1, 2],
			'L': [0, 2], 'R': [0, 2],
			'U': [0, 1], 'D': [0, 1]
		}

		for face in pic_map:
			new_pieces = pic_map[face].copy()
			for piece in pic_map[face]:
				new_pieces.append('i' + piece)
				new_pieces.append('m' + piece)
			pic_map[face] = new_pieces

		for face in pic_map:
			for i in range(3):
				for j in range(3):
					pic_map[face].append(face + str(i) + str(j))
					pic_map[face].append('i' + face + str(i) + str(j))
		
		theta = np.pi / (2 * self._n)

		for action in seq:
			[x_ax, y_ax] = axs_map[action[0]]
			axis_anchor = self._face_anchors[action[0]]
			for i in range(self._n):
				ax.clear()
				ax.view_init(self._view_vertical, self._view_horizontal)
				for piece_id in pic_map[action[0]]:
					piece = self._inner_pieces[piece_id] if (piece_id[0] in ['i', 'm']) else self._pieces[piece_id]
					for vertex in piece:
						x_rel = vertex[x_ax] - axis_anchor[x_ax]
						y_rel = vertex[y_ax] - axis_anchor[y_ax]

						if (action[1] == '+' and (action[0] in ['F', 'L', 'U'])) or (action[1] == '-' and (action[0] in ['D', 'B', 'R'])):
							x_rel_new = x_rel * np.cos(theta) + y_rel * np.sin(theta)
							y_rel_new = y_rel * np.cos(theta) - x_rel * np.sin(theta)
						else:
							x_rel_new = x_rel * np.cos(theta) - y_rel * np.sin(theta)
							y_rel_new = y_rel * np.cos(theta) + x_rel * np.sin(theta)

						vertex[x_ax] = x_rel_new + axis_anchor[x_ax]
						vertex[y_ax] = y_rel_new + axis_anchor[y_ax]

				for piece in self._inner_pieces:
					vtx = 0.2 * np.array(self._inner_pieces[piece])
					tri = a3.art3d.Poly3DCollection([vtx])
					tri.set_color(self._piece_colors['n'])
					# tri.set_color('None')
					tri.set_edgecolor('k')
					ax.add_collection3d(tri)

				for piece in self._pieces:
					vtx = 0.2 * np.array(self._pieces[piece])
					tri = a3.art3d.Poly3DCollection([vtx])
					tri.set_color(self._piece_colors[self._display_state[piece[0]][int(piece[1])][int(piece[2])]])
					tri.set_edgecolor('k')
					ax.add_collection3d(tri)

				pl.draw()
				pl.pause(self._time)
			
			self.rotate(action, display=True)
			self.update_pieces()
			self.print_cube()

		pl.show()



def test_display():

	cube = DisplayCube()
	cube.display_pieces()


def test_rotate():

	cube = DisplayCube()
	cube.display_rotate('R+')
	cube.display_pieces()

	cube.print_cube()


def test_sequence_algorithm():

	cube = DisplayCube()

	cube.shuffle(50)
	cube.print_cube()

	cube.sequence_algorithm(['U+', 'R+'])

	cube.display_sequence_algorithm(['U+', 'R+'])

	cube.display_pieces()



def test_3dplot_1():

	ax = a3.Axes3D(pl.figure())
	for i in range(10):
		vtx = sp.rand(3,3)
		tri = a3.art3d.Poly3DCollection([vtx])
		tri.set_color(colors.rgb2hex(sp.rand(3)))
		tri.set_edgecolor('k')
		ax.add_collection3d(tri)

	pl.show()


def test_3dplot_2():

	ax = a3.Axes3D(pl.figure())
	vtx = [
		[0, 0, 0],
		[0, 0, 1],
		[1, 0, 1],
		[1, 0, 0]
	]
	tri = a3.art3d.Poly3DCollection([vtx])
	tri.set_color('yellow')
	tri.set_edgecolor('k')
	ax.add_collection3d(tri)

	pl.show()


def test_display_solve():

	cube = DisplayCube()

	cube.shuffle(50)
	cube.print_cube()

	stage = cube.get_cur_stage()
	print(stage)

	cube.solve()
	cube.print_cube()

	cube.display_sequence_algorithm(cube._actions)




if __name__ == '__main__':

	# test_display()

	# test_rotate()

	# test_sequence_algorithm()

	test_display_solve()

	

