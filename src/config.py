import os
from dotenv import load_dotenv

assert load_dotenv(
    ".env"
), """Can't load the environment:(
                                        Set in .env file: 
                                        if DB env:
                                            DB_USER=
                                            DB_PASSWORD=
                                            DB_NAME=
                                            DB_HOST=
                                            DB_PORT=
                                            DB_TIMEZONE= (for example: Europe/Moscow)
                                            
                                            MAIL_PASSWORD=
                                        """


class Config:
    pass


class MailConfig(Config):
    PASSWORD = os.environ.get("MAIL_PASSWORD")
    USER = "nikolay41kg@mail.ru"


class SmptConfig(MailConfig):
    HOST = "stmp.mail.ru"
    SUBJECT = "Python"
    TO = ["nnnekrasovasdeadsdau@yandex.ru"]
    FROM = "nikolay41kg@mail.ru"
    TEXT = "Hello from python!"

    BODY = "\r\n".join(("From: %s" % FROM, "Subject: %s" % SUBJECT, "", TEXT))


class ImapConfig(MailConfig):
    HOST = "imap.mail.ru"
    TARGET_DAEMON = "mailer-daemon@corp.mail.ru"


class ConfigDB(Config):
    PASSWORD = os.environ.get("DB_PASSWORD")
    HOST = os.environ.get("DB_HOST")
    DB = os.environ.get("DB_NAME")
    USERNAME = os.environ.get("DB_USER")
    PORT = os.environ.get("DB_PORT")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}"
