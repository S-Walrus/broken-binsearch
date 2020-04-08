from decimal import Decimal
import decimal

decimal.getcontext().prec = 500

class ProbDistributor:
	def __init__(self, p_truth, p_lie, length):
		self.p_lie = Decimal(p_lie)
		self.p_truth = Decimal(p_truth)
		self.P = [Decimal(1) / length for _ in range(length)]

	def update(self, j, response, req='a'):
		T = self.P[:]
		P = self.P
		if req == 'a':
			for i in range(len(P)):
				if not response:
					p_x_a = self.p_truth if i <= j else self.p_lie
					p_a = P[i]
					p_na = Decimal(1) - p_a
					p_x_na = self.p_truth * (sum(P[:j+1]) - P[i]) + self.p_lie * sum(P[j+1:])
				else:
					p_x_a = self.p_truth if i > j else self.p_lie
					p_a = P[i]
					p_na = Decimal(1) - p_a
					p_x_na = self.p_truth * (sum(P[j+1:]) - P[i]) + self.p_lie * sum(P[:j+1])
				p_a_x = p_x_a * p_a / (p_x_a * p_a + p_x_na * p_na)
				T[i] = p_a_x
		self.P = T
		return sum(T)
