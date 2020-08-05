import torch

def _dict_to_entry(_dict, number_of_tokens=20):
    """ Helper function to convert `ProteinNet` dict to tuple of tensors. """
    # read the values from dict
    sequence = _dict['primary']
    xyz = _dict['tertiary']
    mask = _dict['mask']

    # convert things to tensor
    sequence = torch.tensor(sequence, dtype=torch.int64)
    xyz = torch.tensor(xyz, dtype=torch.float32)
    mask = torch.tensor(xyz, dtype=torch.int64)

    # make sequence one-hot
    sequence = torch.zeros(
        sequence.shape[0],
        number_of_tokens,
    ).scatter(
        1,
        sequence.long(),
        1.0
    )

    return sequence, xyz, mask
