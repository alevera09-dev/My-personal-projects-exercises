/*
Versión 0 — “El bucle que lee y ejecuta”

(La base más pura, sin nada fancy todavía)

Lo que NECESITO que tengas funcionando al final de la v0:

    * Un bucle infinito que haga printf("> ")

    * Lea una línea con get_string (o con getline si querés ponerte pro)

    * Separe la línea en argumentos usando strtok o similar

    * Ejecute el comando con fork() + execvp()

    * Espere al hijo con waitpid()

    * Soporte solo comandos simples: ls, pwd, echo hola, cat archivo, etc.

    * Si el usuario escribe exit → termina limpio
*/
#define _POSIX_C_SOURCE 200809L
#define MAX_ARGS 64
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

void get_arguments(char *args[], char *line_buffer, int args_count);

int main(void)
{
    char *line_buffer = NULL;
    pid_t pid;
    int args_count = 0;

    do
    {
        char *args[MAX_ARGS]; 
        get_arguments(args, line_buffer, args_count);

        if (strcmp(args[0],"echo") == 0)
        {
            if (args_count < 3)
            {
                perror("Argumentos insuficientes");
                exit()
            }
            else
            {
                printf("%s\n", args[1]);
            }
            
        }
        else
        {
            pid = fork();

            if (pid < 0)
            {
                perror("Error en linea 44.");
            }
            else if (pid == 0)
            {
                execvp(args[0], args);

                perror("Error en linea 52.");
            }
            else
            {
                int estado_hijo;

                waitpid(pid, &estado_hijo, 0);
            }
        }
        
        free(line_buffer);
        line_buffer = NULL;
    } while (1);
    

    return 0;
}

void get_arguments(char *args[], char *line_buffer, int args_count)
{
    size_t buffer_capacity = 0;
    ssize_t read_characters;

    printf(">");
    read_characters = getline(&line_buffer, &buffer_capacity, stdin);

    const char *delim = " \t\n";
    char *arguments;
    

    arguments = strtok(line_buffer, delim);

    while (arguments != NULL)
    {
        args[args_count] = arguments;
        args_count++;
        arguments = strtok(NULL, delim);
    }
    args[args_count] = NULL;

}