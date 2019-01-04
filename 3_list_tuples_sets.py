# Lists
grades = [ 77 , 80 , 95 , 100 , 10]

print("Current Grade:")
print(grades)

grades.append(102) # adds item to the end

print("Grade After Appened:")
print(grades)

# tuple , fixed ammount of storage , non mutable , unchangable
tuple_grades = (77 , 77 , 80 , 95 , 100 , 101 , 102) 

# unique and unordered
set_grades = { 77 , 80 , 80 , 100, 98}
print(sum(grades)/len(grades))