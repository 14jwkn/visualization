'''
Activity: In what ways is this data visualization inaccessible, and to whom?

Small font, users with visual disabilities would have a harder time seeing. 
Jargon, users who do not know would have a harder time understanding.
Lack of alternative descriptive text means people using screen readers cannot 
access data. Relatedly, tactile or braille versions are hard and expensive to
create.

Activity: Alt-text

A Black woman in a white lab coat is discussing something with a White man in a 
business casual shirt in front of a fume hood in a chemistry lab. Can be different
essential text depending on the purpose of the image.

Activity: Four types of descriptive content

Level 1 - y-axis are famous creative people, x-axis is the 24 hours of a day,
the bars are colored by their daily routine including sleep, creative work,
day job or administration, food/leisure, exercise, and other.

Level 2 - There are some commonalities (i.e., correlations) in their activities
such as sleeping mostly at night and creative work mostly during the day. 

Level 3 - The commonalities might form interpretable patterns or trends.

Level 4 - The commonalities might mean something about how famous creative minds
differ from others.

'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import PIL
import requests

# Set simulated data.
np.random.seed(613)
x1 = np.arange(50)
y1 = np.random.randint(0, 75,50)
x2 = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y2 = np.array([110, 180, 240, 99, 220])

# Place visualizations in multiple defined plots after defining relative positions.
fig, (ax1, ax2) = plt.subplots(ncols=2,
                                nrows=1,
                                figsize=(7, 3))
ax1.scatter(x1,y1)
ax2.bar(x2,y2)
fig.show()

'''
Activity: Customizing our plots

'''

# Customize plots.
plt.style.use('fivethirtyeight')
fig, (ax1, ax2) = plt.subplots(ncols=2,
                                nrows=1,
                                figsize=(7, 3))
ax1.scatter(x1,y1,
            marker='*',
            color="indigo")
ax2.bar(x2,y2,
        color='#fa9359')
fig.show()

# Make sub plots without a grid arrangement and add visualizations.
fig, someaxes = plt.subplot_mosaic([['ax1', 'ax3'],
                                    ['ax2', 'ax3']],
figsize=(7, 4))
someaxes["ax1"].scatter(x1,y1)
someaxes["ax2"].bar(x2,y2)
someaxes["ax3"].plot(x1,y1)
plt.show()

# Add large axis labels and use layout changes to fit them, such as "constrained".
fig, someaxes = plt.subplot_mosaic([['ax1', 'ax3'],
['ax2', 'ax3']],
figsize=(7, 4),
layout = "constrained")
someaxes["ax1"].scatter(x1,y1)
someaxes["ax2"].bar(x2,y2)
someaxes["ax3"].plot(x1,y1)
someaxes["ax1"].set_xlabel('A Big Label', fontsize=18)
someaxes["ax2"].set_xlabel('Another Label', fontsize=18)
someaxes["ax3"].set_xlabel('Label 2: 2 Fast 2 Furious', fontsize=18)

# Add multiple visualizations within the same axes object, add error information
# with custom appearance.
x = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y1 = np.array([110, 180, 240, 99, 220])
y2 = np.array([170, 100, 90, 120, 50])
y2_sd = np.std(y2)
fig, ax = plt.subplots(figsize=(7, 3))
ax.bar(x, y1, color = "indigo")
ax.plot(x, y2, color = "red")
ax.errorbar(x, #our x values
            y2, #our y values
            yerr = y2_sd, #Specify vertical error bars.
            fmt = "none", #Specify not actual data points but only error.
            ecolor= "indigo",
            elinewidth= 4,
            capsize = 6,
            capthick= 4) 

# Only see error bars in intervals.
x = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y1 = np.array([110, 180, 240, 99, 220])
y2 = np.array([170, 100, 90, 120, 50])
y2_sd = np.std(y2)
fig, ax = plt.subplots(figsize=(7, 3))
ax.bar(x, y1, color = "indigo")
ax.plot(x, y2, color = "red")
ax.errorbar(x,
            y2,
            yerr = y2_sd,
            fmt = "none",
            ecolor = "indigo",
            elinewidth = 4,
            capsize = 6,
            capthick = 4,
            errorevery= 2 )

# Libraries to use images from internet.
from PIL import Image # to open images
import requests # to get images from URLs
from io import BytesIO # to store images

# Download image.
response = requests.get('https://upload.wikimedia.org/wikipedia/en/c/cb/Monkey_D_Luffy.png')
image_file = BytesIO(response.content)
image = Image.open(image_file)

# Make basic line plot and add new axis to figure as container for image,
# add image.
fig, ax = plt.subplots(figsize=(7, 3))
ax.plot(x, y2, color = "red")
ax_image = fig.add_axes([0.1, # x coordinate (ON FIGURE, NOT AXES)
                        0.11, # y coordinate (ON FIGURE, NOT AXES)
                        0.15, # image width
                        0.35]) # image height
ax_image.imshow(image)
ax_image.axis('off')

# Save visualization.
path = '.'
filename = '/fig1a.png'
plt.savefig(path+filename, dpi=300)
