open System.Collections.Generic
open System


////definicja listy łączonej 

//type LinkedList<'T> = 
     
//     | Empty
//     | Node of 'T * LinkedList<'T>


//let Head = 
//    function
//    |  Empty -> failwith "Nie można pobrać głowy z listy pustej"
//    |  Node(Head,_) -> Head


//let Tail =
//    function
//    | Empty -> failwith "Nie można pobrać ogona z listy pustej"
//    | Node(Head,_) -> Tail  


//let addHead value list =
//    Node(value, list)

//let rec printList list =
//    match list witch
//    | Empty ->()
//    | Node(Value, next) -> 
//        printf " %A " Value
//        printList next 


//let numberElements =
//   function
//   | Empty -> 0
//   | Node(_,Tail) -> numbersElements Tail + 1


//[<EntryPoint>]
//let main argv =
//    let list1 = Empty
//    let list2 = addHead 1 list1
//    let list3 = addHead 2 list2
//    let list4 = addHead 3 list3

//    printList list4

//    let ilosc = numberElements list4
//    printf "\n%d"  ilosc


//    0



//Zad1

//type LinkedList<'T> =     
//    | Empty
//    | Node of 'T * LinkedList<'T>

////moduł zawierajacy funkcje do zadan

//module LinkedList =

//    //utworzenie listy na podstawie elementów podanych od usera
//    let rec fromList = 
//        function
//        | [] -> Empty
//        | x :: xs -> Node(x, fromList xs)


////koniec modułu


////funckja do wczytywania elementow z klawiatury
//let rec redUserList()=
//    printf "Podaj elementy listy oddzielone spacją: "
//    let input = Console.ReadLine() //1 2 3 
//    let items =
//        input.Split(' ')
//        |> Array.choose (fun x->
//           match Int32.TryParse(x) with
//           |(true, v)_> Some v
//           |   -> None)
//        |> Array.toList 
//    LinkedList.fromList items




//[<EntryPoint>]
//let main argv =
//    let mutable userList = LinkedList.Empty

//    userList <- readUserList()


//    printf "n\elementy listy:\t
    



// 2. Funkcja sumująca elementy listy.
let sumList (lst: int list) =
    List.sum lst

// Przykład użycia dla zadania 2.
let exampleList = [1; 2; 3; 4; 5; 2; 1]
let sum = sumList exampleList
printfn "Sum: %d" sum

// 3. Funkcja znajdująca maksymalny i minimalny element w liście.
let findMinMax (lst: int list) =
    if List.isEmpty lst then
        None
    else
        Some (List.min lst, List.max lst)

// 4. Funkcja odwracająca kolejność elementów listy.
let reverseList (lst: 'a list) =
    List.rev lst

// 5. Funkcja sprawdzająca, czy dany element znajduje się w liście.
let containsElement (element: 'a) (lst: 'a list) =
    List.contains element lst

// 6. Funkcja określająca indeks podanego elementu.
type ElementIndex<'a> =
    | Found of int
    | NotFound

let findElementIndex (element: 'a) (lst: 'a list) =
    match List.tryFindIndex ((=) element) lst with
    | Some index -> Found index
    | None -> NotFound

// 7. Funkcja zliczająca, ile razy dany element występuje w liście.
let countOccurrences (element: 'a) (lst: 'a list) =
    List.filter ((=) element) lst |> List.length

// 8. Funkcja łącząca dwie listy.
let mergeLists (lst1: 'a list) (lst2: 'a list) =
    List.append lst1 lst2

// 9. Funkcja porównująca wartości dwóch list i zwracająca listę wartości logicznych.
let compareLists (lst1: int list) (lst2: int list) =
    if List.length lst1 <> List.length lst2 then
        failwith "Lists must be of the same length"
    else
        List.map2 (>) lst1 lst2

// 10. Funkcja zwracająca listę zawierającą tylko elementy spełniające określony warunek.
let filterList (predicate: 'a -> bool) (lst: 'a list) =
    List.filter predicate lst

// 11. Funkcja usuwająca duplikaty z listy.
let removeDuplicates (lst: 'a list) =
    List.distinct lst

// 12. Funkcja dzieląca listę na dwie części według warunku.
let partitionList (predicate: 'a -> bool) (lst: 'a list) =
    List.partition predicate lst

// Przykłady użycia dla pozostałych zadań:

// 3. Znajdowanie minimum i maksimum.
let minMax = findMinMax exampleList
printfn "Min and Max: %A" minMax

// 4. Odwracanie listy.
let reversed = reverseList exampleList
printfn "Reversed: %A" reversed

// 5. Sprawdzanie obecności elementu.
let contains = containsElement 3 exampleList
printfn "Contains 3: %b" contains

// 6. Znajdowanie indeksu elementu.
let index = findElementIndex 3 exampleList
printfn "Index of 3: %A" index

// 7. Zliczanie wystąpień elementu.
let count = countOccurrences 2 exampleList
printfn "Occurrences of 2: %d" count

// 8. Łączenie dwóch list.
let merged = mergeLists exampleList [6; 7; 8]
printfn "Merged: %A" merged

// 9. Porównywanie dwóch list.
try
    let comparisons = compareLists [1; 2; 3] [3; 2; 1]
    printfn "Comparisons: %A" comparisons
with
| ex -> printfn "Error: %s" ex.Message

// 10. Filtrowanie listy.
let filtered = filterList (fun x -> x > 2) exampleList
printfn "Filtered: %A" filtered

// 11. Usuwanie duplikatów.
let noDuplicates = removeDuplicates exampleList
printfn "No duplicates: %A" noDuplicates

// 12. Dzielenie listy według warunku.
let partitioned = partitionList (fun x -> x % 2 = 0) exampleList
printfn "Partitioned: %A" partitioned
