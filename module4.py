import random
from hangman_art import logo
from hangman_words import word_list

rn_word=random.choice(word_list)
#Test code
print(f'The word is: {rn_word}')
print(logo)
list=[]
# for data in range(0,len(rn_word)):
#     list+='_'
# # or

for data in rn_word:
    list+='_'
# print(list)
lives=6
strt_of_game=True
while strt_of_game:
 user_data=input('Guess any letter of that word: ').lower() 
 if user_data in list:
    print(f'You have already guessed {user_data}')

 for position in range(len(rn_word)):
    letter=rn_word[position]
    if letter==user_data:
        list[position]=letter

 if '_' not in list:
  strt_of_game=False
  print('You won.')
 print(f'lives={lives}') 
 print(list)
 if user_data not in rn_word:
    lives-=1
    print(f'lives={lives}.{user_data} is not in the word.')
    if lives==0:
        print("You've losed.")

# or

# end_of_game=False
# while not end_of_game:
#  user_data=input('Guess any letter of that word: ').lower()

#  for position in range(len(rn_word)):
#     letter=rn_word[position]
#     if letter==user_data:
#         list[position]=letter
#  if '_' not in list:
#   end_of_game=True
#  print(list)
 