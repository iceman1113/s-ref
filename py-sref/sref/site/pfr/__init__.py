"""
Main package for the PFR site.
"""

from sref.model.site import Site, Scheme
_site = Site(scheme=Scheme.HTTPS, domain="pro-football-reference.com")
