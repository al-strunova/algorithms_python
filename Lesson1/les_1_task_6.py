# По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним
first_side = int(input("введите длину первого отрезка: "))
second_side = int(input("введите длину второго отрезка: "))
third_side = int(input("введите длину третьего отрезка: "))
if (first_side + second_side) <= third_side or (first_side + third_side) <= second_side or (
        second_side + third_side) <= first_side:
    print("Треугольник не существует")
elif first_side != second_side and second_side != third_side and first_side != third_side:
    print("Треугольник разносторонний")
elif first_side == second_side == third_side:
    print("Треугольник равносторонний")
else:
    print("Треугольник равнобедренный")
