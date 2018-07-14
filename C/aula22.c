#include <stdio.h>

int main (){

	int nota[4];

	for (int i = 1; i <= 5; i++){
		printf ("Digite %d numero: ", i);
		scanf ("%d", &nota[i]);
	}

	for (int i = 1; i <= 5; i++){
		printf ("%d \n", nota[i]);
	}

	return 0;
}