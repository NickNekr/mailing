import smtplib
from email.message import EmailMessage
from email.utils import formataddr

from config import SmtpConfig
from database.models import Mails, session


def main():
    with smtplib.SMTP_SSL(SmtpConfig.HOST) as server:
        server.login(SmtpConfig.USER, SmtpConfig.PASSWORD)
        mails = [Mails(email=email) for email in SmtpConfig.TO]
        session.add_all(mails)
        session.commit()

        msg = EmailMessage()
        msg.set_content(SmtpConfig.TEXT)
        msg["Subject"] = SmtpConfig.SUBJECT
        msg["From"] = formataddr(SmtpConfig.FROM_TUPLE)

        results = server.sendmail(
            SmtpConfig.FROM,
            SmtpConfig.TO,
            msg.as_string(),
            rcpt_options=["NOTIFY=SUCCESS,DELAY,FAILURE"],
        )
        for res in results:
            pass


if __name__ == "__main__":
    main()
