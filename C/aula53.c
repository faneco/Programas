#include <stdio.h>



int main (){

	char caracteres;
	char linha[100];
	int i;

	do{
		caracteres = getchar();
		linha[i] = caracteres;
		i++;
	}while (caracteres != '\n');

	linha[i-1] = '\0';

	printf ("%s \n", linha);



	return 0;
}