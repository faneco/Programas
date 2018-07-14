#include <stdio.h>

int main (){

	int idade;

	do {
		printf ("Informe sua Idade: ");
		scanf ("%d", &idade);

		if (idade > 0 && idade <= 5){
			printf("Bebê \n");
		} else if (idade > 10 && idade <= 10){
			printf("Criança \n");
		}else if (idade > 10 && idade <= 18){
			printf ("Adolecente \n");
		}else if (idade > 18 && idade <= 50){
			printf("Adulto \n");
		}else if (idade > 50){
			printf("Velho\n");
		}

	} while (idade != 0);
		printf ("FIM \n");

	return 0;
}