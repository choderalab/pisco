# =============================================================================
# IMPORTS
# =============================================================================
import torch
import abc

# =============================================================================
# ABSTRACT CLASSES
# =============================================================================
class IterableDataset(abc.ABC, torch.utils.data.IterableDataset):
    """ Iterable Dataset. """

    def __init__(self, iterable):
        super(IterableDataset, self).__init__()
        self.iterable = iterable

    def __iter__(self):
        return iter(self.iterable)
