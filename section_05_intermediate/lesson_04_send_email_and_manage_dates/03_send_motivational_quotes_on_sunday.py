import datetime as dt
import smtplib
import random


def get_random_quote():
    quotes_file_path = "03_quotes.txt"

    with open(file=quotes_file_path, mode="r") as quotes_file:
        quote_array = quotes_file.readlines()

    return random.choice(quote_array)


def send_email(quote):
    my_email = "abc@gmail.com"  # Update email
    password = "my_password"  # Update password

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Sunday Morning Motivation\n\n{quote}"
        )


# The day of the week as an integer, where Monday is 0 and Sunday is 6.
curr_day_of_week = dt.datetime.now().weekday()

if curr_day_of_week == 6:
    # Sunday
    send_email(get_random_quote())
