gcc -c loop.c -Wint-conversion -Wall
gcc -shared -o loop.dll loop.o -Wall -Wint-conversion
gcc -o loop.exe loop.o -Wall -Wint-conversion
rm loop.o
