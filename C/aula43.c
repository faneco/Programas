#include <stdio.h>




int main (){

	struct horario{
		int horas;
		int minutos;
		int segundos;
	}agora = {10, 20, 30};



	printf("%d: %d: %d \n", agora.horas, agora.minutos, agora.segundos );
	





	return 0;
}