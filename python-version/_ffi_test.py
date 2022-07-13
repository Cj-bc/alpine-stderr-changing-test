from cffi import FFI

ffibuilder = FFI()

ffibuilder.set_source("_ffi_test", None)
ffibuilder.cdef("""
    /* from stdio.h */
    FILE* fopen(const char* path, const char* mode);
    int fclose(FILE* fp);
    extern FILE *const stderr;  /* GNU C library */
    extern FILE* __stderrp;  /* macOS */
""")

if __name__ == '__main__':
    ffibuilder.compile(verbose=True)
