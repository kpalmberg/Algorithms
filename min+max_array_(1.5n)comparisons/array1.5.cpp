/* Author: Kevin Palmberg
* Description: Algorithm to find the min and max element within an array
* while only using a max of 1.5*n comparisons. */

#include <iostream>

int main()
{	
	int a[10] = { 12,64,23,35,11,6,33,97,52,78 }; //array to analyze
	int comparisons = 0; //int to track comparisons
	int n = sizeof(a) / sizeof(a[0]); //get size of array
	int min = a[0]; //initialize min
	int max = a[0]; //initialize max
	
	for (int i = 0; i < (n / 2); i++)
	{
		comparisons++;
		if (a[2 * i] < a[(2 * i) + 1])  //comparison #1 (ALWAYS OCCURS)
		{
			comparisons++;
			if (a[2 * i] < min) //comparison (ROUTE #1)
			{
				min = a[2 * i];
			}
			comparisons++;
			if (a[(2 * i) + 1] > max) //comparison (ROUTE #1)
			{
				max = a[(2 * i) + 1];
			}
		}
		else
		{
			comparisons++;
			if (a[(2 * i) + 1] < min) //comparison (ROUTE #2)
			{
				min = a[(2 * i) + 1];
			}
			comparisons++;
			if (a[2 * i] > max) //comparison (ROUTE #2)
			{
				max = a[2 * i];
			}
		}
	}
		
	printf("Array analyzed: ");

	for (int i = 0; i < n; i++)
	{
		printf("%d ", a[i]);
	}
	printf("\nMinimum element in an array : %d\n", min);
	printf("Maximum element in an array : %d\n", max);
	
	printf("\nNumber of elements in array n = %d\n", n);
	printf("Algorithm should only use max of (n * 1.5) comparisons.\n");
	int m = n * 1.5;
	
	printf("(n * 1.5) = %d\n", m);
	printf("Total comparisons made: %d\n", comparisons);
	std::cout << std::endl;

    return 0;
}

