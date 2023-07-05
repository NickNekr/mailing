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


class SmtpConfig(MailConfig):
    HOST = "smtp.mail.ru"
    SUBJECT = "Python"
    TO = ["nnnekrasovEdu@yandex.ru"]
    FROM = "Информационный сервис ЕМИАС <nikolay41kg@mail.ru>"
    FROM_TUPLE = ("Информационный сервис ЕМИАС", "nikolay41kg@mail.ru")
    TEXT = "Привет!"


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
