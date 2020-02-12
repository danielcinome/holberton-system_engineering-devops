#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <signal.h>
/**
* infinite_while - infinite
* Return: 0
*/
int infinite_while(void)
{
	while (1)
	{
	sleep(1);
	}
	return (0);
}
/**
* main - created process child
*/
void main(void)
{
	int i = 0;
	pid_t child;

	child = 1;
	while (i < 5)
	{
		if (child != 0)
		{
			child = fork();
			kill (child, SIGCHLD);
			printf("Zombie process created, PID: %d\n", child);
			
		}
		i++;
	}
	infinite_while;
}
