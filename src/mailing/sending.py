import smtplib
from config import SmptConfig


def main():
    with smtplib.SMTP_SSL(SmptConfig.HOST) as server:
        server.login(SmptConfig.USER, SmptConfig.PASSWORD)
        server.ehlo()
        results = server.sendmail(
            SmptConfig.FROM,
            SmptConfig.TO,
            SmptConfig.BODY,
            rcpt_options=["NOTIFY=SUCCESS,DELAY"],
        )
        for res in results:
            pass


if __name__ == "__main__":
    main()
