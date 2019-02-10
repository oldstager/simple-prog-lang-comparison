package main

import (
    "bufio"
    "fmt"
    "os"
)

func main() {
    scn := bufio.NewScanner(os.Stdin)
 	var sum, count int
	for scn.Scan() {
    	line := scn.Text()
		sum += len(line)
		count += 1
    }
	fmt.Println("Average line length: ", float64(sum) / float64(count))
}
