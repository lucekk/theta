import math

class MeanSquaredMethod:

    def __init__(self, x_points, y_points):
        self._last_squares_fit(x_points, y_points)

    def _dot(self, v, w):
        return sum(vi * wi for vi, wi in zip(v,w))

    def _sum_of_squares(self, v):
        return self._dot(v, v)

    def _mean(self, x):
        return sum(x) / len(x)

    def _de_mean(self, x):
        x_bar = self._mean(x)
        return [xi - x_bar for xi in x]

    def _variance(self, x):
        n = len(x)
        deviations = self._de_mean(x)
        return self._sum_of_squares(deviations) / (n - 1)

    def _standard_deviation(self, x):
        return math.sqrt(self._variance(x))

    def _coviarance(self, x, y):
        n = len(x)
        return self._dot(self._de_mean(x), self._de_mean(y)) / (n - 1)

    def _correlation(self, x, y):
        stdev_x = self._standard_deviation(x)
        stdev_y = self._standard_deviation(y)
        if stdev_x > 0 and stdev_y > 0:
            return self._coviarance(x, y) / stdev_x / stdev_y
        else:
            return 0

    def _last_squares_fit(self, x, y):
        self._beta = self._correlation(x, y) * self._standard_deviation(y) / self._standard_deviation(x)
        self._alpha = self._mean(y) - self._beta * self._mean(x)
        
    def get_alpha_and_beta_to_straight_equation(self):
        return self._alpha, self._beta
    '''
    def predict(alpha, beta, xi):
        return beta *xi + alpha

    def error(alpha, beta, xi, yi):
        return yi - predict(alpha, beta, xi)

    def sum_of_squad_errors(alpha, beta, x, y):
        return sum(error(alpha, beta, xi, yi) ** 2
                for xi, yi in zip(x, y))
    '''