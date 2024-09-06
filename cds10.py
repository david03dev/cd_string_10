
def remove_adjacent_duplicates(S):
    # Split the input string into words
    words = S.split()
    
    # Stack to store non-duplicate adjacent words
    stack = []
    
    # Iterate through each word
    for word in words:
        # If stack is not empty and the last word is the same as the current word
        if stack and stack[-1] == word:
            # Remove the last word (which is a duplicate)
            stack.pop()
        else:
            # Otherwise, add the word to the stack
            stack.append(word)
    
    # If the stack is empty, print -1
    if not stack:
        print(-1)
    else:
        # Otherwise, print the remaining words
        print(" ".join(stack))

# Sample Input
S = input()

# Function call to print the result
remove_adjacent_duplicates(S)



"""Joyal was given a sentence. His task is to delete the two words that comes together and print the sentence so that the words in the output sentence have distinct words compared to their adjacent words. If no words are present in the output sentence print -1

Input Description:
You are given input string 'S'

Output Description:
Print the all the words that are left in the string 's' so that the words in the output sentence have distinct words compared to their adjacent words. Print -1 if no words are left

Sample Input :
I am john cena cena john

Sample Output :
I am"""
