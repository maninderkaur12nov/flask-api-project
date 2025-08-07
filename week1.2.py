
# for i in range(5):
#  print(i)
# for i in range(1,6):
#  print(i) 
#  print("square:",i*i)
# # save values in list
# Square=[]
# for i in range(1,11):
#  Square.append(i*i)
# print(Square) 


# # while loop
# count=0
# while count < 5:
#  print("count is: ",count)
#  count+=1
# # Task 2: Odd Countdown using while loop
# count=5
# while count > 0:
#  if count%2!=0:
#   print("countdown for odd:",count)
#  count-=1

# # Remove spaces, convert to lowercase, split words
# text = "  Hello Python Learner  "
# result=text.strip().lower().split()
# print(result)

     
# #  Sum of numbers 1 to N
# n=int(input("enter number")) 
# sum1=0
# mul=1
# for i in range(1,n+1):
#  sum1+=i
#  mul*=i
# print(sum1) 
# #  find factorial

# print("factorial", mul)


# #  Pro Tip: Use sum() with range() (Python shortcut)
# # n=int(input("enter number")) 
# print(sum(range(1,n+1))) 
# # Sum only even numbers from a large range
# n=int(input("enter number")) 
# sum=0
# for i in range(1,n+1):
#  if i%2 == 0:
#   sum+=i
# print(sum)  

# #  2.  Why: Analysts often count "how many records are > 50" or "salary > 100000" Count how many values are above a threshold
# data = [12, 45, 78, 30, 92, 25]
# threshold = 50
# count=0
# # Print those values above threshold, not just the count.  
# list=[]
# for value in data:
#     if value>threshold:
#      count+=1
#      list.append(value)
# print("number of values above threshold: ",count) 
# print(list)
  

# # 3. Clean string data using loop Why: Many datasets have messy whitespace or casing 
# names = ["  Alice  ", "BOB", "ChArLie  "]
# result=[]
# for name in names:
#  result.append(name.strip().title())
# print(result)

# #  4.Split records into two groups: above/below average Why: Analysts often split data into two cohorts
# list=[60,80,55,90,45]
# above=[] 
# low=[]
# average=sum(list)/len(list)
# for value in list:
#     if value< average:
#      low.append(value) 
#     else:
#        above.append(value) 
# print("above average list: ",above, "| low average values:",low)   


# # Replace Missing Values (None) with the Average 
# List=[50,None,70,None,90]
# finallist=[]
# avaiable=[x for x in List if  x is not None]
# for value in List: 
#     if value==None:
#         finallist.append(sum(avaiable)/len(avaiable))
#     else:
#         finallist.append(value)   
     

# print(finallist) 
    


 