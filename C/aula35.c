#include <stdio.h>

int fatorial(int x){
	int resultado;

	if (x == 0){
		return 1;
	}else{
		resultado = x * fatorial(x-1);
	}
}

int main (){

	int fatorial(int x);
	int numero, resultado;

	printf ("Digite um numero: ");
	scanf ("%d", &numero);

	resultado = fatorial(numero);

	printf ("%d \n", resultado);




	return 0;
}