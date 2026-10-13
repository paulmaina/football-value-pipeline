"""Semantic CSV binding across Git's LF/CRLF conversion; archive hashes stay exact."""
import hashlib


def forecast_digest_variants(path):
    data=path.read_bytes()
    lf=data.replace(b'\r\n',b'\n')
    return {hashlib.sha256(value).hexdigest() for value in (data,lf,lf.replace(b'\n',b'\r\n'))}
