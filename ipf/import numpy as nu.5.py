import numpy as nu
from numpy import array,mean,median,std,percentile,random
import statistics

a=array([1,2,3,4,5,6,7,8,9,10])
#print(a)
mean = mean(a)
median = median(a)
standard_deviation = std(a)
mod = statistics.mode(a)
print(mod)


print(mean)
print(median)
print(standard_deviation)


b=array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
percentage = percentile(b,80)
print(percentage)

rand = random.randint(100,size=(5,10))
print(rand)

c = random.normal(10,2,10000)
print(len(c))#len()length 




