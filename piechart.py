# GRÁFICO EM FORMATO DE PIZZA (PIE CHART)
# @author: Marcos Paulo de Oliveira
# Github: https://github.com/Marcospaulo-o

import matplotlib.pyplot as plt

labels = ['Exemplo 1', 'Exemplo 2', 'Exemplo 3']        # Dados que serão exibidos nos gráficos.
size = [60, 17, 23]                                     # Dados para a criação das fatias proporcionais.
cores = ['#A0A0A0', '#FF8000', '#3399FF']               # Cores que vão ser usadas.
explode = (0, 0, 0.1)                                   # "Salta" as fatias, distancia do centro.

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

fig1, ax1 = plt.subplots()
ax1.pie(size, explode=explode, colors=cores,            # Plotando o gráfico com as suas devidas configurações.
        autopct=make_autopct(size), pctdistance=0.7,
        shadow=False, startangle=190)

ax1.set_title("Resultado", fontsize=20)                 # Titulo do gráfico.
ax1.axis('equal')
plt.legend(labels=labels, loc='upper right',            # Configuração da legenda do gráfico (Bloco)
           fontsize=12)
#plt.savefig('pie_chart.png', dpi=300)                  # Salva o gráfico em formato .png.
plt.show()
