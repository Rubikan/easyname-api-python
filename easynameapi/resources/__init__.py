from easynameapi.resources.contact import Contact
from easynameapi.resources.domain import Domain
from easynameapi.resources.user import User

class Resources(Contact, Domain, User):
    """
    This object is used to deliver all operations to EasynameClient.
    The operations are seperated by resource into submodules with a single class.
    """
    pass