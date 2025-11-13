"""
Unit-тесты для модулей square.py, rectangle.py и circle.py
Тестирование функций вычисления площадей и периметров геометрических фигур
"""
import unittest
import math
import square
import rectangle
import circle


class SquareTestCase(unittest.TestCase):
    """Тесты для модуля square.py"""
    
    def test_area_positive(self):
        """Тест площади квадрата с положительной стороной"""
        result = square.area(5)
        self.assertEqual(result, 25)

    def test_area_positive_v2(self):
        """Тест площади квадрата с положительной стороной ещё один"""
        result = square.area(6)
        self.assertEqual(result, 36)
    
    def test_area_zero(self):
        """Тест площади квадрата с нулевой стороной"""
        result = square.area(0)
        self.assertEqual(result, 0)
    
    def test_area_float(self):
        """Тест площади квадрата с дробной стороной"""
        result = square.area(2.5)
        self.assertAlmostEqual(result, 6.25, places=7)
    
    def test_area_large(self):
        """Тест площади квадрата с большой стороной"""
        result = square.area(1000)
        self.assertEqual(result, 1000000)
    
    def test_area_small(self):
        """Тест площади квадрата с малой стороной"""
        result = square.area(0.1)
        self.assertAlmostEqual(result, 0.01, places=7)
    
    def test_perimeter_positive(self):
        """Тест периметра квадрата с положительной стороной"""
        result = square.perimeter(5)
        self.assertEqual(result, 20)
    
    def test_perimeter_zero(self):
        """Тест периметра квадрата с нулевой стороной"""
        result = square.perimeter(0)
        self.assertEqual(result, 0)
    
    def test_perimeter_float(self):
        """Тест периметра квадрата с дробной стороной"""
        result = square.perimeter(2.5)
        self.assertAlmostEqual(result, 10.0, places=7)
    
    def test_perimeter_large(self):
        """Тест периметра квадрата с большой стороной"""
        result = square.perimeter(1000)
        self.assertEqual(result, 4000)
    
    def test_perimeter_small(self):
        """Тест периметра квадрата с малой стороной"""
        result = square.perimeter(0.01)
        self.assertAlmostEqual(result, 0.04, places=7)


class RectangleTestCase(unittest.TestCase):
    """Тесты для модуля rectangle.py"""
    
    def test_area_positive(self):
        """Тест площади прямоугольника с положительными сторонами"""
        result = rectangle.area(10, 5)
        self.assertEqual(result, 50)
    
    def test_area_zero_both(self):
        """Тест площади прямоугольника с нулевыми сторонами"""
        result = rectangle.area(0, 0)
        self.assertEqual(result, 0)
    
    def test_area_zero_one(self):
        """Тест площади прямоугольника с одной нулевой стороной"""
        result = rectangle.area(10, 0)
        self.assertEqual(result, 0)
    
    def test_area_square(self):
        """Тест площади квадрата через функцию прямоугольника"""
        result = rectangle.area(7, 7)
        self.assertEqual(result, 49)
    
    def test_area_float(self):
        """Тест площади прямоугольника с дробными сторонами"""
        result = rectangle.area(3.5, 2.5)
        self.assertAlmostEqual(result, 8.75, places=7)
    
    def test_area_large(self):
        """Тест площади прямоугольника с большими сторонами"""
        result = rectangle.area(1000, 2000)
        self.assertEqual(result, 2000000)
    
    def test_area_small(self):
        """Тест площади прямоугольника с малыми сторонами"""
        result = rectangle.area(0.1, 0.2)
        self.assertAlmostEqual(result, 0.02, places=7)
    
    def test_perimeter_positive(self):
        """Тест периметра прямоугольника с положительными сторонами"""
        result = rectangle.perimeter(10, 5)
        self.assertEqual(result, 30)
    
    def test_perimeter_zero_both(self):
        """Тест периметра прямоугольника с нулевыми сторонами"""
        result = rectangle.perimeter(0, 0)
        self.assertEqual(result, 0)
    
    def test_perimeter_zero_length(self):
        """Тест периметра прямоугольника с нулевой длиной"""
        result = rectangle.perimeter(0, 10)
        self.assertEqual(result, 20)
    
    def test_perimeter_zero_width(self):
        """Тест периметра прямоугольника с нулевой шириной"""
        result = rectangle.perimeter(10, 0)
        self.assertEqual(result, 20)
    
    def test_perimeter_square(self):
        """Тест периметра квадрата через функцию прямоугольника"""
        result = rectangle.perimeter(7, 7)
        self.assertEqual(result, 28)
    
    def test_perimeter_float(self):
        """Тест периметра прямоугольника с дробными сторонами"""
        result = rectangle.perimeter(3.5, 2.5)
        self.assertAlmostEqual(result, 12.0, places=7)
    
    def test_perimeter_large(self):
        """Тест периметра прямоугольника с большими сторонами"""
        result = rectangle.perimeter(1000, 2000)
        self.assertEqual(result, 6000)
    
    def test_perimeter_small(self):
        """Тест периметра прямоугольника с малыми сторонами"""
        result = rectangle.perimeter(0.1, 0.2)
        self.assertAlmostEqual(result, 0.6, places=7)


class CircleTestCase(unittest.TestCase):
    """Тесты для модуля circle.py"""
    
    def test_area_positive(self):
        """Тест площади круга с положительным радиусом"""
        result = circle.area(5)
        expected = math.pi * 25
        self.assertAlmostEqual(result, expected, places=7)
    
    def test_area_zero(self):
        """Тест площади круга с нулевым радиусом"""
        result = circle.area(0)
        self.assertEqual(result, 0)
    
    def test_area_one(self):
        """Тест площади круга с радиусом 1"""
        result = circle.area(1)
        expected = math.pi
        self.assertAlmostEqual(result, expected, places=7)
    
    def test_area_float(self):
        """Тест площади круга с дробным радиусом"""
        result = circle.area(3.5)
        expected = math.pi * 3.5 * 3.5
        self.assertAlmostEqual(result, expected, places=7)
    
    def test_area_large(self):
        """Тест площади круга с большим радиусом"""
        result = circle.area(1000)
        expected = math.pi * 1000000
        self.assertAlmostEqual(result, expected, places=7)
    
    def test_area_small(self):
        """Тест площади круга с малым радиусом"""
        result = circle.area(0.01)
        expected = math.pi * 0.0001
        self.assertAlmostEqual(result, expected, places=7)
    
    def test_area_calculation(self):
        """Тест точности вычисления площади круга"""
        result = circle.area(10)
        self.assertAlmostEqual(result, 314.1592653589793, places=7)
    
    def test_perimeter_positive(self):
        """Тест периметра круга с положительным радиусом"""
        result = circle.perimeter(5)
        expected = 2 * math.pi * 5
        self.assertAlmostEqual(result, expected, places=7)
    
    def test_perimeter_zero(self):
        """Тест периметра круга с нулевым радиусом"""
        result = circle.perimeter(0)
        self.assertEqual(result, 0)
    
    def test_perimeter_one(self):
        """Тест периметра круга с радиусом 1"""
        result = circle.perimeter(1)
        expected = 2 * math.pi
        self.assertAlmostEqual(result, expected, places=7)
    
    def test_perimeter_float(self):
        """Тест периметра круга с дробным радиусом"""
        result = circle.perimeter(3.5)
        expected = 2 * math.pi * 3.5
        self.assertAlmostEqual(result, expected, places=7)
    
    def test_perimeter_large(self):
        """Тест периметра круга с большим радиусом"""
        result = circle.perimeter(1000)
        expected = 2 * math.pi * 1000
        self.assertAlmostEqual(result, expected, places=7)
    
    def test_perimeter_small(self):
        """Тест периметра круга с малым радиусом"""
        result = circle.perimeter(0.01)
        expected = 2 * math.pi * 0.01
        self.assertAlmostEqual(result, expected, places=7)
    
    def test_perimeter_calculation(self):
        """Тест точности вычисления периметра круга"""
        result = circle.perimeter(10)
        self.assertAlmostEqual(result, 62.83185307179586, places=7)


if __name__ == '__main__':
    # Запуск тестов с подробным выводом
    unittest.main(verbosity=2)