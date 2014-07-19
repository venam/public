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
		sum += (bin[i] - '0')*pow(2, siz - j);
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

int b10to2(int n) {
	int i;
	char * s = NULL;
	char * temp = NULL;
	int nb = 0;
	do {
		temp = realloc(temp, nb + 1 * sizeof(char));
		if (temp == NULL) {
			printf("failed to allocate memory\n");
			exit(EXIT_FAILURE);
		} else {
		temp[nb] = n % 2;
		n /= 2;
		nb++;
		}
	} while (n > 0);
	s = realloc(s, nb + 1 * sizeof(char));
	if (s == NULL) {
		printf("failed to allocate memory\n");
		exit(EXIT_FAILURE);
	} else {
		for (i = nb; i > -1; i--)
		snprintf(s + strlen(s), sizeof(s), "%d", temp[i]);
	}
	int res = atoi(s);
	free(temp);
	free(s);
	return res;
}

int b10to22(int n ) {
	int i, j;
	int d;
	int siz;

	if (n == 0) { return 0;
	} else if (n == 1) { return 1; }

	for (j = 1, d = 0; d <= n; j++) d = pow(2, j);
	siz = j - 1;
	char tmp[siz]; tmp[0] = '1';
	for (i = 1; i < siz; i++) { tmp[i] = '0'; }

	for (i = 1; n > 1; i++) {
		n -= d*0.5;
		if (n == 0) break;
		for (j = 0, d = 0; d <= n; j++) d = pow(2, j);
		tmp[siz - j + 1] = '1';
	}
	return atoi(tmp);
}

int main(int argc, char **argv) {
    // base 2 to 10
    // char binary[1024];
    // printf("Enter a binary value to convert: ");
    // scanf("%s", binary);
    // printf("(%s)10 = %d\n", binary, b2to10(binary, strlen(binary)));
    // base 10 to 2
    // char n[1024];
    // printf("Enter a decimal value to convert: ");
    // scanf("%s", n);
    // printf("(%s)2 = %d\n", n, base_10(atoi(n)));
    // base 2 to 8
    // char binary[1024];
    // printf("Enter a binary value to convert: ");
	char binary[] = "0100";
	printf("(%s)2 = %d\n", binary, b2to10(binary, strlen(binary)));
	strlcpy(binary, "65", sizeof(binary));
	printf("(%s)8 = %d\n", binary, b8to10(binary, strlen(binary)));
	int a = atoi(argv[1]);
	printf("%d\n", b10to2(a));
	printf("%i\n", b10to22(a));
	return 0;
}
