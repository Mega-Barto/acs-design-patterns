from models.inventory import Inventory
from models.algorithms.simple import SimpleAlgorithm
from models.algorithms.deterministic import DeterministicAlgorithm

if __name__ == "__main__":
    inventory = Inventory()

    algorithm1 = SimpleAlgorithm()
    algorithm2 = DeterministicAlgorithm()

    inventory.add_observer(algorithm1)
    inventory.add_observer(algorithm2)

    inventory.update_state({
    "products": {
        "Coffee Beans": 150,
        "Milk": 30,
        "Sugar": 70
    },
    "warehouses": 3
})

