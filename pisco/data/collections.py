# =============================================================================
# IMPORTS
# =============================================================================
import torch
import abc
import pytest
# =============================================================================
# COLLECTIONS
# =============================================================================
def protein_net_example():
    import pisco
    from pisco.data.utils.protein_net_parser import read_records
    import os
    return pisco.data.datasets.IterableDataset(
            read_records(
                os.path.dirname(pisco.data.__file__) + '/protein_net_example.txt',
            )
    )
