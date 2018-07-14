#include <stdio.h>

void nomeImpar(char nome[]){
	int i = 0;
	while (nome[i] != '\0'){
		if (i % 2 == 0){
			printf ("%c %d \n", nome[i], i+1);
			
		}
		i++;

	}
	printf ("\n");
}



int main (){
	void nomeImpar(char nome[]);

	char nome[15];
	printf ("Digite um nome: ");
	scanf ("%s", nome);


	nomeImpar(nome);


	return 0;
}