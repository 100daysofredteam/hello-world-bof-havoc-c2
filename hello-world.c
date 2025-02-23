#include <windows.h>
#include <stdio.h>
#include "beacon.h"

int go(char * args, unsigned long length) {
   BeaconPrintf(CALLBACK_OUTPUT, "This BOF was compiled as C file. Thank you for joining me on 100 Days of Red Team\n");
   return 0;
}
