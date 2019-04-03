import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
SP = [80] * 150 + [50] * 150 + [25] * 150 + [75] * 500
area = 10000  # cm^2
inputValveCoefficient = 1000  # cm^3/s
outputValveCoefficient = 1600  # cm^3/s
timeStep = 0.05
error = 0
valve = 0
level = 60
KP = 20

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 0.5), ylim=(0, 150))

patch = patches.Rectangle((0, 0), .5, -100, fc='blue')
time_template = 'time = %.1fs'
time_text = ax.text(0.4, 0.9, '', transform=ax.transAxes)

def init_1():
    time_text.set_text('')
    ax.add_patch(patch)
    return patch, time_text

def init_2():
    ax.add_patch(patch)

    return patch,

def animate(i):
    global level
    # P-Conroller
    error = 1*(level - SP[i])
    valve = ((KP * error)/100)
    valve = max(0,valve)
    valve = min(1,valve)
    valveOutput = valve*outputValveCoefficient
    level = level + ((1 / (area ^ 2)) * (inputValveCoefficient - valveOutput))
    print(error)
    patch.set_xy([0, level])
    time_text.set_text(time_template % (i * timeStep))

    return patch,time_text,


anim = animation.FuncAnimation(fig, animate,init_func=init_1,interval=25,blit=True,repeat = True)
anim1 = animation.FuncAnimation(fig,animate,init_func=init_2)

plt.show()