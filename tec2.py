import matplotlib.pyplot as plt
import numpy as np
# plt.gca().invert_yaxis()
a_tok = []
v_1_ = []
v_2_ = []
v_3_ = []
time = [0.004*i for i in range(1,486)]
# print(time)
with open("C:/Users/pasha/Downloads/Telegram Desktop/п2.txt", 'r') as file:
    for i, line in enumerate(file.readlines()[15:500]):
        v_3, v_2, v_1, a_1 = map(float, line.strip().split('\t'))
        if (i < 500):
          a_tok.append(a_1)
          v_3_.append(v_3)
          v_2_.append(v_2)
          v_1_.append(v_1)
# a_tok = np.array(a_tok)
# time = np.array(time)
 # Создаем список пар (x, y) и сортируем по x
# Разделяем отсортированные пары обратно на массивы x и y
# print(len(v_3_),len(v_2_),len(v_1_),len(a_tok))
            
plt.plot(time, a_tok, label='I')
plt.plot(time, v_3_, label='Uc')
plt.plot(time, v_2_, label='Ul')
plt.plot(time, v_1_, label='u')
plt.xlabel('t(мс) ')
plt.ylabel('I(мА), U(В)')
for i in range(10):
  print(a_tok[i], v_3_[i])
# print(a_tok)
# # Включение легенды
plt.legend()

# Отображение сетки
plt.grid(True)
# plt.
# Отображение графика
plt.show()