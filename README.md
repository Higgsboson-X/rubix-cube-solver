# Rubix-Cube-Solver
A primary rubik's cube solver in python using matplotlib and opencv.

## Overview
This is a rubik's cube solver with beginner's algorithm from [beginner's algorithm](https://how-to-solve-a-rubix-cube.com/). It first reads the faces of a real rubik's cube using opencv and passes the states to the solver. Then it displays the move sequence in animation using matplotlib.

## Dependencies
- Python v3.6.5
- numpy v1.14.3
- Opencv-python v4.1.0.25
- matplotlib v3.0.3

## Run
To setup the solver, change directory to `code` and run
```
$ python solver.py
```

### Capture the Rubik's Cube
![capture cube](https://github.com/Higgsboson-X/rubix-cube-solver/blob/master/images/1.png "Capture Cube")

Then an opencv window using PC camera should appear. The letter on the left-top square indicates the face of the rubik's cube. Place the rubik's cube inside the squares as prompted and adjust the color shown in each piece by clicking inside the corresponding square. If the color shows `n`, then the color is not recognized and manual adjustment is required. If the colors are correct, click the `Set` square to confirm the colors. After that, the colors are insensible to live video changes. To make the colors sensible to live video, click `Set` again. The mapping of the colors and faces is shown in the following table.

|     Face    |    Color     |
|:-----------:|:------------:|
| Front \[F\] |  Red \[r\]   |
|  Left \[L\] | Green \[g\]  |
|  Back \[B\] | Orange \[o\] |
| Right \[R\] |  Blue \[b\]  |
|  Up \[U\]   | White \[w\]  |
|  Down \[D\] | Yellow \[y\] |

### View Initial State
When all six faces are recorded, a rubik's cube in the recorded face should be displayed in a matplotlib figure. Confirm that the state is correct and close the window.

![confirm state](https://github.com/Higgsboson-X/rubix-cube-solver/blob/master/images/2.PNG "Confirm State")

### Solve
Then the animation of solving the rubik's cube should appear, and it stops when the cube is solved. The following figures show a screenshot of the solving animation and the final solved state.

![solving](https://github.com/Higgsboson-X/rubix-cube-solver/blob/master/images/3.PNG "Solving")
![final](https://github.com/Higgsboson-X/rubix-cube-solver/blob/master/images/4.PNG "Final")

## Notes
1. The current color recognition is crude and is significantly influenced by conditions of the environment, mainly lighting conditions.
2. The beginner's algorithm is not an efficient algorithm for solving rubik's cube. This implementation takes 200 moves to solve a cube on average.
3. A user interface might be constructed in future development.
