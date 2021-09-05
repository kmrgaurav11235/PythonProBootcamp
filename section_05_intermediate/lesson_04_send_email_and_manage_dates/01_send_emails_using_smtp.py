import smtplib

my_email = "abc@gmail.com"  # Update sender email
password = "my_password"  # Update sender password

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="xyz@gmail.com",  # Update receiver email
        msg="Subject:Hello\n\nThis is the body of my email."
    )
