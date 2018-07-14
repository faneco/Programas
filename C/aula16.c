#include <stdio.h>

int main (){

	int op;

	printf ("Informe um numero 0 a 5: ");
	scanf ("%d", &op);


	switch (op){
		case 1: 
			printf ("Primeiro \n"); break;
		case 2:
			printf ("Segundo \n"); break;
		case 3: 
			printf ("Terceiro \n"); break;
		case 4:
			printf("Quarto \n"); break;
		case 5:
			printf("Quinto\n"); break;
	}
}