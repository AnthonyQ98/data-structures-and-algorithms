from collections import deque
import string


def is_palindrome(word: string):
    if word == "":
        return False # empty strings not allowed.
    
    if len(word) == 1:
        return True # by default, 1 letter words are palindromic.
    
    queue = deque() # use a double ended queue to pop from either end.

    word = word.lower() # casing shouldn't affect palindrome result... lower case everything.
    for letter in word:
        queue.append(letter) # add each letter into the queue

    while len(queue) > 1: # while the queue has 2 or more characters, keep looping.
        front = queue.popleft() # grab left most letter
        rear = queue.pop() # grab right most letter
        if front != rear: # if the letters dont match, its not a palindrome. 
            return False
        
    # at this point, the word has 1 or 0 letters remaining. In both cases, the word will be a palindrome.    
    return True

def main():
    # Test case:
    print(is_palindrome("rotator"))
    print(is_palindrome("roTatoR"))
    print(is_palindrome("Golang"))
    print(is_palindrome(""))
    print(is_palindrome("a"))
    print(is_palindrome("ab"))

    """
    Space and time complexity of this algorithm is O(n)
    """

if __name__ == "__main__":
    main()