import connexion
import six

from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server import util


def health_check():  # noqa: E501
    """Return status of the API server.

    Return status of the API server. # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'
