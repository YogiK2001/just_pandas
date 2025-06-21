import numpy as np

class StockAnalyzer:
	def create_stock_array(self, stocks):
		return np.array(stocks)
		
	def validate_stocks(self, arr):
		return arr.size > 0 and np.all(arr >= -100) and np.all(arr <= 100)
		
	def compute_stocks(self, arr):
		return round(arr.mean(), 2), round(arr.std(), 2), round(arr.max(), 2)
		
	def flag_stocks(self, arr):
		return np.where(arr > 5, 'High Risk', np.where(arr > 2, 'Moderate Risk', 'Stable'))
		
	def longest_loss_streak(self, arr):
		streak = 0
		max_streak = 0
		for val in arr:
			if val < 0:
				streak += 1
				max_streak = max(max_streak, streak)
			else:
				streak = 0
		return max_streak