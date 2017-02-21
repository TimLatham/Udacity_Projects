//: ## Defining a Struct
/*:
**To define a struct in Swift, the following syntax can be used:**

*struct NameOfStruct {*

  *\/\/ variables declarations (known as properties)...*

*}*
*/
struct Student {
    let name: String
    var age: Int
    var school: String
}

struct GeoLocation {
    var latitude: Double = 0.0
    var longitude: Double = 0.0
}

struct Point2D {
    var x: Int = 0
    var y: Int = 0
}
//: [Next](@next)
var ayush = Student(name: "Ayush Saraswat", age: 19, school: "Udacity")
var characterPosition = Point2D(x: 10, y: 10)
let udacityCoordinates = GeoLocation(latitude: 37.400073, longitude: -122.108400)
