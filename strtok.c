#include <stdio.h>
#include <string.h>
/**
 * 
*/
int main(void)
{
char str[] = "This is a sparated word by space";
char delim[5] =" ";
char *trunks;
trunks = strtok(str, delim);
while (trunks != NULL)
{
printf("%s\n", trunks);
trunks = strtok(NULL, delim);
}
return (0);
}
