from ortools.sat.python import cp_model

model = cp_model.CpModel()
solver = cp_model.CpSolver()

# 1. Variable
army = model.NewIntVar(1, 100000, 'army')

# 2. Constraints
model.AddModuloEquality(0, army, 13)
model.AddModuloEquality(0, army, 19)
model.AddModuloEquality(0, army, 37)
class PrintSolutions(cp_model.CpSolverSolutionCallback):
    """Callback to print every solution."""
    def __init__(self, variable):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variable = variable
    def on_solution_callback(self):
        print(self.Value(self.__variable))

# Solve with callback
solution_printer = PrintSolutions(army)
solver.parameters.enumerate_all_solutions = True
status = solver.Solve(model, solution_printer)