#include "merge_sort.h"

void merge(int A[], int left, int middle, int right)
{
	int n1 = (middle - left) + 1; //size of left array
	int n2 = (right - middle); //size of right array

	int L[n1]; //array of size n1
	int R[n2]; //array of size n2
	
	for (int i = 0; i < n1; i++) //For the size of the left array
	{
		L[i] = A[left + i]; //Populate it with all the values from the left list half
	}
	for (int j = 0; j < n2; j++) //For the size of the right array
	{
		R[j] = A[middle + 1 + j]; //Populate it will all the values from the right list half
	}
	int i = 0; //initial index for first subarray
	int j = 0; //initial index for second subarray
	int k = left; //initial index of merged subarray

	while (i < n1 && j < n2) //while not exceeding bounds of sub arrays
	{
		//Put the lower of the values into A[k]
		if (L[i] <= R[j])
		{
			A[k] = L[i];
			i++;
		}
		else
		{
			A[k] = R[j];
			j++;
		}
		k++; //next element in original array
	}

	//Copy remaining values of L array into original array
	while (i < n1)
	{
		A[k] = L[i];
		i++;
		k++;
	}

	//Copy remaining values of R array into original array
	while (j < n2)
	{
		A[k] = R[j];
		j++;
		k++;
	}
}

void mergeSort(int A[], int left, int right)
{
	if (left < right)
	{
		int middle = left + (right - left) / 2;
		int middle2 = (left + right) / 2;
		mergeSort(A, left, middle);
		mergeSort(A, middle + 1, right);
		merge(A, left, middle, right);
	}
}

void doMergeSort(int A[], int length)
{
	mergeSort(A, 0, length - 1);
}

void printArray(int A[], int length)
{
	for (int i = 0; i < length; i++)
	{
		printf("%d ", A[i]);
	}
	printf("\n");
}