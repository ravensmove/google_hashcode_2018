from solver import Solver
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-file')
    args = parser.parse_args()

    solver = Solver(args.file)
    solver.solve_problem()
