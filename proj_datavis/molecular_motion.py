#15-3 molecular motion 
#
import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Make a random walk, and plot the points
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    
    # Set the size of the plotting window
    plt.figure(figsize=(20, 18))
    
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    

        
    #Remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()

    

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
        
