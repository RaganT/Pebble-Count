# throughout my code I use 'cum'. It's short for cumulative

from os.path import exists
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import data from computer and create df for each location
path_to_data = r"C:\Users\Ragan Trask\Documents\GitHub\ENGR265-spring2023\Final Presentation\Pebble_Count_Data.csv"
dtypes = {'Size': int, 'Location': str}
data = pd.read_csv(path_to_data, dtype=dtypes)     # data is a dataframe
df = pd.DataFrame(data, columns=['Size', 'Location'])
riffle = df[df['Location'] == 'riffle']
pool = df[df['Location'] == 'pool']
glide = df[df['Location'] == 'glide']

sizes = [2, 4, 8, 11, 16, 32, 45, 64, 90, 128, 180, 256, 362, 512, 1024]
sizes_graph = range(len(sizes))

riff_size = riffle['Size'].values
pool_size = pool['Size'].values
glide_size = glide['Size'].values
cum_size = df['Size'].values

# find the frequency of each size at each location
freq_riff = []
for value in sizes:
    frequency = np.count_nonzero(riff_size == value)
    freq_riff.append(frequency)
freq_pool = []
for value in sizes:
    frequency = np.count_nonzero(pool_size == value)
    freq_pool.append(frequency)
freq_glide = []
for value in sizes:
    frequency = np.count_nonzero(glide_size == value)
    freq_glide.append(frequency)
freq_cum = []
for value in sizes:
    frequency = np.count_nonzero(cum_size == value)
    freq_cum.append(frequency)

# plot a bar graph with each location being a different color
# x-axis is all the sizes

plt.xlabel('Size of Pebbles')
plt.ylabel('Amount of each size')
plt.title('Pebble Count I')
plt.bar(sizes_graph, freq_cum, label='Cumulative Amounts')
#plt.bar(sizes_graph, freq_riff, label='Riffle amounts')
#plt.bar(sizes_graph, freq_glide, label='Glide amounts')
#plt.bar(sizes_graph, freq_pool, label='Pool amounts')
plt.xticks(sizes_graph, sizes)
plt.legend()
plt.show()
plt.plot()

# add up all the values in the freq lists and divide by the total length to get the individual percentages
cum_riff = []
for i in freq_riff:
    if i <= 0:
        cum_riff.append(i)
    if i > 0:
        ii = i / (sum(freq_riff))
        cum_riff.append(ii)
# add up each value to the next, in ascending order, to get cumulative percentage
exp_riff = []
result = 0
for k in cum_riff:
    result += (k * 100)
    exp_riff.append(result)

cum_pool = []
for i in freq_pool:
    if i <= 0:
        cum_pool.append(i)
    if i > 0:
        ii = i / (sum(freq_pool))
        cum_pool.append(ii)
exp_pool = []
result = 0
for k in cum_pool:
    result += (k * 100)
    exp_pool.append(result)

cum_glide = []
for i in freq_glide:
    if i <= 0:
        cum_glide.append(i)
    if i > 0:
        ii = i / (sum(freq_glide))
        cum_glide.append(ii)
exp_glide = []
result = 0
for k in cum_glide:
    result += (k * 100)
    exp_glide.append(result)

cum_cum = []
for i in freq_cum:
    if i <= 0:
        cum_cum.append(i)
    if i > 0:
        ii = i / (sum(freq_cum))
        cum_cum.append(ii)
exp_cum = []
result = 0
for k in cum_cum:
    result += (k * 100)
    exp_cum.append(result)

# find the 50th and 84th percentiles
P50 = (np.percentile(exp_cum, 50, 0))
diffs = abs(P50 - exp_cum)
D50 = np.argmin(diffs)
D50_x = sizes[D50]  # x
D50_y = exp_cum[D50]  # y
print("The 50th percentile size is:", D50_x)

P84 = (np.percentile(exp_cum, 84, 0))
diffs_84 = abs(P84 - exp_cum)
D84 = np.argmin(diffs_84)
D84_x = sizes[D84]  # x
D84_y = exp_cum[D84]  # y
print("The 84th percentile size is:", D84_x)

# plot the cumulative percentages on a xscale log graph
plt.xlabel('Size of Pebbles')
plt.ylabel('Cumulative Size')
plt.title('Pebble Count II')
plt.plot(sizes, exp_riff, 'm', label='Riffle')
plt.plot(sizes, exp_pool, 'g', label='Pool')
plt.plot(sizes, exp_glide, 'r', label='Glide')
plt.plot(sizes, exp_cum, 'b', label='Cumulative')
plt.scatter(D50_x, D50_y, marker='v', label="D50_cumulative")
plt.scatter(D84_x, D84_y, marker='v', label="D84_cumulative")
plt.legend()
plt.xscale('log')
plt.xticks(sizes, ('2', '4', '8', '11', '16', '32', '45', '64',
                   '90', '128', '180', '256', '362', '512', '1024'))
plt.show()
