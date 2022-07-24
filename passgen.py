#!/usr/bin/python3

#Importing important modules
import argparse
import secrets
import string
import random
import textwrap

#Creating Argument Parser
parser = argparse.ArgumentParser(description= "Password Generator",
        formatter_class = argparse.RawDescriptionHelpFormatter,
        epilog = textwrap.dedent(""" Example:
        ./passgen.py -t 8 
        ./passgen.py -n 8 
        ./passgen.py -n 8 -l 3
        ./passgen.py -n 8 -l 4 -u 4
        ./passgen.py -n 9 -l 4 -u 4 -s 1
        ./passgen.py -n 9 -l 4 -u 4 -s 1 -a 10
        ./passgen.py -n 9 -l 4 -u 4 -s 1 -a 10 -o Generated_passwords.txt
        """))

#Adding argument to the parser
parser.add_argument("-t", "--total-length", type=int, default=0, help="Total length of the password (generate random password: ignores other options)")
parser.add_argument("-n", "--numbers", type=int, default=0, help="Password length")        
parser.add_argument("-l", "--lowercase", type=int, default=0, help="Total number of lowercase letter")
parser.add_argument("-u", "--uppercase", type=int, default=0, help="Total number of uppercase letter")
parser.add_argument("-s", "--special-char", type=int, default=0, help="Total number of special character")
parser.add_argument("-a", "--amount", type=int, default=1, help="Total number (amount) of passwords")
parser.add_argument("-o", "--output-file", help="Save password in file")

#Parsing the command line argument
args = parser.parse_args()

#Password list
passwords = []

#Concatinating alphabets, numbers and specail characters
all_char = string.ascii_letters + string.digits + string.punctuation

#Generating total number of password 
for a in range(args.amount):
    
    #Checking if the total length '-t' is provided, generating random password if present
    if args.total_length:
        passwords.append("".join((secrets.choice(all_char) for t in range(args.total_length))))        
    
    else:
        password = []

        #Total digits (numbers) password should contain
        for n in range(args.numbers):
            password.append(secrets.choice(string.digits))

        #Total number of lowercase password should contain
        for l in range(args.lowercase):
            password.append(secrets.choice(string.ascii_lowercase))

        #Total number of uppercase password should contain
        for u in range(args.uppercase):
            password.append(secrets.choice(string.ascii_uppercase))

        #Total number of special characters
        for s in range(args.special_char):
            password.append(secrets.choice(string.punctuation))

        #Shuffle the list
        random.shuffle(password)

        #Changing list to normal string
        password = "".join(password)

        #Appending password to the list
        passwords.append(password)

#Saving generated password in a file
if args.output_file:
    with open(args.output_file, "w") as f:
        f.write("\n".join(passwords))

else:
    #Printing out the passwords
    print("\n".join(passwords))
