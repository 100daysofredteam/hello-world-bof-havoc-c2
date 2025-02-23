# hello-world-bof-havoc-c2
This reporsitory hosts the code for a minimalistic beacon object file that works with Havoc C2.

This code was created as part of [100 Days of Red Team](https://www.100daysofredteam.com/p/creating-a-simple-beacon-object-file-for-havoc-c2)

## Compiling the BOF

- C: x86_64-w64-mingw32-gcc -c hello-world.c -o hello-world.o -w
- C++: x86_64-w64-mingw32-g++ -c hello-world.cpp -o hello-world.o -w

## Loading the BOF
- Method 1: inline-execute /tmp/hello-world.o (assuming that hello-world.o is stored in the /tmp directory)
- Method 2: Load the Python script using Script Manager: Scripts → Script Manager → Load Script, navigate to the path where the Python script is stored, selecte it and press Open.

## Using the BOF
- Method 1: inline-execute /tmp/hello-world.o (assuming that hello-world.o is stored in the /tmp directory)
- Method 2: Type hello-world in the beacon interactive prompt.
