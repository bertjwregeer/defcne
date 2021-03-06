# File: errors.py
# Author: Bert JW Regeer <bertjw@regeer.org>
# Created: 2013-01-05

import logging
log = logging.getLogger(__name__)

from pyramid.security import authenticated_userid
from pyramid.httpexceptions import HTTPForbidden
from pyramid.httpexceptions import HTTPSeeOther

def not_found(context, request):
    request.response.status_int = 404
    log.exception(context)
    return {}

def bad_request(context, request):
    request.response.status_int = 400
    return {}

def forbidden(context, request):
    # do not allow a user to login if they are already logged in
    if authenticated_userid(request):
        request.response.status_int = 403
        return {}

    loc = request.route_url('defcne.user', traverse='auth', _query=(('next', request.path),))
    return HTTPSeeOther(location=loc)
