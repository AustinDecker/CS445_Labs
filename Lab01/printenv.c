//Pre processor directives
#include <stdio.h>
#include <stdlib.h>


//display sys env variables
void display_env(){
	const char * command = "printenv";
	printf("===\tSystem Environment Variables\t===\n");
	
	//Too lazy to use getenv, this gets all environment variables.
	system(command);
	
}

int main(){
	display_env();
	return 0;
}
