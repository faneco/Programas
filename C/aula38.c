#include <stdio.h>

int funcaoPrint(int x, int vetor[]){
	x += 10;
	vetor[0] = 20;


	printf ("F X %d \n", x);
	printf ("F vetor %d \n", vetor[0]);
}


int main (){

	int x = 10;
	int vetor[3] = {10};

	funcaoPrint(x, vetor);

	printf ("X %d \n", x);
	printf("vetor %d \n", vetor[0]);


	return 0;
}