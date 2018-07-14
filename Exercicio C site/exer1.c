#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void imprimir(char nome[]){
	int i = 0;
	while (nome[i] != '\0' && i < 4){
		printf ("%c ", nome[i]);
		i++;
	}
	printf("\n");
}

int main (){

	void imprimir(char nome[]);
	char nome[15];
	int i = 0;

	printf ("Digite o nome: ");
	scanf ("%s", nome);
	
	imprimir(nome);


	return 0;
}