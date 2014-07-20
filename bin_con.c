/* 
 * No idea what the original license is, but I'm taking the liberty to stick
 * ISC on here, found in the same directory as this file, as a file named
 * "LICENSE".
 */

#include <stdio.h>
#include <bsd/string.h>
#include <stdlib.h>
#include <math.h>

//int b2to10(char *, size_t);
//int b8to10(char *, size_t);
//int b10to2(int);

int b2to10(char *bin, size_t siz) {
	int i, j;
	int sum = 0;

	/* this is a conversion of (single) char to int, summed */
	for (i = 0, j = siz - 1; i < siz; i++, j--) {
		sum += (bin[i] - '0')*pow(2, j);
	}
	return sum;
}

int b8to10(char * oct, size_t siz) {
	int i, j;
	int sum = 0;

	/* same as before, but base is 8, instead of 2 */
	for (i = 0, j = siz - 1; i < siz; i++, j--) {
		sum += (oct[i] - '0')*pow(8, j);
	}
	return sum;
}

int b10to2(int n ) {
	int i, j;
	int d;
	int siz;

	if (n == 0) { return 0; }

	/* dirty */
	for (j = 1, d = 0; d <= n; j++) d = pow(2, j);
	siz = j - 1;
	char tmp[siz]; tmp[0] = '1';
	for (i = 1; i < siz; i++) { tmp[i] = '0'; }

	/* dirtier */
	for (i = 1; n > 1; i++) {
		n -= d*0.5;
		if (n == 0) break;
		for (j = 0, d = 0; d <= n; j++) d = pow(2, j);
		tmp[siz - j + 1] = '1';
	}
	return atoi(tmp);
}

int main(int argc, char **argv) {
	if (argc != 3) { printf("We be broke"); return 1; }

	int num = atoi(argv[2]);
	char *str = argv[2];
	int lng = strlen(str);

	switch ( atoi(argv[1]) ) {
		case 2:  
			printf("%i\n", b2to10(str, lng));
			break;
		case 8:  
			printf("%i\n", b8to10(str, lng));
			break;
		case 10:
			printf("%i\n", b10to2(num));
			break;
		default: printf("We be broke\n"); return 1;
	}
	return 0;
}
