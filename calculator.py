import math
import matplotlib.pyplot as plt
import numpy as np

class History:
    def __init__(self):
        self._history = []
    def add_records(self, category, operation, result):
        self._history.append({'category': category, 'operation': operation, 'result': result})
    def show(self):
        if not self._history:
            print('История пуста')
            return
        for record in self._history:
            cat = record['category']
            op = record['operation']
            res = record['result']
            print(f'{cat}: {op} = {res}')
    def clear(self):
        self._history = []
class BasedCalculator:
    def __init__(self, history):
        self._history = history
    def AddOperation(self, a, b):
        result = a + b
        self._history.add_records(category='Арифметика', operation=f'{a} + {b}', result=result)
        return result
    def MinusOperation(self, a, b):
        result = a - b
        self._history.add_records(category='Арифметика', operation=f'{a} - {b}', result=result)
        return result
    def UmnohOperation(self, a, b):
        result = a * b
        self._history.add_records(category='Арифметика', operation=f'{a} * {b}', result=result)
        return result
    def DeleniaOperation(self, a, b):
        if b == 0:
            error = 'Ошибка деление на ноль'
            self._history.add_records(category='Арифметика', operation=f'{a} / {b}', result=error)
            return error
        result = a / b
        self._history.add_records(category='Арифметика', operation=f'{a} / {b}', result=result)
        return result
class Trigonometria:
    def __init__(self, history):
        self._history = history
    def sin(self, degrees):
        radians = math.radians(degrees)
        result = math.sin(radians)
        self._history.add_records(category='Тригонометрия', operation=f'sin({degrees}°)', result=result)
        return result
    def cos(self, degrees):
        radians = math.radians(degrees)
        result = math.cos(radians)
        self._history.add_records(category='Тригонометрия', operation=f'cos({degrees}°)', result=result)
        return result
    def tan(self, degrees):
        radians = math.radians(degrees)
        result = math.tan(radians)
        self._history.add_records(category='Тригонометрия', operation=f'tan({degrees}°)', result=result)
        return result
    def asin(self, value):
        radians = math.asin(value)
        result = math.degrees(radians)
        self._history.add_records(category='Тригонометрия', operation=f'asin({value})', result=result)
        return result
    def acos(self, value):
        radians = math.acos(value)
        result = math.degrees(radians)
        self._history.add_records(category='Тригонометрия', operation=f'acos({value})', result=result)
        return result
    def atan(self, value):
        radians = math.atan(value)
        result = math.degrees(radians)
        self._history.add_records(category='Тригонометрия', operation=f'atan({value})', result=result)
        return result
class GraphCalculator:
    def __init__(self):
        pass
    def plot_expression(self, expression, x_min=-360, x_max=360):
        #  Создаем массив X в градусах от -360 до 360
        x_deg = np.linspace(x_min, x_max, 1000)
        # Для вычислений внутри eval переводим x в радианы
        x = np.radians(x_deg)
        allowed_names = {
            'x': x,
            'np': np,
            'sin': np.sin,
            'cos': np.cos,
            'tan': np.tan,
            'sqrt': np.sqrt,
            'pi': np.pi
        }
        try:
            # Вычисляем значения Y
            y = eval(expression, {"__builtins__": None}, allowed_names)
            if 'tan' in expression:
                y[np.abs(y) > 20] = np.nan
                plt.ylim(-10, 10)
            # Строим график, где по оси X передаем градусы (x_deg)
            plt.figure(figsize=(10, 5))
            plt.plot(x_deg, y, label=expression, color='blue', linewidth=2)
            # Настраиваем сетку, подписи на оси X кратно 90 градусам
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.xticks(np.arange(x_min, x_max + 1, 90))
            plt.xlabel('Градусы (°)')
            plt.ylabel('Y')
            plt.title(f'График функции: {expression}')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.legend()
            plt.show()
        except Exception as e:
            print(f"Ошибка при вычислении выражения: {e}")
class MatrixCalc(BasedCalculator):
    def __init__(self, history):
        super().__init__(history)
    def _get_dimensions(self, matrix):
        return len(matrix), len(matrix[0])
    def MatrixAdd(self, A, B):
        if self._get_dimensions(A) != self._get_dimensions(B):
            return "Ошибка: матрицы должны быть одинакового размера"
        result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
        self._history.add_records(category="Матрицы", operation=f"{A} + {B}", result=result)
        return result
    def MatrixMinus(self, A, B):
        if self._get_dimensions(A) != self._get_dimensions(B):
            return "Ошибка: матрицы должны быть одинакового размера"
        result = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
        self._history.add_records(category="Матрицы", operation=f"{A} - {B}", result=result)
        return result
    def MatrixUmn(self, A, B):
        rows_A, cols_A = self._get_dimensions(A)
        rows_B, cols_B = self._get_dimensions(B)
        if cols_A != rows_B:
            return "Ошибка: число столбцов матрицы A должно быть равно числу строк матрицы B"
        result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]
        self._history.add_records(category="Матрицы", operation=f"{A} * {B}", result=result)
        return result
    def MatrixDel(self, A, b):
        if b == 0:
            return "Ошибка: деление матрицы на ноль"

        result = [[A[i][j] / b for j in range(len(A[0]))] for i in range(len(A))]
        self._history.add_records(category="Матрицы", operation=f"{A} / {b}", result=result)
        return result
class IntegrationCalculator:
    def __init__(self, history):
        self._history = history
    def IntegrateOperation(self, func, a, b, n=1000):
        if n <= 0:
            raise ValueError("Количество шагов разбиения должно быть больше нуля!")
        h = (b - a) / n
        total = 0.5 * (func(a) + func(b))
        for i in range(1, n):
            total += func(a + i * h)

        result = total * h
        func_name = getattr(func, '__name__', 'f(x)')
        self._history.add_records(
            category="Интегрирование",
            operation=f"∫ от {a} до {b} для {func_name} (n={n})",
            result=result
        )
        return result
    def get_history(self):
        return self._history
def func1(x):
    return x ** 2 + 3 * x
def func2(x):
    return x ** 2 + 3 * x + 1
def func3(x):
    return x ** 3 - 2 * x + 5
def func4(x):
    return math.sin(x) + math.cos(x)
def func5(x):
    return 2 * x ** 2 - 4 * x + 1
def square(x):
    return x ** 2
def sine(x):
    return math.sin(x)
def exp_plus_x(x):
    return math.exp(x) + x
def linear(x):
    return 3 * x + 1
def polynomial(x):
    return x ** 4 - 2 * x ** 3 + 3 * x ** 2 - 4 * x + 5
class EngineeringCalculator:
    def __init__(self):
        self._history = History()
        self.arithmetic = BasedCalculator(self._history)
        self.trigonometria = Trigonometria(self._history)
        #self.graphic = GraphCalculator(self._history)
        self.matrix = MatrixCalc(self._history)
        self.integration = IntegrationCalculator(self._history)
    def show_history(self):
        self._history.show()
history = History()
calc1 = BasedCalculator(history)
calc2 = Trigonometria(history)
calc3 = GraphCalculator()#
print("Обычный калькулятор\n")
print("Сложение", calc1.AddOperation(10, 5))
print("Вычитание", calc1.MinusOperation(10, 5))
print("Умножение", calc1.UmnohOperation(10, 5))
print("Деление", calc1.DeleniaOperation(10, 5))
print("Деление на 0", calc1.DeleniaOperation(10, 0))
print("\n") 
print("Тригонометрия\n")
print("Синус 30°:", f"{calc2.sin(30):.1f}")
print("Косинус 90°:", f"{calc2.cos(90):.1f}")
print("Тангенс 45°:", f"{calc2.tan(45):.1f}")
print("Арксинус 90°:", f"{calc2.asin(0.5):.1f}")
print("Арккосинус 60°:", f"{calc2.acos(0.5):.1f}")
print("Арктангенс 30°:", f"{calc2.atan(1):.1f}")
print("\n")

print("История операций\n")
history.show()
print('\n')
print("График\n")
calc3.plot_expression('sqrt((2*pi)**2 - x**2)')

#calc1 = EngineeringCalc()
#calc1.arithmetic.AddOperation(2, 4)
#calc1.arithmetic.MinusOperation(2, 4)
#calc1.arithmetic.DeleniaOperation(2, 4)
#alc1.arithmetic.UmnohOperation(2, 4)
#calc1.trigonometria.cos(60)
#matrix_A = [[1, 2], [3, 4]]
#matrix_B = [[5, 6], [7, 8]]
#calc1.matrix.MatrixAdd(matrix_A, matrix_B)
#calc1.matrix.MatrixUmn(matrix_A, matrix_B)
#calc1.integration.IntegrateOperation(func2, 0, 2)#
#calc1.integration.IntegrateOperation(func3, -1, 2)
#calc1.integration.IntegrateOperation(func4, 0, math.pi, n=5000)
#calc1.integration.IntegrateOperation(func5, -1, 3)
#print('История всех операция\n')
#calc1.show_history()
