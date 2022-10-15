import os
from dotenv import dotenv_values

config = {
    **dotenv_values(".secret.env"),  # load shared development variables
    **dotenv_values(".shared.env"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}