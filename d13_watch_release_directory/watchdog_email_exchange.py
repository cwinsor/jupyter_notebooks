## reference   https://stackoverflow.com/questions/288546/connect-to-exchange-mailbox-with-python

from exchangelib import DELEGATE, Account, Credentials

credentials = Credentials(
    username='rapidmicrobio\\cwinsor',  # Or myusername@example.com for O365
    password='SafoMs2016'
)
account = Account(
    primary_smtp_address='cwinsor@rapidmicrobio.com', 
    credentials=credentials, 
    autodiscover=True, 
    access_type=DELEGATE
)
# Print first 5 inbox messages in reverse order
for item in account.inbox.all().order_by('-datetime_received')[:5]:
    print(item.subject, item.body, item.attachments)