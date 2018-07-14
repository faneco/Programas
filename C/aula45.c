#include <stdio.h>

struct horario{
	int horas;
	int minutos;
	int segundos;
};

void receberhorario(struct horario lista[5]){
	int i;

	for (i = 0; i < 5; i++){
		printf ("Digite o %d primeiro horario (hh:mm:ss): ", i+1);
		scanf ("%d:%d:%d",	&lista[i].horas,
							   	&lista[i].minutos,
							   	&lista[i].segundos);
	}

}

void printHorario(struct horario lista[5]){
	for (int i = 0; i < 5; i++){
		printf ("O %d horario e = %d: %d: %d \n", i+1, 
												lista[i].horas,
							    				lista[i].minutos,
							   					lista[i].segundos);
	}
	
}



int main(){

	void receberhorario(struct horario lista[5]);
	void printHorario(struct horario lista[5]);

	struct horario listaHorario[5];

	receberhorario(listaHorario);
	printHorario(listaHorario);



	return 0;
}