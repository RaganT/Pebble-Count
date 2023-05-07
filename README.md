## Topic:

This repo addresses a need for an automated pebble count analysis. I am a member of the 2023-2024 Stream Restoration capstone team. We learn through experience and conceptual design the process behind stream restoration and enhancement projects. The pebble count is an assessment of the varying sizes of rocks that make up a stream bed. Enviornmental engineers use this assessment to make stream assessments and decisions for restoration.


## Programs:

The main programs I used in this code were pandas, numpy, and matplotlib. I used the dataframe funtion in pandas to make data processing easier. I used numpy to when I needed to find the 50th and 84th percentile. I used matplotlib to aid in creating the code deliverables.


## Walkthrough:

The code starts off with the proper CSV file opened. I convert the data into a dataframe for easier manipulation. I then seperate the data based off of location by creating a seperate dataframe for the riffle, pool, and glide. I then use for loops to find the frequency that each pebble size occurs. The frequencies are then plotted against the sizes for the first graph. To find the cumulative percentage of each location, I use for loops to find the individual percentage of each pebble size against the total for that location. To find the cumulative percentage, I added the values in the list to each other, in an ascending order. Utilizing numpy, I found the 50th and 84th percentile and graphed the cumulative percentages ogarithmically.


## Results:

The deliverables of this code are two graphs. The first graph shows the amount of each pebble size found. The second graph shows the cumulative percentage of size, as well as the 50th and 84th percentile.


## Limitations:

Limitations of this code is that the data needs to be already organized in two columns, the left column being Size and the right location being Location. Location is also limited by riffle, pool, and glilde.


## Discussion of future results:

There are a few changes I aim to make for future revisions. I would like to be able to integrate another location: run. I would also like to learn more about the plotting libraries and create one graph, instead of two.
