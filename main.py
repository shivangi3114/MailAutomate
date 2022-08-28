from datetime import date  # core python module

import pandas as pd  # pip install pandas


from send_email import send_email  # local python module
import csv


parse_dates = ["date"]
df = pd.read_csv("dataset.csv", parse_dates=parse_dates)
   
#df = pd.read_csv('dataset.csv')
#type(file)

def query_data_and_send_emails(df):
   present_date = date.today()
   email_counter = 0
   for _, row in df.iterrows():
      print("checking... if date matches")
      if (present_date == row["date"]) and (row["available"] == "yes"):
         	#email_counter +=1
         print("connecting to smtp.. ");
         send_email(
                subject=f'[ Minutes(MOM) Reminder] ',
                receiver_email=row["email"],
                name=row["name"],
                date=row["date"].strftime("%d, %b %Y"),  # example: 25, Aug 2022
                
            	);print("Mail Sent");email_counter +=1
   return f"Total Emails Sent on {present_date} : {email_counter}"
result = query_data_and_send_emails(df)
print(result)

