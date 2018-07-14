#include <stdio.h>


int main (){

	struct horario{
		int horas;
		int minutos;
		int segundos;
		float teste;
		char letra;
	};

	struct horario agora;
	agora.horas = 15;
	agora.minutos = 17;
	agora.segundos = 30;

	struct horario depois;
	depois.horas = agora.horas + 10;
	depois.minutos = agora.minutos;
	depois.teste = 50.55 / 123;
	depois.letra = 'a';

	printf ("%d: %d: %d \n", agora.horas, agora.minutos, agora.segundos);

	printf ("%d \n", depois.horas);
	printf ("%d \n", depois.minutos);
	printf("%f \n",depois.teste);
	printf ("%c \n", depois.letra);	







	return 0;
}