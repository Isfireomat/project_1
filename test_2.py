import matplotlib.pyplot as plt
import numpy as np

# Создаем данные для графиков
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Создаем первый график
plt.subplot(2, 1, 1)  # 2 строки, 1 столбец, первый график
plt.plot(x, y1)
plt.title('График 1')

# Создаем второй график
plt.subplot(2, 1, 2)  # 2 строки, 1 столбец, второй график
plt.plot(x, y2)
plt.title('График 2')

# Общая ось для обоих графиков
plt.subplots_adjust(hspace=0.5)  # Устанавливаем пространство между графиками
plt.xlabel('Общая ось')

# Показываем графики
plt.show()
