#include <stdio.h>
#include <string.h>



int main (void){
	int tamanho = 0;
	char nome[20];
	int i = 0;

	printf ("Digite o nome: ");
	fgets(nome, 20, stdin);


	tamanho = strlen(nome);
	while (tamanho > 10){
		printf ("Digite o nome novamente: ");
		fgets(nome, 20, stdin);
		tamanho = strlen(nome);
	}

	printf ("\n");
	printf ("O nome digitado: %s \n", nome);

	

	while(i < 3 && nome[i] != '\0'){
		printf ("%c ", nome[i]);
		i++;
	}
	printf ("\n");


	return 0;
}