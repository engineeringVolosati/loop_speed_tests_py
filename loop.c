#include <stdint.h>

int loop(uint64_t numb)
{
    uint64_t res = 0;
    uint64_t i = 0;
    for (i = 0; i < numb; i++)
    {
        res += i;
    }
    return res;
};
