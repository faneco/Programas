#include <stdio.h>

int main (){

	float nota[5];
	float total, media;

	for (int i = 1; i < 5; i++){
		printf ("Digite %d nota: ", i);
		scanf ("%f", &nota[i]);
		total += nota[i];
	}
	media = total / 4;
	printf ("Nota total: %.2f \n", total);
	printf ("Media: %.2f \n", media);



	return 0;
}