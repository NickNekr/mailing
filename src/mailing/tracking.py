import imaplib
import sys
from config import ImapConfig
import email


def imap_connect():
    imap = imaplib.IMAP4_SSL(ImapConfig.HOST)
    imap.login(ImapConfig.USER, ImapConfig.PASSWORD)
    return imap


def get_mails(imap):
    imap.select()
    status, msg = imap.search(None, "UNSEEN")
    assert status == "OK", print("Status:", status, file=sys.stderr)
    unseen_msg = msg[0].split()[::-1]
    for mail_num in unseen_msg:
        res, msg = imap.fetch(mail_num, "(RFC822)")
        msg = email.message_from_bytes(msg[0][1])
        if msg["From"] == ImapConfig.TARGET_DAEMON:
            pass


if __name__ == "__main__":
    imap = imap_connect()
    get_mails(imap)
