#include <stdio.h>
#include <string.h>
#include <stdlib.h>




int main (){
	int tamanho = 0, i = 0;
	char nome[15];

	printf ("Digite a frase: ");
	fgets(nome, 15, stdin);

	tamanho = strlen(nome);
	i = tamanho;


	while (tamanho > 5){
		fgets(nome, 15, stdin);
		tamanho = strlen(nome);
	}
	i = 0;
	while (i < tamanho-1){
		printf ("%c - %d \n", nome[i], i+1);
		i++;
	}
		

	return 0;
}