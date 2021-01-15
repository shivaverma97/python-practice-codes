word_list = []

def mutate_string(string, position, character):    
        for word in string:
            word_list.append(word)   
        
        word_list.pop(position)
        word_list.insert(position,character)

        btw = ''
        new_string = btw.join(word_list)
        return new_string
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)