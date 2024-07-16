"""
Top level package for sref.site.resource models

These models represent REST resources, web pages, etc.
"""

from dataclasses import dataclass

from ..site import Site

@dataclass
class Page:
    site: Site
    subdirectory: str
    path: str
