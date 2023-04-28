"""
input1
abc@abv.bg

output1
Traceback (most recent call last):
  File ".\email_validator.py", line 20, in <module>
    raise NameTooShort("Name must be more than 4 characters")
__main__.NameTooShort: Name must be more than 4 characters

input2
peter@gmail.com
petergmail.com

output2
Email is valid
Traceback (most recent call last):
  File ".\email_validator.py", line 18, in <module>
    raise MustContainAtSymbolError("Email must contain @")
__main__.MustContainAtSymbolError: Email must contain @

input3
peter@gmail.hotmail

output3
Traceback (most recent call last):
  File ".\email_validator.py", line 22, in <module>
    raise InvalidDomainError("Domain must be one of the folowing: .com, .bg, .org, .net")
__main__.InvalidDomainError: Domain must be one of the folowing: .com, .bg, .org, .net

"""

from custom_exceptions import MustContainAtSymbolError, NameTooShortError, InvalidDomainError

valid_domains = {'.com', '.bg', '.org', '.net'}

while True:
    line = input()
    if line == 'End':
        break
    email = line

    emails_parts = email.split('@')

    if len(emails_parts) != 2:
        raise MustContainAtSymbolError('Email must contain @"')

    name, domain_name = emails_parts

    if len(name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    # gmail.com -> ['gmail', 'com'] -> 'com'
    domain = f".{domain_name.split('.')[-1]}"

    if domain not in valid_domains:
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join(valid_domains)}')

    print('Email is valid')
