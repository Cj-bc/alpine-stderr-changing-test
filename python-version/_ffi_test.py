from cffi import FFI

ffibuilder = FFI()

ffibuilder.set_source("_ffi_test", None)
ffibuilder.cdef("""
    FILE* fopen(const char* path, const char* mode);
    extern FILE* stderr;
""")

if __name__ == '__main__':
    ffibuilder.compile(verbose=True)
