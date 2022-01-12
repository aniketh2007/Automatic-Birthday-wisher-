import pandas
import smtplib
from datetime import datetime
import random

my_email = "abc@gmail.com"
password = "Abc707"
# Create a tuple from today's month and day using datetime
today = datetime.now()
today_tuple = (today.month, today.day)

# Use dictionary Comprehension tyo create dictionary from birthday.csv that is format
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"],data_row['day']): data_row
                 for (index, data_row) in data.iterrows()}

# Compare if today's date is birthday or not

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    # Use the replace method to replace the [NAME]
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}"
                            )

