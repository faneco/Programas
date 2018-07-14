#include <stdio.h>

float areaQuadradaRetangulo(float base, float altura){
	float area = base * altura;

	return area;
}


int main (){

	float area = areaQuadradaRetangulo(10, 20);

	printf ("Area quadrada eh %.2f \n", area);


	return 0;
}