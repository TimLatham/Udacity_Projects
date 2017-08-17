/*:
 [Table of Contents](Table%20of%20Contents) | [Previous](@previous)
 ****
 */
import Foundation
//: ## Challenge
//: **This exercise is completely optional and is not required for completing the Swift Problem Set.**
//: ### Challenge 1
//: Mystery code! What does this code do? Briefly, using comments, describe what is happening in each line. **Hint**: You may need to look up [Int initializers](http://stackoverflow.com/questions/30739460/toint-removed-in-swift-2).
let array = ["A", "13", "B", "5", "87", "t", "41"] //creating an array of strings
var sum = 0 //initializing a "sum" variable to zero
for string in array { //looping through each item in the array
    if Int(string) != nil { //If the string can be converted to an Int type perform the following steps
        let intToAdd = Int(string)! //convert the string to an integer
        sum += intToAdd //add that integer to the current value of the sum variable
    }
}
print(sum) //print the total of 13 + 5 + 87 + 41, aka the strings that can convert to Int type
// It is looping through the array, and if an item can successfully be converted to an Int type
// it adds that amount to the cumulative sum, then prints the resulting total
/*:
 ****
 [Table of Contents](Table%20of%20Contents) | [Previous](@previous)
 */
