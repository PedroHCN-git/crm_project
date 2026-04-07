from functools import wraps
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR)
logger = logging.getLogger(__name__)


def handle_exceptions():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(
                    "Error in function",
                    extra={
                        "function": func.__name__,
                        "error_type": type(e).__name__,
                        "error_message": str(getattr(e, "orig", e)),
                    },
                    exc_info=True
                )
                raise
        return wrapper
    return decorator


