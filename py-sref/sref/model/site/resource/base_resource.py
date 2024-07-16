"""
"""
from __future__ import annotations
import logging

class BaseResource:
    """
    Base class for resources to be extended by resource type classes or concrete resource classes
    """
    # Class logger.
    LOGGER = logging.getLogger("%s.BaseResource" %__module__)

    # Static, to be set by the implementing concrete resource class.
    # Map of resource identifier (i.e. URL) to resource instances.  One map per concrete resource
    # class.
    RESOURCE_MAP: dict[str, BaseResource] = dict()

    def __new__(cls):
        """
        Static instantiator.  Check for existing instantiations of the resource before creating a
        new instance
        """
        pass
