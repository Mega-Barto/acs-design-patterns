from models.algorithm import AlgorithmOptimization

class SimpleAlgorithm(AlgorithmOptimization):
    def update(self, state):
        """
        Applies a simple optimization strategy based on available stock.
        If a product count falls below 50, it triggers a restocking alert.
        """
        print("[Simple Algorithm] Checking inventory...")

        for product, quantity in state.get("products", {}).items():
            if quantity < 50:
                print(f"⚠ Warning: Low stock for {product} ({quantity} units). Consider restocking.")

        print("[Simple Algorithm] Optimization complete.\n")
