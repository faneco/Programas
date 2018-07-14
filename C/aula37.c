#include <stdio.h>

void FuncaoPrint(int x[3][3]){

	for (int i = 0; i < 3; i++){
		for (int j = 0; j < 3; j++){
			printf ("%d ", x[i][j]);
		} 
		printf ("\n");
	}
}


int main (){

	void FuncaoPrint(int x[3][3]);
	int matriz[3][3] = {1, 2, 3,
						4, 5, 6,
						7, 8, 9};

	FuncaoPrint(matriz);




	return 0;
}