// Team Crispy Elevator :: Verit Li, Johnathan
// SoftDev pd7
// K27 -- Basic functions in JavaScript
// 2023-04-04t
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.

/*
(define fact (lambda (n)
    (if (< n 2)
        1
        (* n (fact (- n 1)))
    )
))
*/

function fact(n) {
    if (n < 2) {
        return 1
    }
    else { 
        return (n * (fact (n - 1)))
    }
}

//------------------------------------------

/*
(define fib (lambda (n)
    (if (= n 0)
        0
        (if (= n 1)
            1
            (+ (fib (- n 1)) (fib (- n 2)))
        )
    )
))
*/

function fib(n){
    if (n == 0) {
        return 0
    }
    else if (n == 1) {
        return 1
    }
    else {
        return fib(n - 1) + fib(n - 2)
    }

}

