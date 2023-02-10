#include <stdint.h>

int loop(uint32_t numb)
{
    int res = 0;
    int i = 0;
    for (i = 0; i < numb; i++)
    {
        res += i;
    }
    return res;
};
