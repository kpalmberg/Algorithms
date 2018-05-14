#include "bubble_sort.h"

int main()
{
	int arr[] = {3, 5, 71, 22, 44, 20, 83, 28, 73, 33, 13, 15, 2, 6, 9, 7, 47};

	int n = sizeof(arr) / sizeof(int); //get size of array as n

	printf("BUBBLE SORT:\n");
	printf("Print array before bubble_sort: ");

	printArray(arr, n);

	bubbleSort(arr, n); //call bubbleSort

	printf("Print array after bubble_sort: ");
	printArray(arr, n);

	printf("Press any key to continue...");
	getchar();

	return 0;
}