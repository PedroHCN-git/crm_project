class DomainException(Exception):
    """Base class for domain exceptions"""
    pass

class PasswordNotValidException(DomainException):
    """Raise a password not valid error"""
    pass

class EmailNotValidException(DomainException):
    """Raise a email not valid exception"""
    pass

class UserBlockedException(DomainException):
    """Raise a user blocked exception"""
    pass