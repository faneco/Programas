#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void inverteNome(char nome[]){
	int i, tamanho;
	tamanho = strlen(nome);
	for (i = tamanho; i >= 0; i--){
		printf ("%c ", nome[i]);
	}
	printf ("\n");
}

int main (void){
	void inverteNome(char nome[]);

	char nome[15];

	printf("Digite um nome: ");
	fgets(nome, 15, stdin);

	inverteNome(nome);


	return 0;
}