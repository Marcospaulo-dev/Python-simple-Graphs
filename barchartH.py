import matplotlib.pyplot as plt
import numpy as np

cores = ['#000033', '#0066CC', '#0080FF', '#3399FF',
         '#66B2FF', '#99CCFF', '#99CCFF', '#99CCFE']
qnt = [100, 200, 500, 1000, 5000, 10000, 50000, 100000]
time = [0.002996922, 0.011967659, 0.085800409, 0.369423389,
        8.895563841, 37.81426978, 1158.773203, 10189.93415]

y_pos = np.arange(len(time))                                                                                            # Quantidade de elemento que haverão no eixo Y
arredondamento = []
c = 0

for i in time:                                                                                                          # Laço 'for' para arredondar os numeros grandes (numeros grandes invadem os espaços um do outro no grafico)
    a = time[c]
    arredondamento.append(str(round(a, 3)))
    c = c+1

plt.barh(y_pos, arredondamento, align='center', alpha=0.5,                                                              # Configurações pro PLOT do grafico.
         color=cores, edgecolor='black', linewidth=1)
plt.yticks(y_pos, qnt)                                                                                                  # Posição aonde os dados entram.
plt.title('Cocktail Sort: Tempo X Quantidade de elementos')
plt.xlabel("Tempo (segundos)")
plt.ylabel('Qnt. Elementos')
plt.grid(linestyle='dotted', axis='x', color='black', linewidth=1.5)
plt.show()
