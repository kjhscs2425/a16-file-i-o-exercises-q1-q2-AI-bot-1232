# Read and print the contents of the file "q1.txt"

####
#### YOUR CODE HERE 
####
with open("q1.txt", "r") as file:
    contents = file.read()
    print(contents)