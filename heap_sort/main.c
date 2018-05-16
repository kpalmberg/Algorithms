#include "heapsort.h"

int main()
{
	int arr[] = {3, 5, 71, 22, 44, 20, 83, 28, 73, 33, 13, 15, 2, 6, 9, 7, 47};

	int n = sizeof(arr) / sizeof(int); //get size of array as n

	printf("HEAP SORT ALGORITHM:\n");
	printf("Print array before heap_sort: ");

	printArray(arr, n);

	heapSort(arr, n); //Call max heap function

	printf("Print array after heap_sort: ");
	printArray(arr, n);

	printf("Press any key to continue...");
	getchar();

	return 0;
}