import hashlib


def hash_file(file):  # bytes
    """fn to cal sha1 for a given file"""
    h = hashlib.sha1(file)
    return h.hexdigest()
