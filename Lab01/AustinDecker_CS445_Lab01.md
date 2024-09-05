Austin Decker  
CS445 - Computer Security  
8 September 2024  

---
# LAB 01

## Part 1:
![](Screenshot from 2024-09-04 09-47-37.png)

## Part 2:
**Code**
```c
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char * argv[], char * envp[]){
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
```
**Output**
![](Screenshot from 2024-09-05 13-36-04.png)
![](Screenshot from 2024-09-05 13-36-36.png)
![](Screenshot from 2024-09-05 13-36-56.png)
![](Screenshot from 2024-09-05 13-38-02.png)

