from __future__ import unicode_literals

import re
from ldap3 import Server, Connection

class LDAPError(Exception):
    pass

def search_ldap(username):
    '''Searches the Tilburg University LDAP server for the given username and returns a tuple of first name, full name, ANR and email address. Permission has been granted by TiU's legal department for retrieving this data. Raises LDAPError on any kind of error.'''

    result = ()
    baseDN = "o=Universiteit van Tilburg,c=NL"
    searchFilter = '(uid={})'.format(username)
    attributes = ['givenName', 'cn', 'employeeNumber', 'mail']

    try:
        server = Server('ldaps.uvt.nl', use_ssl=True)
        conn = Connection(server, auto_bind=True)
        conn.search(baseDN, searchFilter, attributes=attributes)
        response = conn.response[0]['attributes']
        for a in attributes:
            if a in response:
                result += (response[a][0],)
            else:
                result += ('',)
    except Exception:
        raise LDAPError('Error in LDAP query')

    return result

def strip_initials(full_name):
    '''Removes leading capitals, periods, and spaces (initials) from strings, then moves any uncapitalized words (tussenvoegsels) to the rear.'''

    last_name = re.sub(r'[A-Z\. ]+\. ', '', full_name)
    last_name_reversed = re.sub(r'^([a-z ]*)(.*)', r'\2, \1', last_name)
    last_name_without_trailing_comma = last_name_reversed.rstrip(', ') # I miss Perl
    return last_name_without_trailing_comma
