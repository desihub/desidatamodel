# License information goes here
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
# The line above will help with 2to3 support.
def get_uri(element):
    """Return the uri portion of an element tag.

    Parameters
    ----------
    element : xml.etree.ElementTree.Element
        An element to examine.

    Returns
    -------
    uri : str
        A string containing the element's uri.  If there is none, return the
        empty string.

    Examples
    --------
    >>> get_uri(div)
    '{http://www.w3.org/1999/xhtml}'
    """
    from re import match
    m = match(r'(\{.+\})',element.tag)
    if m is None:
        uri = ''
    else:
        uri = m.groups()[0]
    return uri
