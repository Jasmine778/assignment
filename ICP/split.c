#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include "header.h"

void split(char details[][80], char* str, char* spl)
{
    int n = 0;
    char * storage = NULL;
    storage = strtok(str, spl);
    while(storage != NULL )
    {
        strcpy(details[n++], storage);
        storage = strtok(NULL, spl);
    }
}
