import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

print("Automatiion Email code is Running :)")

MY_ADDRESS = 'namanmathur3232@gmail.com'
PASSWORD = 'cbhd haqh iynt ucom'

# Function to read contacts from file
def get_contacts(filename):
    names, emails = [], []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for contact in contacts_file:
            parts = contact.split()
            names.append(parts[0])
            emails.append(parts[1])
    return names, emails

# Function to read message template
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        return Template(template_file.read())

# Function to attach a file to email
def attach_file(msg, filename):
    with open(filename, "rb") as file:
        attach = MIMEApplication(file.read(), _subtype=filename.split('.')[-1])
        attach.add_header("Content-Disposition", f"attachment; filename={filename}")
        msg.attach(attach)

def main():
    names, emails = get_contacts('mycontacts.txt')  # Read contacts
    message_template = read_template('message.txt')

    # Set up SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # File to attach (Change this to the actual file path)
    attachment_file = "gate 2024 Qpap.pdf"  # Can be "photo.jpg", "document.docx", etc.

    # Send email to each contact
    for name, email in zip(names, emails):
        msg = MIMEMultipart()
        message = message_template.safe_substitute(PERSON_NAME=name.title())
        
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "This is TEST with Attachment"

        msg.attach(MIMEText(message, 'plain'))  # Attach the message body
        attach_file(msg, attachment_file)  # Attach the file

        s.send_message(msg)
        del msg

    s.quit()

if __name__ == '__main__':
    main()

print("The emails are sent with attachments :)")
