#Will Agble
#This is a program that takes the input of an integer from a user and
#prints a phrase that repeats a word based on the number input by the user

# include the sys module in this program
import sys

# read the input from the command line
timesFar = int(sys.argv[1])

#Set initial values of string variables
beginning = "A long time ago in a galaxy "
far ="far "
end = "away..."
#calculate the number of times to print far
count = timesFar
temp = ""
while (count > 0):
    count = count - 1
    temp = temp + far
#display

print(beginning + temp + end)
