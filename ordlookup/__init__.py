"""
A small module for keeping a database of ordinal to symbol
mappings for DLLs which frequently get linked without symbolic
info.
"""

from . import ws2_32
from . import oleaut32

ords = {
    'ws2_32.dll': ws2_32.ord_names,
    'wsock32.dll': ws2_32.ord_names,
    'oleaut32.dll': oleaut32.ord_names,
}


def ordLookup(libname, ord, make_name=False):
    """
    Lookup a name for the given ordinal if it's in our
    database.
    """
    names = ords.get(libname.lower())
    if names is None:
        if make_name is True:
            return 'ord%d' % ord
        return None
    name = names.get(ord)
    if name is None:
        return 'ord%d' % ord
    return name
