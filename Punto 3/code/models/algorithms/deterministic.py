from models.algorithm import AlgorithmOptimization

class DeterministicAlgorithm(AlgorithmOptimization):
    def update(self, state):
        """
        Uses a deterministic approach by forecasting future demand 
        and adjusting stock levels accordingly.
        """
        print("[Deterministic Algorithm] Running demand forecast...")

        for product, quantity in state.get("products", {}).items():
            forecasted_demand = quantity * 0.2  # Assume 20% daily depletion rate
            suggested_stock = quantity + forecasted_demand

            print(f"🔍 {product}: Current stock = {quantity}, Recommended stock = {suggested_stock:.2f}")

        print("[Deterministic Algorithm] Optimization complete.\n")
