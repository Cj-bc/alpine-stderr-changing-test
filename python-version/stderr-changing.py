from _ffi_test import ffi as _ffi
import os as _os

stdio = _ffi.dlopen(None)
getattr(stdio, 'stderr')
devnull = stdio.fopen(_os.devnull.encode(), b'w')
setattr(stdio, 'stderr', devnull)
