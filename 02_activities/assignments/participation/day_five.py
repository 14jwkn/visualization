'''
Activity: How did this diagram of the Brooks use rational, moral, and emotional appeal to make a case to its audiences?

Rational: Shows extremely crowded conditions for slaves quantitatively.
Moral: Highlights inhuman conditions such as having to crawl to move through the 
ship and number of people crowded within.
Emotional: Evokes sympathy for the slaves by showing the conditions in the ship, 
facilitating audience vicarious experience of it.

Activity: Comparing data visualizations

Bar plot shows data for a specific dataset while the scatter plot shows the 
overall trend, sample size differences. Scatter plot has more depth in the 
information given and can result in a more subjective and different interpretation 
depending on the viewer, bar plot is easier to understand reducing cognitive load. 

Activity: Types of changes
Immediate or transitional changes occur as X and Y axes change when switching options, 
data point positions change. Elements that stay constant include what color 
represents male and female. To improve, could make order of Y axis constant to 
make it easier to compare between departments and different words. 

'''

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import PIL
import requests

# Load tips dataset.
tips = sns.load_dataset("tips")
print(tips)

# Line plot.
sns.lineplot(data=tips, # choose our dataset
            x='total_bill', # define our x variable
            y='tip') # define our y variable

# Set style for line plot.
sns.set_style('whitegrid')
sns.lineplot(data=tips, # choose our dataset
            x='total_bill', # define our x variable
            y='tip') # define our y variable

# Add labels to line plot.
tipgraph = sns.lineplot(data=tips,
                        x='total_bill',
                        y='tip')
tipgraph.set(title='Tips vs. Total Bill',
            xlabel='Total Bill ($)',
            ylabel='Tip Amount ($)')

# Change figure size, color, marker style, and line style in line plot.
fig = plt.subplots(figsize=(10, 3))
tipgraph = sns.lineplot(data=tips,
                        x='total_bill',
                        y='tip',
                        color = 'hotpink',
                        linestyle = '--',
                        linewidth = 3,
                        marker = 'o',
                        markerfacecolor = 'indigo')

# Change features of scatter plot by category.
tipgraph = sns.scatterplot(data=tips, x='total_bill',
                            y='tip', style = 'time', hue =
                            'day', palette = ['purple',
                            'hotpink', 'deepskyblue',
                            'yellowgreen'])
tipgraph.set(title='Tips vs. Total Bill',
            xlabel='Total Bill ($)',
            ylabel='Tip Amount ($)')

# Generate pair plot which shows distributions of variables on diagonal and 
# scatterplots between variables off diagonal.
sns.pairplot(data = tips, hue = 'day')

'''
Activity: Comment this snippet of code and describe what each new element is doing/
'''

# Generate relative plot which splits scatter plot into different plots per
# category level. 
daysplot = sns.relplot(data=tips, # Generates relative plot using tips dataset.
                        x="total_bill", # Defines X variable.
                        y="tip", # Defines Y variable.
                        hue="sex", # Colors by sex.
                        col="day", # Splits into different plots by day.
                        kind="scatter", # Specifies scatter plot.
                        col_wrap=2) # Wraps around after two columns.


# Import plotly library.
import plotly.graph_objects as go # 'go' is 'graph objects’

# Set sample data.
x1 = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y1 = np.array([110, 180, 240, 99, 220])

# Make bar plot with titles and save it as HTML to embed in webpage.
graph = go.Figure()
graph.add_trace(go.Bar(x=x1, y=y1))
graph.update_layout(title="Pirate Scores",
                    xaxis_title="Pirates",
                    yaxis_title="Score")
graph.show()
graph.write_html("pirategraph.html")

# Make and customize plotly scatter plot.
graph = go.Figure()
graph.add_trace(go.Scatter(x=x1, y=y1, mode='markers', # we want points for a scatter plot
marker=dict(size=15, # point size
            color='hotpink', # point colour
            opacity=1, # point transparency/alpha
            line=dict(width=5, color='purple') # point outline
            )))
graph.update_layout(title='Interactive Pirate Plot',
                    xaxis_title='Pirates',
                    yaxis_title='Scores',
                    width=500, height=500)

# Import word cloud library.
from wordcloud import WordCloud

# Load sample dataset of movie quotes.
df = pd.read_csv("https://raw.githubusercontent.com/prasertcbs/basic-dataset/master/movie_quotes.csv",
                on_bad_lines='skip')

# Make word cloud for quote variable. 
text = " ".join(each for each in df.quote) # join all our text into a string
wordcloud = WordCloud(background_color="white", # generate our wordcloud image
                    colormap = 'inferno').generate(text)
fig, ax = plt.subplots(figsize=(7, 3)) # use matplotlib syntax to put image in figure
ax.imshow(wordcloud, # add picture to matplotlib axes
        interpolation='bilinear') # help smooth image
ax.axis("off")

# Import venn diagram library.
from matplotlib_venn import venn2, venn2_circles, venn2_unweighted

# Load sample dataset.
A = set(["apple", "banana", "watermelon"])
B = set(["pumpkin", "blueberry", "apple", "key lime"])

# Assign sets to circles with custom appearance, showing counts in each set by
# default.
diagram = venn2_unweighted([A, B],
                        set_labels = ('Fruits', 'Pies'),
                        set_colors=("blue", "red"),
                        alpha=0.5)
plt.show()

# See strings in each set, and modify venn diagram to see different versions.
diagram.get_label_by_id("10").set_text("n".join(A - B))
diagram.get_label_by_id("11").set_text("n".join(A & B))
diagram.get_label_by_id("01").set_text("n".join(B - A))
