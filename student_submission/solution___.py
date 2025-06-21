import numpy as np

class TemperatureAnalyzer:
    
    # 1. Create Temperature Array
    def create_temperature_array(self, temperatures: list) -> np.ndarray:
        return np.array(temperatures)

    # 2. Validate Temperature Array
    def validate_temperature_array(self, temperature_array: np.ndarray) -> bool:
        return np.all((temperature_array >= 30) & (temperature_array <= 45))

    # 3. Compute Temperature Metrics (avg, max, min)
    def compute_temperature_metrics(self, temperature_array: np.ndarray) -> tuple:
        avg = np.round(np.mean(temperature_array), 2)
        max_val = np.max(temperature_array)
        min_val = np.min(temperature_array)
        return (avg, max_val, min_val)

    # 4. Detect Abnormal Temperatures
    def detect_abnormal_temperatures(self, temperature_array: np.ndarray) -> np.ndarray:
        return np.where(
            temperature_array < 35, "Hypothermia",
            np.where(temperature_array > 37.5, "Fever", "Normal")
        )

    # 5. Identify Longest Normal Temperature Streak
    def longest_normal_temperature_streak(self, temperature_array: np.ndarray) -> int:
        normal_mask = (temperature_array >= 35) & (temperature_array <= 37.5)
        longest_streak = current_streak = 0
        for is_normal in normal_mask:
            if is_normal:
                current_streak += 1
                longest_streak = max(longest_streak, current_streak)
            else:
                current_streak = 0
        return longest_streak

    # 6. Format Temperature Readings
    def format_temperature_readings(self, temperature_array: np.ndarray) -> np.ndarray:
        return np.array([f"{temp:.2f} °C" for temp in temperature_array])
