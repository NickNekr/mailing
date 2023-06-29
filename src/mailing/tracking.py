import imaplib
import sys
from config import ImapConfig
import email
from database.models import Mails, session


def imap_connect():
    imap = imaplib.IMAP4_SSL(ImapConfig.HOST)
    imap.login(ImapConfig.USER, ImapConfig.PASSWORD)
    return imap


def change_status(failed_email, status: bool):
    mail: Mails = session.query(Mails).filter(Mails.email == failed_email).first()
    if not mail:
        return
    mail.sent = status
    session.commit()


def check_mails(imap, unseen_msg):
    for mail_num in unseen_msg:
        res, msg = imap.fetch(mail_num, "(RFC822)")
        msg = email.message_from_bytes(msg[0][1])
        if msg["From"] == ImapConfig.TARGET_DAEMON:
            failed_email = msg["X-Failed-Recipients"]
            if failed_email:
                change_status(failed_email, False)
            else:
                success_email = (
                    msg.get_payload()[1]
                    .get_payload()[1]["Final-Recipient"]
                    .split(";")[1]
                )
                change_status(success_email, True)
    imap.close()
    imap.logout()


def get_mails(imap):
    imap.select()
    status, msg = imap.search(None, "UNSEEN")
    assert status == "OK", print("Status:", status, file=sys.stderr)
    unseen_msg = msg[0].split()[::-1]
    check_mails(imap, unseen_msg)


def main():
    imap = imap_connect()
    get_mails(imap)


if __name__ == "__main__":
    main()
