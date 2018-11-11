package main

import (
	"fmt"
)

func main() {
	fmt.Println("Testing binary search function.")
	fmt.Println("Binary search runs in O(logn) time complexity.")

	fmt.Println("Testing one input, result should be true:")
	println(binarySearch([]int{2, 4, 8, 12, 16, 23, 38, 56, 72, 91}, 23))

	fmt.Println("Go Test file in same directory. Reference that to run automated unit tests.")
}

func binarySearch(L1 []int, value int) bool {

	if len(L1) <= 0 {
		println("List is empty!")
		return false
	}

	var low = 0
	var high = len(L1) - 1
	var mid = 0

	for low <= high {
		mid = (low + high) / 2

		if L1[mid] == value {
			return true
		} else if L1[mid] < value {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return  false
}