class ServiceException(Exception):
    """Base class for services exeptions"""
    pass

class UserNotFoundException(ServiceException):
    """Rais an error if user is not found"""
    pass