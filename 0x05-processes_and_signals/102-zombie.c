#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
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

	while (i < 5)
	{
		child = fork();
		wait();
		printf("Zombie process created, PID: %d \n", child);
		i++;
	}
	infinite_while;
}
