import smtplib
from config import SmptConfig
from database.models import Mails, session


def main():
    with smtplib.SMTP_SSL(SmptConfig.HOST) as server:
        server.login(SmptConfig.USER, SmptConfig.PASSWORD)
        mails = [Mails(email=email) for email in SmptConfig.TO]
        session.add_all(mails)
        session.commit()
        results = server.sendmail(
            SmptConfig.FROM,
            SmptConfig.TO,
            SmptConfig.BODY,
            rcpt_options=["NOTIFY=SUCCESS,DELAY,FAILURE"],
        )
        for res in results:
            pass


if __name__ == "__main__":
    main()
