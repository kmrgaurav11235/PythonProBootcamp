import pandas
import random
import smtplib
import datetime as dt

BIRTHDAYS_CSV_FILE_PATH = "birthdays.csv"
NAME_PLACEHOLDER = "[NAME]"


def is_today(month, day):
    """Check if today matches the provided month and date"""
    today = dt.datetime.today()
    return (month == today.month) and (day == today.day)


def get_letter_body(name):
    """Pick a random letter from letter templates and replace the [NAME] with the provided name"""
    file_index = random.randint(1, 3)
    chosen_letter_path = random.choice(f"04_letter_templates/letter_{file_index}.txt")
    with open(file=chosen_letter_path, mode="r") as letter_file:
        letter_text = letter_file.read()
    return letter_text.replace(NAME_PLACEHOLDER, name)


def send_email(email_address, email_body):
    """Send email to the provided email_address with the provided email_body"""
    my_email = "my_email@gmail.com"  # Update email
    password = "my_password"  # Update password

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email_address,
            msg=f"Subject:Happy Birthday!\n\n{email_body}"
        )


birthday_data_frame = pandas.read_csv(filepath_or_buffer=BIRTHDAYS_CSV_FILE_PATH)

for _, data in birthday_data_frame.iterrows():
    if is_today(data["month"], data["day"]):
        letter_body = get_letter_body(data["name"])
        # print(data["email"], letter_body)
        send_email(data["email"], letter_body)

