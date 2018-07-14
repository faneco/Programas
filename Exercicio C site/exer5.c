#include <stdio.h>
#include <stdlib.h>

void DesejaImprimir(char imprimir[], char nome[], int telefone){
	int i = 0;
	if (imprimir[i] == 's'){
		printf("nome: %s telefone: %d \n", nome, telefone);
	}else{
		printf("Não aceito imprimir! \n");
	}
}



int main (){
	void DesejaImprimir(char imprimir[], char nome[], int telefone);

	char nome[15], endereco[15], imprimir[15];
	int telefone, i = 0; 

	printf ("Digite o nome: ");
	fgets(nome, 15, stdin);

	printf ("Digite o endereço: ");
	fgets(endereco, 15, stdin);

	printf ("Digite o telefone. DD e telefone: ");
	scanf ("%d %d",&dd &telefone);

	while (imprimir[i] != 's' && imprimir[i] != 'n'){
		printf ("Deseja imprimir (S/N): ");
		fgets (imprimir, 15, stdin);
	}
	

	DesejaImprimir(imprimir, nome, telefone);

	return 0;
}