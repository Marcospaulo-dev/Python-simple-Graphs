# GRÁFICO EM FORMATO DE BARRA (BAR CHART)
# @author: Marcos Paulo de Oliveira
# Github: https://github.com/Marcospaulo-o

import numpy as np
import matplotlib.pyplot as plt

objects = ('01/01', '02/04', '03/04', '04/04',              # Dados que serão exibidos nos gráficos.
           '05/04', '06/04', '07/04')
y_pos = np.arange(len(objects))                             # Contagem do comprimento dos 'objects'
performance = [5,19,28,14,106,63,53]                        # Dados para a criação das barras proporcionais.
cores = ['#000033', '#0066CC', '#0080FF', '#3399FF',        # Cores que vão ser usadas.
         '#66B2FF', '#99CCFF', '#99CCFF']

for index, value in enumerate(performance):                 # Criação dos numeros acima das barras.
    plt.text(index, value, str(value), fontsize=12,
             color='black', ha='center', va='bottom')

plt.bar(y_pos, performance, align='center', alpha=0.5,      # Plotando o gráfico com as suas devidas configurações.
        color=cores, edgecolor='black', linewidth=1)
plt.xticks(y_pos, objects)                                  # Colocando os numeros acima das barras no gráfico.
plt.ylabel('Y - Data Label')                                # Dados Y.
plt.xlabel('X - Data Label')                                # Dados X.
plt.title('Title')                                          # Titulo do gráfico.
                # Adicionando 'grid' na horizontal.
#plt.savefig('bar_chart.png', dpi=350)
plt.show()