class MustContainAtSymbolError(Exception):
    """Email does not have @ """
    pass


class NameTooShortError(Exception):
    """ Name less than or equal to 4 characters"""
    pass


class InvalidDomainError(Exception):
    """ the domain is different than .com, .org... """
    pass


MIN_NAME_LEN = 5
VALID_DOMAINS = ("com", "net", "bg", "org")


def validate_email(email):
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split("@")[0]) < MIN_NAME_LEN:
        raise NameTooShortError("Name must be more than 4 characters")

    if email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")


while True:
    email = input()

    if email == "End":
        break
    validate_email(email)
