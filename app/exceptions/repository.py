class RepositoryError(Exception):
    pass

class NotFoundError(Exception):
    """Raise an error if get by id failed"""
    pass