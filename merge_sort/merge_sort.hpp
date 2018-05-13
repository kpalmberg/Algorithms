#ifndef INSERTION_H
#define INSERTION_H
#pragma once

#include <iostream>
#include <vector>
using std::cout;
using std::endl;
using std::vector;
void merge(int A[], int left, int middle, int right);
void mergeSort(int A[], int left, int right);
void doMergeSort(int A[], int length);
void printArray(int A[], int length);

#endif