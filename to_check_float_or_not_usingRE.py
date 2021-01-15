import re

pattern = re.compile(r'^[+-]?[0-9]*\.[0-9]+$')
search_list= []

num_of_inp = int(input())
for i in range(num_of_inp): 
    user_inp = str(input())
    search_list.append(user_inp)

for j in range(len(search_list)) :
    match = pattern.search(search_list[j])
    if match :
        print(True)
    else :
        print(False)