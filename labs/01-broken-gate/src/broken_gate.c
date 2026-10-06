#include <stdio.h>
#include <string.h>
#include <windows.h>

static int validate_license(const char *license) {
    const char expected[] = "NE0SYNC-LAB-2026";
    return strcmp(license, expected) == 0;
}

int main(void) {
    char license[64] = {0};
    char username[256] = {0};
    DWORD username_length = (DWORD)sizeof(username);

    printf("NE0SYNC RE Lab 01 - The Broken Gate\n");
    printf("Enter license: ");
    if (scanf("%63s", license) != 1) {
        puts("rejected");
        return 1;
    }

    GetUserNameA(username, &username_length);
    printf("analyst: %s\n", username[0] ? username : "unknown");

    if (!validate_license(license)) {
        puts("rejected");
        return 1;
    }

    puts("accepted");
    puts("training-token: BG-LOCAL-SYNTHETIC-ONLY");
    return 0;
}
