#include <stdio.h>

int main (){
	int idade;

	printf ("Digite sua idade: ");
	scanf ("%d", &idade);

	if (idade < 18){
		printf("Ainda não tem idade \n");
	}else{
		printf("Bebida libera! \n");
	}
	return 0;
}