from datetime import datetime
from telnetlib import STATUS


def handle_exceptions(excpt):
    status_code = excpt.status_code if hasattr(excpt, "status_code") else 500
    message = excpt.message if hasattr(excpt, "message") else "something went wrong"
    error_response = {
        "message": message,
        "error_type": excpt.__class__.__name__,
        "timestamp": datetime.utcnow(),
        "status_code": status_code,
    }
    return error_response, status_code


class SymbolNotFound(Exception):
    """Currency symbol not found"""

    status_code = 404

    def __init__(self, message):
        self.message = message
