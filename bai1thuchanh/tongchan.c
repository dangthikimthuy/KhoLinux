#include<stdio.h>
int chan(int n)
{
	int s=0;
	for(int i=0;i<=n;i++)
		if(i%2==0)
			s=s+i;
	return s;
}
