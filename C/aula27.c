#include <stdio.h>

int main (){
	const int notasAlunos = 4, Bimestre = 4;
	float nota[notasAlunos][Bimestre];

	float mediaAluno[Bimestre];
	float media;

	for (int aluno = 1; aluno <= notasAlunos; aluno++){
		for (int notas = 1; notas <= Bimestre; notas++){
			printf ("%d aluno nota %d Bimestre: ", aluno, notas);
			scanf ("%f", &nota[aluno][notas]);
			media += nota[aluno][notas];

		}
		printf ("\n");
		mediaAluno[aluno] = media / Bimestre;
		media = 0;
	}

	for (int aluno = 1; aluno <= notasAlunos; aluno++){
		printf ("A media do aluno %d e %.2f \n", aluno, mediaAluno[aluno]);
	}



	return 0;
}