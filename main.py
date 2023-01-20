#CyHelp Code
#integer
cyberBirthYear = 1970

#Greets user
print("Hello! I'm CyHelp.")
#string
userName = input("What is your name?\n")
print("\nHello " + userName + ". It's nice to meet you.")

#Recounts start of Cybersecurity
todaysYear = input("What is the year right now?\n")
print("\nWow, it's " + todaysYear + ".")
#integer = string - integer
#data type cast to integer
passedYears = int(todaysYear) - cyberBirthYear
#data type cast to string
print("That means it's been " + str(passedYears) +
      " since Cybsecurity has been around.")

print(
    "The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!"
)

#enter - new line
# "\n" = escape character - adds new line
input("Please press enter to continue.\n")

#Describes Cybersecurity
print(
    "Cybsecurity refers to the practices that people use to protect computer systems and networks from digital threats."
)
print(
    "These people can be government nations, companies, community origanizations, and people.\n"
)

#Introduces CIA Triad
print(
    "The CIA Triad is the model used to discuss cybersecurity. CIA stands for confidentiality, integrity, availiability."
)
print("Would you like to learn about the CIA Triad?")
giveInfo = input("Type 'yes' or 'no': \n")

#Explains pillars of CIA Triad
#everything in while loop - repeats as long boolean true
while giveInfo.lower() == "yes":
    print(
        "What would you like to learn more about? Enter the     lowercase letter of the following options: \n (a) confidentiality, (b) integrity, (c) availiability, or (d) none of the above"
    )
    topic = input()
    #conditionals

    #.lower method
    if topic.lower() == 'a':
        print("\nConfidentiality makes sure data is private.")
    elif topic.lower() == 'b':
        print(
            "\nIntegrity makes sure data has not been tampered with and can be trusted."
        )
    elif topic.lower() == 'c':
        print("\nAvailiability makes authorized people can access the data.")
    elif topic.lower() == 'd':
        break
    else:
        print(
            "\nMy bad. I didn't catch that. Please choose one of the options listed."
        )

        #new line
    print("\n")
    #Chatbot ends conversation
print("\nThanks for chatting with me, and I hope you learned something new!")

#notes: indent everything inside while loop
#2 ways to stop loop: 1)boolean isn't true, 2)break
