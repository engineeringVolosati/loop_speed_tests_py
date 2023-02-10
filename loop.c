#include <stdio.h>

#define DEBUG 1

#define NUMSYMBOLS 24
#define BUFLEN (NUMSYMBOLS * 8)

void loop(unsigned long long numb)
{
    unsigned long long res = 0;
    for (unsigned long long i = 0; i < numb; i++)
    {
        res += i;
        if (DEBUG && i % 1000000 == 0)
        {
            // printf("i = %llu, res = %llu)\n", i, res);
        }
    }
    printf("%llu", res);
    return;
};

unsigned long long test64(unsigned long long numb)
{
    unsigned long long res = 0;
    for (unsigned long long i = 0; i < numb; i++)
    {
        res += i;
        if (DEBUG && i % 1000000 == 0)
        {
            // printf("i = %llu, res = %llu)\n", i, res);
        }
    }
    unsigned long long res1 = res;
    printf("%llu\n", res);
    return res1;
};

int main()
{
    unsigned long long ans = test64(5000000);

    if (ans == 12499997500000ull)
    {
        printf("\nCorrect answer!\n");
        return 0;
    }
    else
    {
        printf("%llu", ans);
        printf("\nWrong answer!\n");
        return 1;
    }
}
