import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Данные: часы учебы в неделю и итоговые оценки
horas_estudio = np.array([1, 2.5, 3.5, 4.2, 4.5, 5.3, 6, 6.3, 7, 8.5], dtype='float16')
notas = np.array([2, 3, 3.5, 3.7, 4, 4.2, 4.5, 4.6, 4.8, 5], dtype='float16')

# Выполняем линейную регрессию
slope, intercept, r_value, p_value, std_err = linregress(horas_estudio, notas)

"""
используем функцию `linregress` из `scipy.stats` для вычисления параметров линейной регрессии:
уклона (slope), пересечения (intercept).
А также характеристик показывающий качество фитинга модели:
коэффициента корреляции (r_value), p-значения (p_value) и стандартной ошибки (std_err)
"""

# Выводим параметры регрессии
print(f'Slope: {slope}')
print(f'Intercept: {intercept}')
print(f'R^2: {r_value**2}')
print(f'p-value: {p_value}')
print(f'Standard error: {std_err}')

print(f'y={slope:.2f}*x+{intercept:.2f}')

# Функция для предсказания
def predict(x):
    return slope * x + intercept
"""
Мы определяем функцию `predict`, которая принимает значение `x` (часы учебы)
и возвращает предсказанное значение `y` (итоговая оценка).
"""

# Создаем значения для линии регрессии
regression_line = predict(horas_estudio)

# Построение графика
plt.scatter(horas_estudio, notas, color='blue', label='Данные')
plt.plot(horas_estudio, regression_line, color='red', label='Линейная регрессия')
plt.xlabel('Часы учебы в неделю')
plt.ylabel('Итоговые оценки')
plt.legend()
plt.title('Простая линейная регрессия')
plt.show()
