#include <stdio.h>





int main (){

	struct horario{
		int horas;
		int minutos;
		int segundos;
	};

	struct horario teste[5] = {{10, 20, 30}, {40, 50, 60},
								{70, 80, 90}, {100, 110, 120}, 
								{130, 140, 150}};

	for (int i = 0; i < 5; i++){
		printf ("%d: %d: %d \n", teste[i].horas, 
								 teste[i].minutos, 
								 teste[i].segundos);

	}



	return 0;
}