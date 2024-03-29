try:
    from processedimagefield.fields import ProcessedImageField
except ImportError:
    try:
        import django.db.models
    except ImportError:
        pass # Django's not installed or configured. Ah well. We can at least expose version info.
    else:
        raise # Django's fine, something else is wrong.

from processedimagefield.transforms import *


VERSION = (0, 1)

def version_string():
    return '.'.join(str(component) for component in VERSION)
