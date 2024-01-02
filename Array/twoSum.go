func twoSum(nums []int, target int) []int {
    numToIndexMap := map[int]int{}

    for i, num := range nums {
        if complementIndex, ok := numToIndexMap[target - num]; ok {
            return []int{i, complementIndex}
        }

        numToIndexMap[num] = i
    }

    return []int{}
}
