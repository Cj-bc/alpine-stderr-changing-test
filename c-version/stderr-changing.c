#include <stdio.h>

int main() {
  fprintf(stderr, "---- Before changing stderr ----\n");
  freopen("/dev/null", "w", stderr);
  fprintf(stderr, "---- After changing stderr (Should not be printed out) ----\n");
  fprintf(stdout, "---- This is stdout ----\n");
}
