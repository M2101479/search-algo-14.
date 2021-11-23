import random
import time

start=time.time()

fruits= [i for i in range(1000000)]


def find(element,value):
  
  while True:
    random_element=random.choice(element)
    if random_element == value:
      return random_element 
    elif value not in element:
      return False
  


end=time.time()

print(find(fruits,int(input('Enter a number'))))
print("It took ",end-start,' seconds')

#test1-0.11911129951477051  seconds with 45
#test 2- 0.16582441329956055 seconds with 45
#test 3- 0.22660422325134277  seconds with 45
#test 4- 0.13206791877746582  seconds with 45
#test 5-  0.19592642784118652  seconds with 45
#test 6- average is 0.16790685653 seconds