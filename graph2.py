import matplotlib.pyplot as plt

#x-coordinates of left sides of bars
left = [1,2,3,4,5]

# heights of bars
height=[10,20,30,40,50]

# labels for bars
tick_label = ['one','two','three','four','five']


# plotting a bar chart
plt.bar(left, height, tick_label= tick_label,
		width= 0.8, color= ['red','green'])

#naming x axis
plt.xlabel('x axis')
#naming y axis
plt.ylabel('y axis')
# plot tittle
plt.title('My bar chart!')

# function to show the plot
plt.show()