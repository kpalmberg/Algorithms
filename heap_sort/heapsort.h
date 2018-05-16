#ifndef HEAPSORT_H
#define HEAPSORT_H

#include <stdio.h>

int Left(int i);
int Right(int i);
void exchange(int A[], int i, int j);
void maxHeapify(int A[], int i, int n);
void buildMaxHeap(int A[], int A_length);
void heapSort(int A[], int n);
void printArray(int A[], int length);

#endif