#include <stdio.h>

int main (){
	int num = 5;
	int total = 1;
	
	printf ("Digite um numero inteiro: ");
	scanf ("%d", &num);

	for (; num > 0; num--){
		total *= num;
	}

	printf ("%d \n", total);

	return 0;
}