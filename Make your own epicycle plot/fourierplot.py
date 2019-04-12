from presentation import *
import numpy as nm
import matplotlib.animation

time_table, x_table, y_table = create_close_loop(sys.argv[1])

order = int(sys.argv[2])
coef=coef_list(time_table, x_table, y_table, order)
print(coef)

space = np.linspace(0,tau,300)
x_DFT = [DFT(t, coef, order)[0] for t in space]
y_DFT = [DFT(t, coef, order)[1] for t in space]

fig, ax = plt.subplots(figsize=(5, 5))
ax.plot(x_DFT, y_DFT, 'r--')
ax.plot(x_table, y_table, 'k--')
ax.set_aspect('equal', 'datalim')
xmin, xmax = xlim()
ymin, ymax = ylim()
# fig.savefig('finalimage.jpg')

anim = visualize(x_DFT, y_DFT, coef, order, space, [xmin, xmax, ymin, ymax])

if(sys.argv[3] == 'plot'):
    plt.show()
elif(sys.argv[3] == 'save'):
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=30)
    anim.save('epicycle.mp4', writer=writer, dpi=300)