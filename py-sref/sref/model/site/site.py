"""
Model containing all the required attributes for a site
"""

from dataclasses import dataclass

from .scheme import Scheme

@dataclass
class Site:
    """
    Model containing all the required attributes for a site
    """
    domain: str
    scheme: Scheme
