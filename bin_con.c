/* 
 * No idea what the original license is, but I'm taking the liberty to stick
 * ISC on here, found in the same directory as a file named "LICENSE"
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int b2to10(char *, size_t);
int b8to10(char *, size_t);
int b10to2(int);

int b2to10(char *bin, size_t siz) {
	int i;
	int sum = 0;

	for (i = 0; i < siz; i++) {
		/* this is a conversion of (single) char to int, summed */
		sum += (bin[i] - '0')*pow(2, i);
	}
	return sum;
}

int b8to10(char * oct, size_t siz) {
	int i;
	int sum = 0;
	for (i; i < siz; i++) {
		/* same as before, but base is 8, instead of 2 */
		sum += (oct[i] - '0')*pow(8, i);
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

int main(void) {
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
	printf("%d\n", b10to2(20));
	return 0;
}
