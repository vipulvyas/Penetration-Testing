#include <stdio.h>

void main(int argc, const char *argv[]){
	
	const char *string = argv[1];
	int cont = 0;
	
	printf("\n");
	
	for(int i=0; string[i] != '\0'; i++)
	{
		if(cont > 6)
		{
			cont =0;
			printf("\n");
		}
		if(string[i] == 'r')
			printf("1");
		else
			printf("0");
		cont ++;
	}
	printf("\n");
}
