#include <windows.h>
int main(void){
    MessageBoxW(
        NULL,
        L'MY FIRST MESSGE!'
        L'YIPPIE'
        MB_ICONEXCLAMATION | MB_OKCANCEL
    );
    return EXIT_SUCCESS;
}