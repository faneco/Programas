#include <stdio.h>
#include <string.h>
#include <ctype.h> 
#include <stdlib.h>

char maiusculo(char nome[]){
	int tamanho;
	char letra[15];

	tamanho = strlen(nome);
	for (int i = 0; i < tamanho; i++){
		printf ("%c", toupper(nome[i]));
		
	}
}


int main (void){
	char nome[15];
	char letra[15];
	printf ("Digite o nome: ");
	fgets(nome,	 15, stdin);
	
	maiusculo(nome);


	return 0;
}
