# -*- coding: utf-8 -*-
"""C112_Data_story.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bJ9I4irSOTSfr2hefplKbgUZQ4gixMka

# Data Story
### To analyse if reminders to save increase savings.

\
**Note** - Some columns represent values in 0s and 1s. 0 is equivalent to False whereas 1 is equivalent to True.
"""

#Importing the important modules

import pandas as pd
import statistics
import plotly.express as px

"""Now let's visualise the data to see if we can find anything?"""

#Uploading the csv
from google.colab import files
data_to_load = files.upload()

#Plotting the graph
df = pd.read_csv("savings_data_final.csv")
fig = px.scatter(df, y="quant_saved", color="rem_any")
fig.show()

"""If we look at this data, we can see that the yellow dots are the ones who were given a reminder to save (**Since 1 stands for True**) while the blue dots are the ones who were not given a reminder to save.

\
We can also see that most of the outliers are the Blue dots, who have saved more than others.

\
Let's try to see how many people were given a reminder v/s the people who were not given a reminder.
"""

import csv

with open('savings_data_final.csv', newline="") as f:
  reader = csv.reader(f)
  savings_data = list(reader)

savings_data.pop(0)

#Finding total number of people and number of people who were reminded
total_entries = len(savings_data)
total_people_given_reminder = 0
for data in savings_data:
  if int(data[3]) == 1:
    total_people_given_reminder += 1

import plotly.graph_objects as go

fig = go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y=[total_people_given_reminder, (total_entries - total_people_given_reminder)]))

fig.show()

"""Here, we can see that about 8 thousand people were reminded, compared to about 5 thousand people who were not reminded to save.

Let's see what is the mean, median and mode of the savings made by people.
"""

#Mean, median and mode of savings
all_savings = []
for data in savings_data:
  all_savings.append(float(data[0]))

print(f"Mean of savings - {statistics.mean(all_savings)}")
print(f"Median of savings - {statistics.median(all_savings)}")
print(f"Mode of savings - {statistics.mode(all_savings)}")

"""Now these are some very interesting results! Can you guess why the mean, median and the mode is not same and worlds apart?

\
If we go back and look at the scatterplot we plotted before, we can see that majority of the savings data lies between 0 to 100.

\
Now, since we have a few outliers, which are the blue dots that are away from the rest of the crowd, our mean has significantly increased from the median, since it is the sum of all values by total entries. Since the outliers lie far away from the crowd, the difference is huge.

\
Similarly, for mode, in our data, there are a lot of people who didn't save at all. Thus, the mode of the data is 0. Mode is the value with maximum occurences.

\
Let's see if we have a similar massive difference between the mean, median and mode of people who got reminded and people who didn't receive reminders.
"""

#Mean, median and mode of savings
reminded_savings = []
not_reminded_savings = []
for data in savings_data:
  if int(data[3]) == 1:
    reminded_savings.append(float(data[0]))
  else:
    not_reminded_savings.append(float(data[0]))

print("Results for people who were reminded to save")
print(f"Mean of savings - {statistics.mean(reminded_savings)}")
print(f"Median of savings - {statistics.median(reminded_savings)}")
print(f"Mode of savings - {statistics.mode(reminded_savings)}")
#To add new lines
print("\n\n")
print("Results for people who were not reminded to save")
print(f"Mean of savings - {statistics.mean(not_reminded_savings)}")
print(f"Median of savings - {statistics.median(not_reminded_savings)}")
print(f"Mode of savings - {statistics.mode(not_reminded_savings)}")

"""Again, there seems to be massive differences between the mean, median and modes of savings of people who were both reminded and not reminded. We can conclude this with the same explaination as above.

\
Let's first calculate the standard deviation of the data.
"""

#Standard Deviation
print(f"Standard deviation of all the data -> {statistics.stdev(all_savings)}")
print(f"Standard deviation of people who were reminded -> {statistics.stdev(reminded_savings)}")
print(f"Standard deviation of people who were not reminded -> {statistics.stdev(not_reminded_savings)}")

"""Here, we can see that the standard deviation varies a lot in all three types of data.

\
It is higher for the people who were not reminded v/s the people who were reminded.

\
Looking at the data up until now, we can assume that reminding people to save did not have a significant effect.

\
From standard deviations, we can see that the people who were not reminded have much more scattered data than people who were reminded. 

\
The question is, does this data have a correlation? Let's see if the savings are corellated to the age of people.

\
**Note** - The columns that have age as 0 will not be considered, since their age is missing. No one can be saving data at the age of 0
"""

import numpy as np

age = []
savings = []
for data in savings_data:
  if float(data[5]) != 0:
    age.append(float(data[5]))
    savings.append(float(data[0]))

correlation = np.corrcoef(age, savings)
print(f"Correlation between the age of the person and their savings is - {correlation[0,1]}")

"""Here, we receive the correlation between the age and the savings to be 0.03, which means that the given data is not correlated.

\
Let's see if this given data for savings follow a bell curved normal distribution
"""

import plotly.figure_factory as ff

fig = ff.create_distplot([df["quant_saved"].tolist()], ["Savings"], show_hist=False)
fig.show()