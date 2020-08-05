import torch
from pisco.data.utils.protein_net_parser_to_raw import read_record

def _dict_to_entry(_dict, number_of_tokens=20):
    """ Helper function to convert `ProteinNet` dict to tuple of tensors. """
    # read the values from dict
    sequence = _dict['primary']
    xyz = _dict['tertiary']
    mask = _dict['mask']

    # convert things to tensor
    sequence = torch.tensor(sequence, dtype=torch.int64)
    xyz = torch.tensor(xyz, dtype=torch.float32)
    mask = torch.tensor(mask, dtype=torch.int64)

    # make sequence one-hot
    sequence = torch.zeros(
        sequence.shape[0],
        number_of_tokens,
    ).scatter(
        1,
        sequence[:, None].long(),
        1.0
    )

    return sequence, xyz, mask

def read_records(path, number_of_tokens=20, first=9999999):
    """ Read multiple records from path. """
    f_handle = open(path, 'r')
    count = 0
    while count < first:
        count += 1
        record = read_record(f_handle, number_of_tokens)
        if record is None:
            break
        yield _dict_to_entry(record)
