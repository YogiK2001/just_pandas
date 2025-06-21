import numpy as np

class FuelDataAnalyzer:
    def __init__(self):
        pass

    # 1. Create Fuel Consumption Array
    def create_fuel_array(self, fuel_list: list) -> np.ndarray:
        return np.array(fuel_list)

    # 2. Validate Fuel Array
    def validate_fuel_array(self, fuel_array: np.ndarray) -> bool:
        return np.size(fuel_array) > 0 and np.all(fuel_array >= 0)

    # 3. Compute Fuel Summary
    def compute_fuel_summary(self, fuel_array: np.ndarray) -> tuple:
        total = np.sum(fuel_array)
        avg = np.mean(fuel_array)
        max_val = np.max(fuel_array)
        return (total, avg, max_val)

    # 4. Apply Discount on Bulk Fuel Usage (>100 litres → 10% discount)
    def apply_bulk_discount(self, fuel_array: np.ndarray) -> np.ndarray:
        return np.where(fuel_array > 100, fuel_array * 0.9, fuel_array)

    # 5. Flag Heavy Consumption Trips
    def flag_heavy_consumption(self, fuel_array: np.ndarray) -> np.ndarray:
        return np.where(
            fuel_array > 100, "High Risk",
            np.where(fuel_array > 70, "Moderate Risk", "Stable")
        )

    # 6. Format Fuel Records
    def format_fuel_readings(self, fuel_array: np.ndarray) -> np.ndarray:
        return np.array([f"{x:.2f} Litres" for x in fuel_array])
