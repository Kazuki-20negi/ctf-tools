import os
import sys

SIGNATURES = { #マジックナンバー
    'ZIP': b'\x50\x4B\x03\x04',      # PK..
    'PNG': b'\x89PNG\r\n\x1a\n',     # .PNG....
    'PDF': b'%PDF-',                 # %PDF-
    'GIF': b'GIF89a',                # GIF89a
}

