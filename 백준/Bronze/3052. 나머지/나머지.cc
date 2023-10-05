#include <stdio.h>

int main(void)
{
	int s[10];
	int i, j, x;
	int sum = 0;

	for (i = 0; i < 10; i++) {
		scanf("%d", &x);
		s[i] = x % 42;
	}

	for (i = 0; i < 10; i++) {
		for (j = i + 1; j < 10; j++) {
			if (s[i] == -1)
				break;
			if (s[i] == s[j])
				s[j] = -1;
		}
	}

	for (i = 0; i < 10; i++) {
		if (s[i] != -1)
			sum++;
	}

	printf("%d", sum);

}