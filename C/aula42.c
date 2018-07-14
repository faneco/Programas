#include <stdio.h>

struct horario{
	int horas;
	int minutos;
	int segundos;
};



int main (){

	struct horario teste(struct horario x);

	struct horario agora;
	agora.horas =  10;
	agora.minutos = 42;
	agora.segundos = 58;

	struct horario proximo;
	proximo = teste(agora);

	printf ("%d %d %d \n", proximo.horas, proximo.minutos, proximo.segundos);

	return 0;
}


struct horario teste(struct horario x){

	printf ("%d %d %d \n", x.horas, x.minutos, x.segundos);
	
	x.horas = 100;
	x.minutos = 100;
	x.segundos = 100;

	return x;
}