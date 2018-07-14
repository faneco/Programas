#include <stdio.h>
#include <stdbool.h>

struct dicionario{
	char palavra[20];
	char definicao[50];
};

bool comprarString(const char palavra1[], const char palavra2[]){
	int i = 0;
	while (palavra1[i] == palavra2[i] && 
						palavra1[i] != '\0' && palavra2[i] = '\0'){
		i++;
	}
	if (palavra1[i] == '\0' && palavra2[i] == '\0'){
		return true;
	}else{
		return false;
	}
}

int procurarString(const struct dicionario lingua[], 
	const char procurar[], const int numDePalavras){

	bool comprarString(const char palavra1[], const char palavra2[]);

	int i = 0;
	while (i < numDePalavras){
		if (comprarString(procurar, lingua[i].palavra)){
			return i;
		}else{
			return ++i;
		}
	}
	return -1;	

}

int main (){
	const int NUMERODEFINICOES = 7;
	char palavra[20];
	int resultadoPesquisa;


	const struct dicionario portugues[NUMERODEFINICOES] = 
	{{"pao", "comida de farinha"},
	{"mortadela", "comida de carne"},
	{"feijao", "comida brasileira"}};

	printf ("Digite um palavra: ");
	scanf ("%s", palavra);

	resultadoPesquisa = procurarString(portugues, palavra, 
									   NUMERODEFINICOES);
	if (resultadoPesquisa != -1){
		printf("%s\n", portugues[resultadoPesquisa].definicao);
	}else{
		printf("palavra não encontrada \n");
	}

	return 0;
}