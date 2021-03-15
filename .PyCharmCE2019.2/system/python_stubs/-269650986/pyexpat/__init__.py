# encoding: utf-8
# module pyexpat
# from (pre-generated)
# by generator 1.147
""" Python wrapper for Expat parser. """

# imports
import pyexpat.errors as errors # <module 'pyexpat.errors'>
import pyexpat.model as model # <module 'pyexpat.model'>

# Variables with simple values

EXPAT_VERSION = 'expat_2.2.6'

native_encoding = 'UTF-8'

XML_PARAM_ENTITY_PARSING_ALWAYS = 2
XML_PARAM_ENTITY_PARSING_NEVER = 0

XML_PARAM_ENTITY_PARSING_UNLESS_STANDALONE = 1

# functions

def ErrorString(*args, **kwargs): # real signature unknown
    """ Returns string error for given number. """
    pass

def ParserCreate(*args, **kwargs): # real signature unknown
    """ Return a new XML parser object. """
    pass

# classes

class ExpatError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



error = ExpatError


class XMLParserType(object):
    """ XML parser """
    def ExternalEntityParserCreate(self, *args, **kwargs): # real signature unknown
        """ Create a parser for parsing an external entity based on the information passed to the ExternalEntityRefHandler. """
        pass

    def GetBase(self, *args, **kwargs): # real signature unknown
        """ Return base URL string for the parser. """
        pass

    def GetInputContext(self, *args, **kwargs): # real signature unknown
        """
        Return the untranslated text of the input that caused the current event.
        
        If the event was generated by a large amount of text (such as a start tag
        for an element with many attributes), not all of the text may be available.
        """
        pass

    def Parse(self, *args, **kwargs): # real signature unknown
        """
        Parse XML data.
        
        `isfinal' should be true at end of input.
        """
        pass

    def ParseFile(self, *args, **kwargs): # real signature unknown
        """ Parse XML data from file-like object. """
        pass

    def SetBase(self, *args, **kwargs): # real signature unknown
        """ Set the base URL for the parser. """
        pass

    def SetParamEntityParsing(self, *args, **kwargs): # real signature unknown
        """
        Controls parsing of parameter entities (including the external DTD subset).
        
        Possible flag values are XML_PARAM_ENTITY_PARSING_NEVER,
        XML_PARAM_ENTITY_PARSING_UNLESS_STANDALONE and
        XML_PARAM_ENTITY_PARSING_ALWAYS. Returns true if setting the flag
        was successful.
        """
        pass

    def UseForeignDTD(self, *args, **kwargs): # real signature unknown
        """
        Allows the application to provide an artificial external subset if one is not specified as part of the document instance.
        
        This readily allows the use of a 'default' document type controlled by the
        application, while still getting the advantage of providing document type
        information to the parser. 'flag' defaults to True if not provided.
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


# variables with complex values

expat_CAPI = None # (!) real value is '<capsule object "pyexpat.expat_CAPI" at 0x0000022B1739B120>'

features = [
    (
        'sizeof(XML_Char)',
        1,
    ),
    (
        'sizeof(XML_LChar)',
        1,
    ),
    (
        'XML_DTD',
        0,
    ),
    (
        'XML_CONTEXT_BYTES',
        1024,
    ),
    (
        'XML_NS',
        0,
    ),
]

version_info = (
    2,
    2,
    6,
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022B173740B8>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyexpat', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022B173740B8>, origin='C:\\\\BuildAgent\\\\system\\\\.persistent_cache\\\\pythons\\\\python37\\\\DLLs\\\\pyexpat.pyd')"

