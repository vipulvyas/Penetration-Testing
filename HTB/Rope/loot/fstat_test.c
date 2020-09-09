#include <stdlib.h>
#include <stdio.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
 
int main(int argc, char *argv[]) {
  if (argc < 2) return -1;
  int f = open(argv[1], O_RDONLY);
  struct stat buffer;
  fstat(f, &buffer);
  printf("size: %d\n", buffer.st_size);
  close(f);
  return 0;
}
