Austin Decker  
CS445 - Computer Security  
8 September 2024  

---
# LAB 01

---
## Part 1:
![](Screenshot from 2024-09-04 09-47-37.png)

## Part 2:
**Code**
```c
//Pre processor directives
#include <stdlib.h>
#include <stdio.h>


//display sys env variables
void display_env(){
	const char * command = "printenv";
	printf("===\tSystem Environment Variables\t===\n”);
	
	//Too lazy to use getenv, this gets all environment variables.
	system(command);
	
}

int main(){
	display_env();
	return 0;
}
```
**Output**
![](Screenshot from 2024-09-04 10-18-29.png)
![](Screenshot from 2024-09-04 10-18-49.png)
![](Screenshot from 2024-09-04 10-19-07.png)
![](Screenshot from 2024-09-04 10-19-26.png)

