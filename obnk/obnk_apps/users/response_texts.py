# Django
from django.utils.translation import ugettext as _

# Python
import logging
logger = logging.getLogger(__name__)

USER_NOT_EXISTS = "USER_NOT_EXISTS"
LOGIN_ERROR = "LOGIN_ERROR"
PASSWORD_REQUIRED = "PASSWORD_REQUIRED"
WRONG_UUID = "WRONG_UUID"

RESPONSE_TEXTS = {
    USER_NOT_EXISTS: {"userError": [_("The user does not exists")]},
    LOGIN_ERROR: {"userError": [_("Unable to login with provided "
                                  "credentials")]},
    PASSWORD_REQUIRED: {"userError": [_("The password must be provided")]},
    WRONG_UUID: {"hiddenError": [_("Wrong user uuid")]},
}


def get_response_text(response_key):
    response_text = RESPONSE_TEXTS.get(response_key)
    print(response_text)
    if not response_text:
        logger.warning("Response text key without text. Key {0}".format(
                       response_key))
        return response_text
    if "hiddenError" in response_text:
        logger.warning(response_text)
    return response_text
