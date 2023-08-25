from logging import getLogger, LogRecord, Logger, Formatter, StreamHandler, FileHandler, DEBUG, INFO
from typing import Optional


class OriginalFormatter(Formatter):
    def __init__(self, func, *args, **kwargs) -> None:
        self.func = func
        super().__init__(*args, **kwargs)

    def format(self, record: LogRecord) -> str:
        record.message = self.func(record.getMessage())
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)
        s = self.formatMessage(record)

        if record.exc_info:
            # Cache the traceback text to avoid converting it multiple times
            # (it's constant anyway)
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            if s[-1:] != "\n":
                s = s + "\n"
            s = s + record.exc_text
        if record.stack_info:
            if s[-1:] != "\n":
                s = s + "\n"
            s = s + self.formatStack(record.stack_info)
        return s


def init_logger(name: Optional[str], func: object, filename: Optional[str]) -> Logger:
    logger = getLogger(name)
    logger.setLevel(DEBUG)
    log_format = OriginalFormatter(
        func, "%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s")

    st = StreamHandler()
    st.setFormatter(log_format)
    st.setLevel(INFO)
    logger.addHandler(st)

    if filename is not None:
        fl = FileHandler(filename)
        fl.setFormatter(log_format)
        fl.setLevel(DEBUG)
        logger.addHandler(fl)

    return logger
