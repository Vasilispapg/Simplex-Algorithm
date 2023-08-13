# Simplex Problem Solver

This Python script implements the Simplex method to solve linear programming problems with equality constraints. The script iteratively optimizes the given objective function subject to the provided constraints.

## Prerequisites

To run this script, you need to have the following installed:

- Python (3.x recommended)
- `tabulate` library: You can install it using `pip`:

## Usage

1. Clone the repository or download the script `simplex_solver.py`.

2. Open a terminal and navigate to the directory containing the script.

3. Run the script using Python:

4. Follow the on-screen instructions to input the objective function coefficients and constraint coefficients.

5. The script will perform iterations of the Simplex method to find the optimal solution (or determine if no solution exists).

## Script Overview

- `fix_the_lists()`: Initializes data structures for the problem.
- `isdone()`: Checks if the solution is optimal or not.
- `arxikopoisi_zj_cj()`: Initializes the `zj_cj` list.
- `find_min_zj_cj()`: Finds the entering variable.
- `calculate_th()`: Calculates the ratios for the leaving variable.
- `find_min_Th()`: Finds the leaving variable.
- `line_operations()`: Performs row operations.
- `divide_the_line()`: Divides the pivot row.
- `make_everyting_0()`: Updates other rows.
- `fix_the_base()`: Updates basic variables.
- `find_zj_cj()`: Calculates updated `zj_cj` values.
- `calculate_zj()`: Calculates updated `zj` values.

## Note

This code is provided as a simplified implementation for educational purposes. It may require further testing and modification to handle various problem instances.
