func compress(chars []byte) int {
    if len(chars) <= 1 {
        return len(chars)
    }

    slow, fast := 0, 0
    var result []byte
    
    for fast < len(chars) {
        if chars[slow] != chars[fast] {
            result = append(result, chars[slow])

            count := fast - slow 
            if count > 1 {
                for _, digit := range strconv.Itoa(count) {
                    result = append(result, byte(digit))
                }
            }
            slow = fast
        }

        fast++
    }

    if slow <= fast - 1 {
        result = append(result, chars[slow])
        count := fast - slow 
        if count > 1 {
            for _, digit := range strconv.Itoa(count) {
                result = append(result, byte(digit))
            }
        }
    }

    for i := 0; i < len(result); i++ {
        chars[i] = result[i]
    }
    chars = chars[:len(result)]

    return len(result)
}
