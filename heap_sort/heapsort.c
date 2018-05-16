#include "heapsort.h"

//Returns the left "node" based off index in the array
int Left(int i)
{
    return (2 * i);
}

//Returns the right "node" based off index in the array
int Right(int i)
{
    return ((2 * i) + 1);
}

//Exchanges two elements in array A based off indexes i and j
void exchange(int A[], int i, int j)
{
	int temp = A[i];
	A[i] = A[j];
	A[j] = temp;
}

//Converts array A in a bottom-up manner into a max-heap
void maxHeapify(int A[], int i, int n)
{
    int largest = i;
    int l = Left(i);
    int r = Right(i);

    if(l < n && A[l] > A[r])
    {
        largest = l;
    }

    if(r < n && A[r] > A[largest])
    {
        largest = r;
    }

    if(largest != i)
    {
		exchange(A, i, largest);
        maxHeapify(A, largest, n);
    }
}

//Goes through elements of the tree and calls maxHeapify on each one
void buildMaxHeap(int A[], int A_length)
{
    for(int i = (A_length / 2) - 1; i >= 0; i--)
    {
        maxHeapify(A, i, A_length);
    }
}

//First builds the max_heap, then sorts in ascending order using exchange and maxHeapify
void heapSort(int A[], int n)
{
    buildMaxHeap(A, n);

    for(int i = (n - 1); i >= 0; i--)
    {
		exchange(A, 0, i);
		maxHeapify(A, 0, i);
    }
}

//Prints the given array, needs to be passed length
void printArray(int A[], int length)
{
	for (int i = 0; i < length; i++)
	{
		printf("%d ", A[i]);
	}
	printf("\n");
}