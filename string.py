#------string---------
str = "thsi is string 'brother' "
str = 'thsi is string "brother"'

str = 'Plan Your destination'
print(str[0], str[-1]) #P n
print(str[0:4])  #Plan
print(str[5:9]) #Your

#string multiline
str = ''' 
 this is  multiline
 string
 you  can use as you want
'''

str1 = "Train Your Mind"

print(str1[:5])
print(str1[5:])

print(str1[1:-1]) #rain Your Min
print(str1[:10])  #Train Your

print(str1[0:]) #Train Your Mind
print(str1[:]) #Train Your Mind

#Formated string
first_name ="kanon"
last_name ="chakma"

full_name = f'{first_name} {last_name}'
print(full_name)


course = "This is for beginner"
print(course.upper())
print(course.lower())
print(len(course))

#find return  index
print(course.find('T'))
print(course.find('beginner'))

#in return boolean
print('for' in course)
print('Is' in course)

#replace
print(course.replace('i', 'o'))
print(course.replace('beginner', 'absolute beginner'))
