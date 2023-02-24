import matplotlib.pyplot as plt

# Define the size of the house in square meters
house_size = 100

# Define the dimensions of the house in meters
length = 10 # 10 meters
width = house_size / length # calculate the width based on the given size

# Create a figure and axis object
fig, ax = plt.subplots()

# Set the x and y limits of the plot
ax.set_xlim([0, length])
ax.set_ylim([0, width])

# Add a rectangle patch to represent the house
rect = plt.Rectangle((0, 0), length, width, linewidth=1, edgecolor='r', facecolor='none')
ax.add_patch(rect)

# Label the x and y axes and add a title to the plot
ax.set_xlabel('Length (m)')
ax.set_ylabel('Width (m)')
ax.set_title('House Blueprint ({} m²)'.format(house_size))

# Show the plot
plt.show()
