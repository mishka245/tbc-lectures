# example how is possible to send simple email from python script
# lets use sendgrid
import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

API_KEY = os.getenv('SENDGRID_API_KEY')

message = Mail(
    from_email='mikheil@maxinai.com',
    to_emails='lomidzemikheili@gmail.com',
    subject='Hello from TBC academy',
    html_content='ჩვენ ვართ საქართველო!<br> <br> <br><br><br><br><br>კეთილი სურვილებით, ქართველი ხალხი!')
try:
    # sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    sg = SendGridAPIClient(API_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
except Exception as e:
    print(e.message)
