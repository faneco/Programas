#include <stdio.h>
#include <stdlib.h>

void verificaPalavra(char frase[]){
	int x = 0;
	int a = 0, e = 0, i = 0, o = 0, u = 0;

	while (frase[x] != '\0'){
		if (frase[x] == 'a'){
			a++;
		}else if (frase[x] == 'e'){
			e++;
		}else if (frase[x] == 'i'){
			i++;
		}else if (frase[x] == 'o'){
			o++;
		}else if (frase[x] == 'u'){
			u++;
		}
		x++;
		
	}
	printf ("A-%d E-%d I-%d O-%d U-%d \n", a, e, i, o, u);
}



int main (){
	void verificaPalavra(char frase[]);

	char frase[100];

	printf("Digite uma mensagem: \n");
	fgets(frase, 100, stdin);

	verificaPalavra(frase);



	return 0;
}