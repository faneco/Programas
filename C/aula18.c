#include <stdio.h>

int main (){
	int num;
	int t1;
	printf ("Digite o numero: ");
	scanf ("%d", &num);

	
	if (num >= 0){
		do{
			t1 = num % 10;
			printf ("%d ", t1);
			num /= 10;
		}while (num != 0);
	}else if (num < 1){
		num *= -1;
		do{
			printf ("-");
			t1 = num % 10;
			printf ("%d ", t1);
			num /= 10;
		}while (num != 0);
	}

	return 0;
}