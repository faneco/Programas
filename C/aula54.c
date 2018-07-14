#include <stdio.h>

void alfabetico(char nome){
	if (nome >= 'a' && nome <= 'z' || nome >= 'A' && nome <= 'Z'){
		printf ("é nome \n");
	}else{
		printf ("não é nome \n");
	}

}


int main (){
	void alfabetico(char nome);

	char letra[20];
	int i;
	printf ("Digite nome: ");
	scanf ("%s", letra);

	while (letra[i] != '\0'){
		alfabetico(letra[i]);
		i++;
	}




	return 0;
}