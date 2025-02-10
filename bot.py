from telethon.sync import TelegramClient
"""
Instructions:

Create a new python project(mybot for example)

Copy-paste all this code into the python file

Go in cmd to the folder where the project is located

You have to install the package telethon.sync with(copy paste this command in cmd): pip install telethon.sync

Then use the following command in cmd(change mybot with the name of your py file): python mybot.py
 
To get your Telegram API ID and API hash, follow these steps:

Create a Telegram Application:

Go to Telegram's website (https://my.telegram.org/) and log in with your phone number.
Once logged in, go to the API development tools (https://my.telegram.org/apps)
Create a new application and fill in the required information (name, description, etc. just use random words doesn't really matter).

Retrieve API ID and Hash:

After creating the application, you should see your app details with an API hash and API ID.
These are the values you'll use in cmd. The API ID is a number, and the API hash is a string.

"""
api_id =input('API id:')
api_hash = input('API hash:')
phone_number = input('Phone number(with country code too(ex):+90....):')
group_name=input('Group name(t.me/groupname):')
client = TelegramClient('session_name', api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code(in the telegram app you should get a code): '))

participants = client.get_participants(group_name)

phone_numbers = []
usernames = []

for participant in participants:
    if participant.phone:
        phone_numbers.append(participant.phone)
    if participant.username:
        usernames.append(participant.username)
while True:
    choose = input("Choose 1 (Phone numbers only), 2 (User + Phone number), 3 for both(separate files), 4(usernames): ")

    if choose == '1':
        with open('phone.txt', 'w') as file:
            for number in phone_numbers:
                file.write("+" + number + '\n')
        break

    elif choose == '2':
        with open('user&phone.txt', 'w') as file:
            for index, number in enumerate(phone_numbers):
                file.write(usernames[index] + ": +" + number + '\n')
        break
    elif choose == '3':
        with open('phone.txt', 'w') as file:
            for number in phone_numbers:
                file.write("+" + number + '\n')
        with open('user&phone.txt', 'w') as file:
            for index, number in enumerate(phone_numbers):
                file.write(usernames[index] + ": +" + number + '\n')
        break
    elif choose == '4':
        with open('users.txt', 'w') as file:
            for index, number in enumerate(usernames):
                file.write(usernames[index]+'\n')
        break
    else:
        print("Only 1, 2 and 3 are the available options. Choose again.")