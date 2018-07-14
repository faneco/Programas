#include <stdio.h>

int main (){

	for (int i = 0; i < 3; i++){
		printf ("###volta %d \n", i);
		for (int j = 0; j < 3; j++){
			printf ("*ponto %d \n", j);
		}
		printf("\n");
	}


	return 0;
}