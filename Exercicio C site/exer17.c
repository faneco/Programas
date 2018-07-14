#include <stdio.h>
#include <string.h>


void vogais(char nome[]){
	float porcentagem(float tamanho, float x);
	float tamanho = 0;
	int i = 0, x = 0;
	float total = 0;

	tamanho = strlen(nome);
	for (i = 0; i < tamanho; i++){
		if (nome[i] == 'a' || nome[i] == 'e' || nome[i] == 'i' ||
			nome[i] == 'o' || nome[i] == 'u'){
			x++;
		}

	}
		
	printf("numero de vogais %d numero total de letra %.0f \n", x, tamanho-1);
	total = porcentagem(tamanho, x);
	printf ("porcentagem da vogais em relação as letra: %.2f \n", total);
}

float porcentagem(float tamanho, float x){
	float total = 0;
	tamanho--;
	total = (tamanho / 100) * x;
	return total;
}

int main (void){
	void vogais(char nome[]);

	char nome[15];

	printf ("Digite o nome: ");
	fgets(nome, 15, stdin);

	vogais(nome);





	return 0;
}