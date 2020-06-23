"""
pisco
Probabilistic Inference for Shape, Conformation, and Organization of Macromolecular Systems
"""

# Add imports here
from .pisco import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
