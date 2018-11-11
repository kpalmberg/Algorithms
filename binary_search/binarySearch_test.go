package main

import (
	"testing"
)

type TestIOs struct {
	L1 []int
	value int
	expected bool
}

// Test table
var testIOs = []TestIOs {
	{[]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 8, true},
	{[]int{2, 4, 8, 12, 16, 23, 38, 56, 72, 91}, 38, true},
	{[]int{2, 4, 8, 12, 16, 23, 38, 56, 72, 91}, 18, false},
	{[]int{2, 4, 8, 12, 16, 23, 38, 56, 72, 91}, 72, true},
	{[]int{2, 4, 8, 12, 16, 23, 38, 56, 72, 91}, 64, false},
	{[]int{}, 64, false},
	{[]int{1}, 5, false},
	{[]int{3}, 3, true},

}

// Test function to test binary search
func TestBinarySearch(t *testing.T) {
	for _, test := range testIOs {
		result := binarySearch(test.L1, test.value)

		if result != test.expected {
			t.Fatal("Binary Search function failed!")
		}
	}
}
