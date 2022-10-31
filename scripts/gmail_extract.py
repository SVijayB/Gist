import imaplib
import os
import email
import sys
import json
class GMAIL_EXTRACTOR():
    def helloWorld(self):
        print("\nWelcome to Gist,\n Gmail_Extractor")

    def initializeVariables(self):
        self.usr = ""
        self.pwd = ""
        self.mail = object
        self.mailbox = ""
        self.mailCount = 0
        self.destFolder = ""
        self.data = []
        self.ids = []
        self.idsList = []

    def getLogin(self):
    	print("\nPlease enter your Gmail login details below.")
    	self.usr = input("Email: ")
    	self.pwd = input("Password: ")

    def attemptLogin(self):
    	self.mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    	if self.mail.login(self.usr, self.pwd):
        	print("\nLOGIN SUCCESSFUL")
        	self.destFolder = input("\nPlease choose a destination folder in the form of /Users/username/dest/ : ")
        	if not self.destFolder.endswith("/"): self.destFolder+="/"
        	return True
    	else:
        	print("\nLogIn FAILED")
        	return False

    def selectMailbox(self):
    	self.mailbox = input("\nPlease type the name of the mailbox you want to extract, e.g. Inbox: ")
    	bin_count = self.mail.select(self.mailbox)[1]
    	self.mailCount = int(bin_count[0].decode("utf-8"))
    	return True if self.mailCount > 0 else False

    def searchThroughMailbox(self):
    	type, self.data = self.mail.search(None, "ALL")
    	self.ids = self.data[0]
    	self.idsList = self.ids.split()

    def checkIfUsersWantsToContinue(self):
    	print("\nWe have found "+str(self.mailCount)+" emails in the mailbox "+self.mailbox+".")
    	return True if input("Do you wish to continue extracting the recent 10 emails into "+self.destFolder+"? (Y/N) ").lower().strip()[:1] == "y" else False

    def parseEmails(self):
    	output=[]
    	mails=self.data[0].split()[-10:]
    	index=0
    	for anEmail in mails:
        	type, self.data = self.mail.fetch(anEmail, '(UID RFC822)')
        	raw = self.data[0][1]
        	raw_str = raw.decode("utf-8")
        	msg = email.message_from_string(raw_str)
	        raw = self.data[0][0]
	        raw_str = raw.decode("utf-8")
	        uid = raw_str.split()[2]
	        index+=1
	        jsonOutput = {}
	        jsonOutput['id']= index
	        jsonOutput['subject'] = msg['subject']
        	jsonOutput['from'] = msg['from']
        	jsonOutput['date'] = msg['date']
	        # Body #
	        if msg.is_multipart():
	            for part in msg.walk():
	                partType = part.get_content_type()
	                ## Get Body ##
	                if partType == "text/plain" and "attachment" not in part:
	                    jsonOutput['body'] = part.get_payload()
	                ## Get Attachments ##
	                if part.get('Content-Disposition') is None:
	                    attchName = part.get_filename()
	                    if bool(attchName):
	                        attchFilePath = str(self.destFolder)+str(uid)+str("/")+str(attchName)
	                        os.makedirs(os.path.dirname(attchFilePath), exist_ok=True)
	                        with open(attchFilePath, "wb") as f:
	                        	f.write(part.get_payload(decode=True))
	        else:
	            jsonOutput['body'] = msg.get_payload(decode=True).decode("utf-8") # Non-multipart email, perhaps no attachments or just text.
	        output.append(jsonOutput)
    	outputDump = json.dumps(output)
    	emailInfoFilePath = str(self.destFolder)+str(self.usr)+str(".json")
    	os.makedirs(os.path.dirname(emailInfoFilePath), exist_ok=True)
    	with open(emailInfoFilePath, "w") as f:
    		f.write(outputDump)

    def __init__(self):
	    self.initializeVariables()
	    self.helloWorld()
	    self.getLogin()
	    if self.attemptLogin():
	        not self.selectMailbox() and sys.exit()
	    else:
	        sys.exit()
	    not self.checkIfUsersWantsToContinue() and sys.exit()
	    self.searchThroughMailbox()
	    self.parseEmails()


if __name__ == "__main__":
    run = GMAIL_EXTRACTOR()
