# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)

####
#### YOUR CODE HERE 
####
with open("romeo_and_juliet.txt", "r") as file:
    text = file.read()


# Count how many times the word "Juliet" appears

####
#### YOUR CODE HERE 
####
count = text.lower().count("juliet")

print(f"The word 'Juliet' appears {count} times in Romeo and Juliet.")

