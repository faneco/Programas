#include <stdio.h>

void ordemCrescente(int vetor[], int n){
	int aux;

	for (int i = 0; i < n; i++){
		for (int j = i+1; j < n; j++){
			if (vetor[i] > vetor[j]){
				aux = vetor[i];
				vetor[i] = vetor[j];
				vetor[j] = aux;
			}		
		}

				
	}

}






int main (){

	int vetor[10] = {6, 4, 1, 9, 8, 0, 5, 7, 3, 2};
	int i;
	void ordemCrescente(int vetor[], int n);

	ordemCrescente(vetor, 10);

	for (i = 0; i < 10; i++){
		printf ("%d ", vetor[i]);

	}

	return 0;
}