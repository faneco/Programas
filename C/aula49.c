#include <stdio.h>

int stringPalavra (char string1[]){
	int contador = 0;
	while (string1[contador] != '\0'){
		contador ++;
	}
	return contador;

}



int main (){
	int stringPalavra (char string1[]);
	int total;
	char palavra[20];

	printf ("Digite um letra: ");
	scanf ("%s", palavra);

	total = stringPalavra(palavra);

	printf ("%d \n", total);

	return 0;
}