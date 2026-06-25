import hashlib

def get_file_hash(path):

    md5 = hashlib.md5()

    with open(path, "rb") as f:

        for chunk in iter(
            lambda: f.read(4096),
            b""
        ):
            md5.update(chunk)

    return md5.hexdigest()