This algorithm determines whether two items in a list are equal to a given sum. There are two functions, one equip to handle a sorted list
and another equip to handle sorted or unsorted. The naive solution for this would probably result in O(n^2) time complexity, using a double
for loop method to check every single pair in the list against the given sum. An okay solution would be to use binary search on each item in
the list. Since binary search runs in O(log(n)) this would result in O(nlog(n)) worse case for that algorithm. Instead we investigate further,
and find a solution that will be able to reach our goal in linear time O(n).

A unit testing file is included along with the functions file. This tests some scenarios to vet the functions provided.