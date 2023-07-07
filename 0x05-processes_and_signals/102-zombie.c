#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(void) {
    int i;

    for (i = 0; i < 5; i++) {
        pid_t pid = fork();

        if (pid < 0) {
            perror("fork error");
            exit(1);
        } else if (pid == 0) {
            // Child process
            exit(0);
        } else {
            // Parent process
            printf("Zombie process created, PID: %d\n", pid);
            sleep(1); // Sleep to allow parent process to create more zombies
        }
    }

    // Infinite loop to keep the parent process running
    while (1) {
        sleep(1);
    }

    return 0;
}

