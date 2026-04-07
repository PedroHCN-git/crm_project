class RepositoryException(Exception):
    pass

class NotFoundException(Exception):
    """Raise an error if get by id failed"""
    pass

class DuplicatedUserException(RepositoryException):
    """Raise duplicated user insert in table"""
    pass