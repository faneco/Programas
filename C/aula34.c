#include <stdio.h>

float somaDeDigitos(float num1, float num2){
	float valorAbsoluto(float x);

	if (num1 < 0){
		num1 = valorAbsoluto(num1);
	}
	if (num2 < 0){
		num2 = valorAbsoluto(num2);
	}
}

float valorAbsoluto(float x){
	return x * -1;
}

int main (){

	float somaDeDigitos(float num1, float num2);
	float a, b, soma;

	printf ("Digite 2 numero: ");
	scanf ("%f %f", &a, &b);

	soma = somaDeDigitos(a, b);

	printf ("%.2f \n", soma);

	return 0;
}

