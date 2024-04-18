#include <stdio.h>
#include <stdlib.h>
/**
 * main -
*/
int main(int ac, char **av)
{
int i;
printf("argv content is argv[]\n");
while (*av != NULL)
{
printf("argv = %s\n", *av);
av++;
}
}