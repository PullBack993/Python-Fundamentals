class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
line = input()
while line != "Stop":
    tokens = line.split(" ")
    email = Email(tokens[0], tokens[1], tokens[2])
    emails.append(email)
    line = input()

send_emails = [int(x) for x in input().split(", ")]
for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())
# TODO: print the emails
