import pathlib


_basedir = pathlib.Path(__file__).parents[1]

SQLALCHEMY_DATABASE_URI = (
    'sqlite:///' + str(_basedir.joinpath(pathlib.PurePath('app.db')).resolve())
)
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'INSECURE'

MAIL_SERVER = 'localhost'
MAIL_PORT = '25'
MAIL_DEFAULT_SENDER = 'no-reply@localhost.localdomain'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": '%(asctime)s %(levelname)s: %(message)s '
                      '[in %(pathname)s:%(lineno)d]'
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "formatter": "verbose",
            "class": "iis.log.LockingFileHandler",
            "filename": "/home/max/Projects/iis/iis.log"
        },
    },
    "loggers": {
        "iis": {
            "level": "DEBUG",
            "handlers": ["file"]
        },
    }
}
LOGGER_NAME = "iis"
