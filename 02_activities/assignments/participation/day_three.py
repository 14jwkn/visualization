'''
Activity: Comment our code

It is helpful to include information about what you are trying to do in the code
blocks in plain language so you and others can understand it in the future, which
aids reproducibility by letting you (if you forget) and others run it
in the future. A good comment contains all the necessary information to 
understand it, but is brief so that it is efficient to read.

'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import PIL
import requests

# Set simulated data.
np.random.seed(613)
x = np.arange(50)
y1 = np.random.randint(0,100,50)
y2 = np.random.randint(0,100,50)

# Make line plot with both y variables.
fig, ax = plt.subplots(figsize=(5,3))
ax.plot(x,y1)
ax.plot(x,y2)
fig.show()

# Add legend and line labels to line plot.
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x,y1, label = "Person 1" )
ax.plot(x,y2, label = "Person 2" )
ax.legend(loc='lower right')
fig.show()

# Customize legend for line plot.
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x,y1, label = "Person 1")
ax.plot(x,y2, label = "Person 2")
ax.legend(loc='lower right',
            frameon = True, # Controls whether there is a box in the legend.
            fontsize = 12, 
            ncol = 2, # Controls how legend items are staggered.
            shadow = True ) # Controls whether there is a shadow in the legend.
fig.show()

# Move legend outside of plot area for line plot.
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x,y1, label = "Person 1")
ax.plot(x,y2, label = "Person 2")
ax.legend(loc='upper left',
bbox_to_anchor =(1, 1))
fig.show()

# Generate scatter plot and add a text annotation anchored to a data point.
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend(loc='lower right')
ax.text(10, 95, "This value is important!")
fig.show()

# Modify text annotation on scatter plot.
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend(loc='lower right')
ax.text(10, 95, "This value is important!",
ha='center', 
color = 'red', 
size = 20) 
fig.show()

# Add text annotations with reference to data, axes, and figure.
fig, ax = plt.subplots()
ax.axis([0, 10, 0, 10])
ax.text(1, 5, ". Data:(1, 5)", transform=ax.transData )
ax.text(0.5, 0.1, ". Axes:(0.5, 0.1)", transform=ax.transAxes ) # X percent of the whole area.
ax.text(0.2, 0.2, ". Figure:(0.2, 0.2)", transform=fig.transFigure )

# Add annotations with arrows to scatter plot.
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend(loc='lower right')
ax.annotate('This is important!', 
            xy=(10, 95), 
            xytext=(20, 94),
            arrowprops=dict(facecolor='black'))
fig.show()

# Modify the arrow annotations in the scatter plot.
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend(loc='lower right')
ax.annotate('This is important!',
            xy=(10, 95), xytext=(20, 94),
            arrowprops = dict(arrowstyle = "wedge",
            color = "hotpink"))
fig.show()

# Remove tick marks and labels from scatter plot.
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend(loc='lower right')
ax.yaxis.set_major_locator(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullFormatter())

# Limit number of tick marks in scatter plot.
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend(loc='lower right')
ax.xaxis.set_major_locator(plt.MaxNLocator(3))

# Change tick mark interval in scatter plot.
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend(loc='lower right')
ax.xaxis.set_major_locator(plt.MultipleLocator(5))

# Rotate axis labels in scatter plot.
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend(loc='lower right')
plt.xticks(rotation=45,ha='right')

# Modify axis title font and color in scatter plot.
font1 = {' family':'serif','color':'indigo'}
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend(loc='lower right')
plt.xlabel('Shiny New X Axis!', fontsize = 18, fontdict = font1)

# Check premade styles for plots.
plt.style.available

# Use style for plot.
plt.style.use('fivethirtyeight')
np.random.seed(613)
x = np.arange(50)
y1 = np.random.randint(0,100,50)
y2 = np.random.randint(0,100,50)
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x,y1)
ax.plot(x,y2)
fig.show()
