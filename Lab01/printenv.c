#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[], char * envp[])
{
const char * env_var_name = "SHELL";
char * shell;
int i = 0;
while (envp[i] != NULL) {
printf("%s\n", envp[i++]);
}
shell = (char *)getenv(env_var_name);
if (shell) {
printf("%s's value: %s\n", env_var_name, shell);
printf("%s's address: %p\n", env_var_name, shell);
}
else {
printf("Value is not found for %s\n", env_var_name);
}
}
