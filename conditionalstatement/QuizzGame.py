print('Welcome to the quiz')
score = 0
print("Question 1: How old is Nivaan?")

print('A. 9 B. 10 C. 4 D. 8')

answer=input('Enter your answer here(A/B/C/D): ')
if answer=='A':
     print ('Correct')
     score = score + 10
else:
     print ('Incorrect')
     score = score -5
print ('Question.2 What is the capital of the UAE') 

print ("A. Sharjah /B. Umm Al Quain /C. Abu Dhabi /D. Dubai")
answer=input('Enter your answer here (A/B/C/D): ')
if answer =='C':
     print ('Correct') 
     score = score +10
else:
     print ('Incorrect')
     score = score -5


print('Question 3: What is capital of India?')

print ("A. Bengaluru B. Mangalore C. New Delhi D. Karnatika ")

answer=input('Enter your answer here (A/B/C/D): ')
if answer =='C':
    print ('Correct')
    score = score +10
else:
     print('Incorrect')
     score = score -5 
# if the person scores more than or equal to 10 we have to display "you won" else he has to display "you lost"

print("your score is : ",score)

if score>=10:
   print('YOU WON!')
else:
     print ('YOU LOST!')
  