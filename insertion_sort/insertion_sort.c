#include "insertion_sort.h"

void insertionSort(int A[], int length)
{
	for (int currentIndex = 1; currentIndex < length; currentIndex++)
	{
		int key = A[currentIndex]; //Get the current element in array

		int i = currentIndex - 1; //Get the index of the previous element in array

		//{ 5,2,4,6,1,31,35,21,64,71,21,15,13};

		while (i >= 0 && A[i] > key)
		{
			A[i + 1] = A[i]; //Repleace current index value with previous index value
			i--; //Decrement i to place it further towards the start of the array
		}
		/* If current element didn't need to be replaced, this simply assignns it to itself in the
		array, since i would be the previous index in the array under this case.
		Otherwise, variable i will be updated from the above while loop, and it will insert key appropriately. */
		A[i + 1] = key;
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