'''
Activity: What is ‘good’ data visualization?

Is the visualization pleasing to look at? 
Does the visualization accurately represent data?
Can we understand what message the maker of the visualization is attempting to convey?
Consider factors such as colour, size, use of images. Is this a ‘good’ data visualization? Why or why not?

Slide 20 Plot:

The visualization seems to be conveying that life expectancy is highest in Oceania, 
lowest in Africa, and so on during the year of 2007. However, the title is 
confusing - there is not enough details about whether this is the actual meaning.

It would have been more pleasing to look at a 2D plot. It is not clear what
the purpose of making the bars 3D is, which makes it harder to read. It is hard 
to estimate the numerical differences between the continents based on 
the axis ticks because the 3D bars are projecting diagonally. The shadows don't
seem to be informative. The axis tick spacing looks confusing, it is not clear
why they chose these ranges to represent. The legend is unnecessary since the
bars themselves are colored. The use of a parchment background does not seem to 
add information. There is no source citations so we do not know where they got
these numbers.

Slide 21 Plot:

The visualization seems to be conveying that campaign expenditures rise every
year, and there seems to be a political call to action about it in regards
to voting. 

The use of the creature makes the visualization eye-catching. It also gives 
source citations which is good for knowing where the data comes from. However, 
the diagonal orientation of the plot makes it hard to read, especially since the
bars seem to not be in the same dimension. It is eye-catching but discourages
you from looking to closely at the data.

Slide 22 Plot:

The visualization seems to be conveying difference in aspect ratios changes how 
quickly we perceive the value to increase with each unit increase in x.

The lack of labels for value, x, the lines, and source information makes the 
exact message and information being conveyed unclear, however. 

Slide 23 Plot:

The visualization seems to be conveying the percentage of people backing three
GOP candidates.

However, the fact that the percentages do not add up to 100% makes it confusing
what percentages are actually being shown. Furthermore, the numbers are offset
from the chart. The pie chart also seems to have almost the same size for each
category despite the difference in percentages. It is also slanted, making it 
hard to interpret. The background color also matches the color of one of the 
categories. The shiny effect on the pie chart also does not seem to have any use. 
It is nice that the source information is cited, but it is not clear what that 
source refers to just based on two words.

Slide 24 Plot:

The visualization seems to be conveying wind speed and direction in the US at a
given date.

The movement of the wind is pleasing to look at and gives information about the 
direction. Source information is presented, which is also good. However, the 
exact mph is not very clear from the legend and how the wind speed is presented. 
Furthermore, why the specific cities and the size of the dots are questions which
do not seem to be easily answered.

Key Points:

Important qualities of data visualization include aesthetic (i.e., pleasing
to look at), substantiative (i.e., accurately and honestly present data), and
perceptual (i.e., the message of the visualization is conveyed well).

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
y = np.random.randint(0,100,50)

# Generate scatter plot.
fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x,y)

# Generate bar plot.
fig, ax = plt.subplots(figsize=(5,3))
ax.bar(x,y)

# Generate line plot.
fig, ax = plt.subplots(figsize=(5,3))
ax.plot(x,y)

# Generate histogram.
fig, ax = plt.subplots(figsize=(5,3))
ax.hist(y)

# Add axis labels and titles to line plot.
fig, ax = plt.subplots(figsize=(5,3))
ax.plot(x,y)
ax.set_title('Total growth over time')
ax.set_ylabel('Total growth')
ax.set_xlabel('Years since start')
fig.tight_layout()

# Modify labels and titles in line plot.
font1 = {'family':'sans-serif','color':'blue','size':20}
font2 = {'family':'monospace','color':'green','size':14}
fig, ax = plt.subplots(figsize=(5,3))
ax.plot(x,y)
ax.set_title('Total growth over time',fontdict=font1)
ax.set_ylabel('Total growth',fontdict=font2)
ax.set_xlabel('Years since start',fontdict=font2)
fig.tight_layout()

# Change color and marker for scatter plot.
fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x,y,
           marker='*',
           color="indigo") 
fig.show()

# Add line with line style and width for scatter plot.
fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x,y,
           marker='*',
           color="indigo",
           linestyle='--', 
           linewidth=2) 
fig.show()

# Use hex code for color for scatter plot.
fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x,y,
           marker='*',
           color="#7425b9",
           linestyle='--', 
           linewidth=2) 
fig.show()

# Change marker size, marker edge, and marker face for scatter plot.
fig, ax = plt.subplots(figsize=(5,3))
ax.plot(x,y,
        marker='*',
        markersize = 12, 
        color = '#7425b9', 
        linestyle = '--', 
        linewidth = 2, 
        markeredgecolor = '#fa9359', 
        markerfacecolor = '#000000' ) 
fig.show()

# Add grid lines to scatter plot, and modify color, line width, and line style.
fig, ax = plt.subplots(figsize=(5,3))
ax.plot(x,y,
        marker='*',
        markersize = 12, 
        color = '#7425b9', 
        linestyle = '--', 
        linewidth = 2, 
        markeredgecolor = '#fa9359', 
        markerfacecolor = '#000000' ) 
ax.grid(axis='y', 
        color="blue", 
        linewidth=2,
        linestyle='-.')
fig.show()

'''
Activity: Python Graph Gallery

https://python-graph-gallery.com/404-dendrogram-with-heat-map/

Aesthetic: I think it succeeds in this area because the heat map and the 
dendrogram look visually appealing, especially the colors and sizing. 
Substantive: I think it might be more informative to make the x-axis labels
vertical and spell out the full word rather than abbreviations. 
Perceptual: It seems pretty clear that the heatmap indicates a car's value on a 
specific variable and the dendrogram indicates which cars have similar 
distributions of values across variables.

'''

# Libraries
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
 
# Data set
url = 'https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/mtcars.csv'
df = pd.read_csv(url)
df = df.set_index('model')
 
# Standardize or Normalize every column in the figure
# Standardize:
sns.clustermap(df, standard_scale=1)
plt.show()

# Normalize
sns.clustermap(df, z_score=1)
plt.show()
