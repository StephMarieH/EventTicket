"""
Create a programme where users apply for a free ticket for an event.
The user needs to input some personal information to receive the ticket.
Do input validation and exception handling for each user input submitted.

"""

LINE = "-" * 79
heading = "Application for a Free Ticket to our Event!"

print(f"{LINE}\n{heading}\n{LINE}")

# Enter first name
user_name = input("Enter your first name: ")
user_name = user_name.lower()


# Enter surname
user_surname = input("Enter your surname: ")
user_surname = user_surname.lower()


# Enter email address

user_email = input("Enter your email address: ")  
if "@" in user_email and "." in user_email:
    user_email = user_email    
else:
    print("Error")

# Enter mobile number
user_mob_num = input("Enter a UK mobile number (starting in 07 and without spaces): ")
if len(user_mob_num) == 11 and user_mob_num.isdigit() and "07" in user_mob_num:
    print(user_mob_num)
else:
    print("ERROR: Please enter a valid UK mobile number: ")

# Enter age (applicant must be over 18)
user_age = input("Enter your age: ")
user_age = int(user_age)
if user_age >= 18:
# Thank user for registering, their ticket will be emailed 24hrs before event.
    print("Thankyou for registering, your ticket will be emailed to you 24hrs before the event starts.")
else:
    print("Sorry you have to be 18 or over to attend this event.")
    