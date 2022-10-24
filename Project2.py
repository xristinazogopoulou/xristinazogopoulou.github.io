import json 
import matplotlib.pyplot as plt
f = open('rowws.json')
rowws = json.load(f)
print (rowws)

year_x= [2020,2019,2018,2017]
population_y= [20,34,35,36]
data = rowws[1]
for i in data:
    year_x.append(i['year'])
    population_y.append(i['population'])

plt.plot=(year_x,population_y,color='#444444',linestyle='-',label= 'population over the years', marker='o')
plt.xlabel('Population')
plt.ylabel=('Year')
plt.title('Population in India by year')
plt.legend('Population over the year')
plt.show()

#fig = plt.figure()
#plt.bar(xAxis,yAxis, color='maroon')
#plt.xlabel('variable')
#plt.ylabel('value')
#dictionary = json.load(open('file.json', 'r'))
#xAxis = [key for key, value in dictionary.items()]
#yAxis = [value for key, value in dictionary.items()]
#plt.grid(True)