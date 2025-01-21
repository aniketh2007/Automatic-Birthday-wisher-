#Importing all the required libraries
import pandas
import smtplib
import datetime as dt
import random
#Initalizing of variables
user_name = "abc@gmail.com"
password = "xyz"
#Check if today matches a birthday in the birthdays.csv
#Initalizing the tuples and reading the .csv file
now = dt.datetime.now()
today_month = now.month
today_day = now.day
today_tuple = (today_day,today_month)

#Using dictionary comprehension to convert the month and day into the key and the other values to values 
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["day"],data_row["month"] ): data_row for (index,data_row) in data.iterrows() }

#Checking if the dates match if so, then randomly selecting the letter and replacing the default value with the value in the dict
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt","r") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])
        contents= contents.replace("Angela","Abc")
        #Developing the SMTP connection to send the email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=user_name,password=password)
            connection.sendmail(from_addr="abc@gmail.com",
                                to_addrs=birthday_person["email"],
                                msg="Subject: Happy Birthday then after \n\n"
                                    f"{contents}")
        
    