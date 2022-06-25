import random
words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']
  
word = random.choice(words)
joon = 10
char = []
for i in range(len(word)):
    char.append('_')

while joon > 0:
    print(' '.join(char))
        
    if ((''.join(char)) == word):
        print("You win")
        break
    
    user_character = input("please enter your character:").lower()
    
    if (user_character in word):
        print("yes")
        for i in range(len(word)):
            if (word[i] == user_character):
                char[i] = user_character        
                
    else:
        joon = joon - 1
        print("no") 
        if joon==0:
            print("You loss")
            break 