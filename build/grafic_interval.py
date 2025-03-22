import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class Grafic:
    def __init__(self, a, v, p, interval: tuple[float, float] = (0, 10)):
        self.interval = interval
        self.vi = v + a*(interval[0])
        self.pi = p + v*(interval[0]) + 0.5*a*(interval[0])**2
        self.vf = v + a*(interval[1])
        self.pf = p + v*(interval[1]) + 0.5*a*(interval[1])**2
        self.x = [i/10 for i in range(0, int(interval[1]*10) + int(interval[0]*10) + 10)]
        self.ya = [a for i in self.x]
        self.yv = [v + a*i for i in self.x]
        self.yp = [p + v*i + 0.5*a*i**2 for i in self.x]
        self.dv = self.vf - self.vi
        self.dp = self.pf - self.pi

        self.plot()

    def plot(self):
        plt.figure(figsize=(10, 6))

        plt.subplot(3, 1, 1)
        plt.plot(self.x, self.ya, label='Aceleración')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.axvline(self.interval[0], color='red', linewidth=1)
        plt.axvline(self.interval[1], color='red', linewidth=1)
        plt.fill_between(self.x, self.ya, where=[self.interval[0] <= x <= self.interval[1] for x in self.x], color='blue', alpha=0.3)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.ylabel('Aceleración')
        plt.legend()
        plt.text(self.interval[1], min(self.ya) - 1, f'Area Bajo la Curva o Cambio en la Velocidad {self.dv:.2f}', horizontalalignment='right')

        plt.subplot(3, 1, 2)
        plt.plot(self.x, self.yv, label='Velocidad', color='orange')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.axvline(self.interval[0], color='red', linewidth=1)
        plt.axhline(self.vi, color='gray', linewidth=2, label='Velocidad Inicial')
        plt.plot([self.interval[1], self.interval[1]], [self.vi, self.vf], color='blue', linewidth=2)
        plt.fill_between(self.x, self.yv, where=[self.interval[0] <= x <= self.interval[1] for x in self.x], color='purple', alpha=0.3)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.ylabel('Velocidad')
        plt.legend()
        plt.text(self.interval[1], min(self.yv) - 1, f'Area Bajo la Curva o Cambio de posicion {self.dp:.2f}', horizontalalignment='right')

        plt.subplot(3, 1, 3)
        plt.plot(self.x, self.yp, label='Posición', color='green')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.axvline(self.interval[0], color='red', linewidth=1)
        plt.axhline(self.pi, color='gray', linewidth=2, label='Posición Inicial')
        plt.axvline(self.interval[1], self.pi, self.pf, color='green', linewidth=2)
        plt.plot([self.interval[1], self.interval[1]], [self.pi, self.pf], color='purple', linewidth=2)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.xlabel('Tiempo')
        plt.ylabel('Posición')
        plt.legend()

        plt.tight_layout()
        plt.show()