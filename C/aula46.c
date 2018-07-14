#include <stdio.h>

void concatenarString(char string1[], int t1, char string2[], 
					  int t2, char string3[]){
	int i, j;
	for (i = 0; i < t1; i++){
		string3[i] = string1[i];
	}
	for (j = 0; j < t2; j++){
		string3[t1 + j] = string2[j];
	}
}

int main (){
	void concatenarString(char string1[], int t1, char string2[], 
										  int t2, char string3[]);

	char palavra1[] = {'p', 'a', 'o', ' '};
	char palavra2[] = {'m', 'o', 'r', 't', 'a','n', 'd', 'e', 'l', 'a'};
	char novaPalavra[14];
	int i;

	concatenarString(palavra1, 4, palavra2, 10, novaPalavra);

	for (i = 0; i < 14; i++){
		printf ("%c ", novaPalavra[i]);
	}
	printf ("\n");

	return 0;
}