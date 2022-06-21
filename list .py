
#1#Write a function that takes one argument as a list a=[2,4,6,8] and remove the second 
#last item from that list and returns the whole list without the removed item

def remove_items(list):
    list.remove(list[-2])
    return list
list1= [1,2,3,4,5,6,7]
print(remove_items(list=list1))


#2#Write a python program that has a list days = ["Monday","Tuesday","Friday","Monday"] and
#counts the number occurrences of Monday

def week_days(list):
    list=['mon','tue','wed','thur','fri','sat','mon','mon','mon']
    t=list.count('mon')
    print(t)
week_days(list)


# #3#Write a python function named smallest that accepts a list of unsorted integers and returns
# #the smallest number in the list.Example:smallest([3,6,8,2,4,1,5,7]) returns 
def smallest(list):
    print(min(list))
list=[9,8,7,6,2,4,5,1,0]
smallest(list)


# 4.Write a function named divisible_by_seven that;using the range function and a for loop
# #returns a list containing all the numbers between 
# 100 and 200 that are divisible by 7
def divisible_by_seven():
    for x in range(100,200):
        if x % 7== 0:
           print(x)
            
divisible_by_seven()
   
   
#5.Write a python program that takes two inputs(as int) from a user and adds
   # #the 2 numbers,checks if the sum is greater 
   # than 10,less than 10 or equal 10     
  
def numbers(a,b):  
    sum=a+b
    if sum > 10:
        print("sum is greater than 10")
    elif sum <10:
        print("sum is less than 1o")
    else:
        print("sum is equal to 10")
numbers(5,9)   
  
  
#6.Write a function that takes one argument which is a list a=[1,2,3,4,5] and
#returns True if 4 is present in the list and 
# False if 4 is not in the list

def num(list):
    y=[3,5,5,6,7,8,9,12,2,42,33,4,56]
    if 4 in y:
        print("true")
    else:
        print("false")
num(list)

#7.Write a function that takes one argument which is a list
#fruits=["apples","grapes","pineapple"]and removes the last fruit from the list
        
def fruits():
    fruits=['apple','grapes','pineapple','kiwi']
    fruits.remove('kiwi')
    print(fruits)
fruits()
             
#8.#Write a python program that takes in a list of cars,cars=["Ford","BMW","VOLVO"]
#and returns a sorted list
# #then returns the list without the removed fruit
# # #and prints a statement after each check

def vehicles():
    cars=['BMW','Toyota','Subaru','Harrier']
    cars.sort()
    print(cars)
vehicles()