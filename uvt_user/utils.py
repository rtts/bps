from __future__ import unicode_literals

import re
from ldap3 import Server, Connection

class LDAPError(Exception):
    pass

def search_ldap(username):
    '''Searches the Tilburg University LDAP server for the given username and returns a tuple of first name, last name, full name, ANR, emplId and email address. Permission has been granted by TiU's legal department for retrieving this data. Raises LDAPError on any kind of error.'''

    result = ()
    baseDN = "o=Universiteit van Tilburg,c=NL"
    searchFilter = '(uid={})'.format(username)
    attributes = ['givenName', 'sortableSurname', 'cn', 'employeeNumber', 'emplId', 'mail']

    try:
        server = Server('ldaps.uvt.nl', use_ssl=True)
        conn = Connection(server, auto_bind=True)
        conn.search(baseDN, searchFilter, attributes=attributes)
        response = conn.response[0]['attributes']
        for a in attributes:
            if a in response and response[a]:
                if type(response[a]) is list:
                    result += (response[a][0],)
                else:
                    result += (response[a],)
            else:
                result += ('',)
    except IndexError:
        raise LDAPError('Username not found')
    except Exception:
        raise LDAPError('Unknown error in LDAP query')

    return result
