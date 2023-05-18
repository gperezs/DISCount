import numpy as np
import matplotlib.pyplot as plt


def plot_line(F, F_hat, CI, lw=5, lw2=1.5, step=3, title='',
                    colors = ['teal', 'maroon', 'olive', 'blue', 'orange']):

    plt.plot(np.arange(1,len(F)+1), F, color=colors[0], linestyle='-', linewidth=lw, 
             alpha=0.3, label='Ground truth')

    plt.plot(np.arange(1,len(F)+1)[::step], F_hat[::step], color=colors[1], linestyle='-', 
             linewidth=lw2, alpha=0.5, marker='x', label='Estimation')
    plt.fill_between(np.arange(1,len(F)+1)[::step], 
                     np.array(F_hat)[::step]-np.array(CI)[::step], 
                     np.array(F_hat)[::step]+np.array(CI)[::step],
                     alpha=0.05, edgecolor=colors[1], facecolor=colors[1], hatch='/')

    plt.ticklabel_format(axis='y', style='sci', scilimits=(5,5))
    plt.grid(True, color='gray', linestyle=':', linewidth=0.5)
    plt.ylim(bottom=0)
    plt.ylabel('Counts')
    plt.legend(loc='upper left')
    plt.title(title)


def plot_bar(F, F_hat, CI, lw=5, lw2=1.5, step=3, bw=0.35, title='',
                    colors = ['teal', 'maroon', 'olive', 'blue', 'orange']):

    plt.bar(np.arange(1,len(F)+1)-0.2, F, color=colors[0], linestyle='-', 
            linewidth=lw, alpha=0.3, label='Ground truth', width = bw)

    plt.bar(np.arange(1,len(F)+1)+0.2, F_hat, color=colors[1], linestyle='-', 
            linewidth=lw, alpha=0.3, label='Estimation', width = bw)
    plt.errorbar(np.arange(1,len(F)+1)+0.2, F_hat, yerr=CI, 
            capsize=5, fmt=".", color=colors[1], alpha=0.5)

    plt.ticklabel_format(axis='y', style='sci', scilimits=(5,5))
    plt.grid(True, color='gray', linestyle=':', linewidth=0.5)
    plt.ylim(bottom=0)
    plt.ylabel('Counts')
    plt.legend(loc='upper left')
    plt.title(title)
