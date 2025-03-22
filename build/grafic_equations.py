import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class Grafic:
    def __init__(self, a, v, p):
        self.x = [i/10 for i in range(100)]
        self.ya = [a for i in self.x]
        self.yv = [v + a*i for i in self.x]
        self.yp = [p + v*i + 0.5*a*i**2 for i in self.x]

        aux = f"p = {p}"
        if v != 0:
            aux += f'{v}t'
        if a != 0:
            aux += f' + (1/2)*{a}t²'
        self.equciones = {
            'Aceleración': f'a = {a}',
            'Velocidad': f'v = {v} + {a}t' if a != 0 else f'v = {v}',
            'Posición': aux
        }

        self.plot()

        

    def plot(self):
        plt.figure(figsize=(10, 6))

        plt.subplot(3, 1, 1)
        plt.plot(self.x, self.ya, label=f'Aceleración {self.equciones['Aceleración']}')
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
        plt.ylabel('Aceleración')
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(self.x, self.yv, label=f'Velocidad {self.equciones['Velocidad']}', color='orange')
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
        plt.ylabel('Velocidad')
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.plot(self.x, self.yp, label=f'Posición {self.equciones['Posición']}', color='green')
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
        plt.xlabel('Tiempo')
        plt.ylabel('Posición')
        plt.legend()

        plt.tight_layout()
        plt.show()