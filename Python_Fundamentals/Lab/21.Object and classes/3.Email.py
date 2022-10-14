"""
input1
Peter John Hi,John
John Peter Hi,Peter!
Katy Lilly Hello,Lilly
Stop
0, 2

output1
Peter says to John: Hi,John. Sent: True
John says to Peter: Hi,Peter!. Sent: False
Katy says to Lilly: Hello,Lilly. Sent: True

input2
Anna, Bella, Hi
Sam, Dany, Okey
Felix, Mery, Bye
Stop
0

output2
Anna, says to Bella,: Hi. Sent: True
Sam, says to Dany,: Okey. Sent: False
Felix, says to Mery,: Bye. Sent: False

"""

class Email:

    def __init__(self, sender,receiver,content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"

emails = []

while True:
    command = input().split(' ')

    if command[0] == "Stop":
        break

    sender = command[0]
    receiver = command[1]
    content = command[2]
    email = Email(sender, receiver ,content)
    emails.append(email)

send_email = [emails[int(x)].send() for x in input().split(', ')]

for email in emails:
    print(email.get_info())





