// #include <stdint.h>
#include <stdio.h>
#include <string.h>

#define DEBUG 0

#define NUMSYMBOLS 24
#define BUFLEN (NUMSYMBOLS * 8)

void debugprint(unsigned long long res, int go)
{
    if (DEBUG == 0 || go != 0)
        return;
    char buf[BUFLEN];
    memset(buf, 0x00, BUFLEN);
    sprintf(buf, "%d", res);
    printf("The res is %s\n", buf);
}

int loop(unsigned long long numb)
{
    unsigned long long res = 0;
    for (unsigned long int i = 0; i < numb; i++)
    {
        res += i;
        debugprint(res, i % 1000000);
    }
    debugprint(res, 0);
    return res;
};
