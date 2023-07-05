from celery import Celery

app = Celery("hello", broker="redis://localhost:6379/0", include=["src.celdery.tasks"])

if __name__ == "__main__":
    app.start()
