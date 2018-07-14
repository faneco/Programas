#include <stdio.h>

void imprimirNomes(char nome1[], char nome2[]){
	void imprimirNumero(char tamanho1[]);
	int i = 0;

	if (nome1[i] == 'a'){
		printf ("%s", nome1);
		imprimirNumero(nome1);
		printf ("\n");
	}else{
		printf ("Primeiro nome não tem letra 'A' no começo \n");
	}
	if (nome2[i] == 'a'){
		printf ("%s", nome2);
		imprimirNumero(nome2);
		printf ("\n");
	}else{
		printf ("Segundo nome não tem letra 'A' no começo \n");
	}
}

void imprimirNumero(char tamanho1[]){
	int i = 0, j = 0;
	while (tamanho1[i] != '\0'){
		i++;
	} 
	printf ("tem: %d palavra ", i-1);
}

int main (void){
	void imprimirNomes(char nome1[], char nome2[]);
	void imprimirNumero(char tamanho1[]);

	char nome1[15];
	char nome2[15];

	printf("Digite 1 nome: ");
	fgets(nome1, 15, stdin);

	printf("Digite 2 nome: ");
	fgets(nome2, 15, stdin);

	imprimirNomes(nome1, nome2);




	return 0;
}