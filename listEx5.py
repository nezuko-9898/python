
#Turn every item of a list into its square
list=[1,2,3,4,5]

res=[]

for x in list:
    res.append(x*x)
print(res)    



list1=[10,20,30,40]
l1=[x*x for x in list1]

print(l1)


#even number added into list3

list2 =[10,2,4,20,13,60]
list3=[]

for x in list2:
    if x % 2 == 0:
        list3.append(x)
list3.sort()        
print(list3)   

#Find Maximum and Minimum

list4=[10,30,1,100]

l1=max(list4)
print("Maximum n in list==>",l1)

l2=min(list4)
print("minimum n of list==>",l2)



# count occurance 

sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']
football_count = sports.count('Football')
print("Count:", football_count)