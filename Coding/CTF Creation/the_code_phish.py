

#figure out how to hide google colab code
from dataclasses import dataclass
from typing import List
import sys
import base64

# Define a dataclass to act as a struct for phishing information
@dataclass
class PhishingEmail:
    id: int
    email: str
    message: str
    link: str
    mail_server: str
    suspicious: str
    sus_part: str

# Function to add phishing information with custom parameters
def add_phishing_info(phishing_emails: List[PhishingEmail], id, email, message, link, mail_server, suspicious, sus_part):
    phishing_emails.append(
        PhishingEmail(
            id=id,
            email=email,
            message=message,
            link=link,
            mail_server=mail_server,
            suspicious=suspicious,
            sus_part=sus_part
        )
    )

def print_phishing_email(phishing_emails: List[PhishingEmail], index: int):
    if 0 <= index < len(phishing_emails):
        email = phishing_emails[index]
        print(f"Question Number: {email.id}")
        print(f"Email: {email.email}")
        print(f"Message: {email.message}")
        print(f"Link: {email.link}")
        print(f"Mail Server: {email.mail_server}")
        print("---")
    else:
        print("Invalid index")

# Declaration of the phishing email list (array of structs)
phishing_emails = []

print("Greetings user! \nYour task is answering the questions provided by the code and you will need to use the provided sources to\n recognize these social engineering attempts!")
# Adding phishing emails
add_phishing_info(phishing_emails, 1, "NorfolkStateHelpDesk@spartans.nsu.edu", "\nGreetings Jane Doe,\nWe hope this email finds you well. We are writing to inform you that your recent \nsupport request, with the reference number [10982329], is currently under review. ", "N/A", "microsoft", "no", "a")
add_phishing_info(phishing_emails, 2, "Norfolk5tateHelpDesk@spartans.nsu.edu", "\nGreetings,\n You have a hold on your student account and it will prevent you from registering for classes.\nPlease sign into you account so you can take a look at the issue.\n Use the link www.Norfolk5tate.com/studentaccounts", "www.Norfolk5tate.com/studentaccounts", "microsoft", "yes", "a")
add_phishing_info(phishing_emails, 3, "Jenson.Grayson@protonmail.com", "\nHello!\nThis Jenson from work! I just wanted to know if you could take my shift for tomorrow thats all?", "N/A", "proton", "no", "a")
add_phishing_info(phishing_emails, 4, "googlecustomersupport@gmail.com","\nHello there. \nIn a recent huge worldwide data leak google data leak your password showed up amoungst others. Please click this link to reset your password\nwww.googleresetpassword.com" , "www.googleresetpassword.com", "gmail", "yes", "e")
add_phishing_info(phishing_emails, 5, "mike.jones@mitre.org", "\nHello, \nI'm from the help desk sector, some coworker has been going around gathering our passwords and we need to change passwords now.\n Please send me your new and old password before it too late!", "N/A", "mitre.org", "yes", "c")
add_phishing_info(phishing_emails, 6 ,"mrrobot@protonmail.com", "\nHi,\nIve obtained your banking information. To get your information back, send 500 dollars in bitcoin to my cashapp and all is well.","N/A", "zoom","yes","b")
add_phishing_info(phishing_emails, 7,"security@paaypal.com", "\nDear Customer,\nWe noticed suspicious activity on your account. For your security, please confirm your information by clicking the link below.\nwww.paaypal.com/securitycheck","www.paaypal.com/securitycheck", "paypal", "yes", "a")
add_phishing_info(phishing_emails, 8,"sarah.b@friendsmail.com", "\nHey!\nI saw this hilarious video and thought of you! You have to check it out when you get a chance. Here’s the link: www.friendsmail-videos.com\n\nTalk soon!", "www.friendsmail-videos.com","friendsmail","yes", "d")
add_phishing_info(phishing_emails, 9,"team@jobportal.com", "\nHello,\nThank you for using JobPortal! We wanted to remind you to update your profile to ensure you don’t miss out on potential job matches. You can log in at your convenience on our website.\n\nBest regards,\nThe JobPortal Team", "N/A", "jobportal", "no", "a")
add_phishing_info(phishing_emails, 10, "support@streamingfriends.com", "\nHi there!\nWe noticed you've been watching a lot of thrillers recently! Here’s a list of recommendations tailored just for you. Check them out here: www.streamingfriends-recs.com\n\nHappy Watching!", "www.streamingfriends-recs.com", "streamingfriends", "yes","d")


for i, email in enumerate(phishing_emails):
    while True:
        print_phishing_email(phishing_emails, i)
        print("Does this email have anything suspicious? \nType 'yes' or 'no'")
        
        user_answer = input().lower()
        other_user_answer = None
        
        if user_answer == email.suspicious:
            print("Correct!\n")
            if(user_answer == "yes"):
                print("What social engineering principle is used (just type the letter)?\nA)Typosquatting\nB)Intimidation\nC)Urgency\nD)Familiarity\nE)Hoax")
                other_user_answer = input().lower()

                
                if other_user_answer == email.sus_part:
                    print("Correct!\n")
                    break  # Exit the loop to move to the next email
                else:
                    print("Nope, try again.\n")
                    sys.exit()

            break  # Exit the loop to move to the next email
        else:
            print("Nope, try again.\n")
            sys.exit()


#spell check
print("Answer Key")
print("Q2: A \nThis is typosquatting because the social engineer put a 5 instead of an S to trick the recipient due to the characters looking similar.\n")
print("Q4: E \nThis is a hoax because Google hasn't had a data leak in recent history.\n")
print("Q5: C \nThis is using urgency because the social engineer is trying to get the recipient to act fast!\n")
print("Q6: B \nThis is intimidation because they are scaring the recipient into believing that their banking information has been compromised.\n")
print("Q7: A \nThis is typosquatting because the social engineer's email name spells 'Paypal' incorrectly, which is an easy mistake to miss.\n")
print("Q8: D \nThis is familiarity because Sarah B is pretending that they know the recipient.\n")
print("Q10: D \nThis is familiarity because the fake movie platform is presenting that the recipient has an account with them.\n")

print("The Flag: ;-)")
print("ictf{bigPHISHinAlittlePOND}")