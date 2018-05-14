#include "bubble_sort.h"

void bubbleSort(int A[], int length)
{
	for(int i = 0; i < length - 1; i++) //for i = 0 to A.length - 1
	{
		for(int j = length; j >= i + 1; j--) //For j = A.length downto i + 1
		{
			if(A[j] < A[j - 1]) //SWAP
			{
				int temp = A[j];
				A[j] = A[j - 1];
				A[j - 1] = temp;
			}
		}
	}
}

void printArray(int A[], int length)
{
	for (int i = 0; i < length; i++)
	{
		printf("%d ", A[i]);
	}
	printf("\n");
}