# original_logger

Initialize a Python logger and apply a function to the output log strings.

# Samples
```Python
import traceback

# applied function
def cat_and_upper(s: str) -> str:
    s = s.upper()
    s = s.replace("CAT", "ฅ^•ω•^ฅ")
    return s

logger = init_logger(__name__, cat_and_upper, "test.log",)

logger.debug("logger debug")
logger.info("logger info")
logger.warning("logger warn")
logger.error("logger error")

try:
    raise("raise!")
except:
    logger.exception("logger exception", exc_info=True)  # applying the function to traceback
    logger.error("except log\n" + traceback.format_exc())  # not applying the function to traceback

logger.info("Concatenate A & B")
```

## Stream Output
```
2023-08-24 23:38:26,126 __main__:63 <module> [INFO]: LOGGER INFO
2023-08-24 23:38:26,126 __main__:64 <module> [WARNING]: LOGGER WARN
2023-08-24 23:38:26,126 __main__:65 <module> [ERROR]: LOGGER ERROR
2023-08-24 23:38:26,126 __main__:70 <module> [ERROR]: LOGGER EXCEPTION
Traceback (most recent call last):
  File "/Users/********/Documents/speed_test/original_logger.py", line 68, in <module>
    raise("raise!")
TypeError: exceptions must derive from BaseException
2023-08-24 23:38:26,126 __main__:71 <module> [ERROR]: EXCEPT LOG
TRACEBACK (MOST RECENT CALL LAST):
  FILE "/USERS/********/DOCUMENTS/SPEED_TEST/ORIGINAL_LOGGER.PY", LINE 68, IN <MODULE>
    RAISE("RAISE!")
TYPEERROR: EXCEPTIONS MUST DERIVE FROM BASEEXCEPTION

2023-08-24 23:38:26,126 __main__:73 <module> [INFO]: CONฅ^•ω•^ฅENATE A & B
```
The "test.log" file is also output.

