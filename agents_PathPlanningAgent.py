from utils_path_optimizer import RLPathOptimizer

class PathPlanningAgent:
    def __init__(self):
        self.optimizer = RLPathOptimizer()

    def optimize_path(self, order_data: dict, constraints: dict) -> list:
        self.optimizer.set_constraints(constraints)
        optimal_path = self.optimizer.run_optimization(order_data)
        return optimal_path
