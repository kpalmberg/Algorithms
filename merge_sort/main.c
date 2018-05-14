#include "merge_sort.h"


int main()
{
	int arr[] = { 5,2,4,6,1,31,35,21,64,71,21,15,13 };

	int n = sizeof(arr) / sizeof(int); //get size of array as n

	printf("Print array before merge_sort: ");

	printArray(arr, n);

	doMergeSort(arr, n); //call mergeSort

	printf("Print array after merge_sort: ");
	printArray(arr, n);

	getchar();

	return 0;
}