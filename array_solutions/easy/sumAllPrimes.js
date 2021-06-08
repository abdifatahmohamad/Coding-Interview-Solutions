// Pass in a number to loop up to and add all of the prime numbers
// ex. sumAllPrimes(10) ==> 17

// Prime numbers are natural numbers that are divisible by exactly 2 natural numbers with NO remainder
// Those 2 exactly numbers are: #1 and itself
// ex. 3 is divisible by 1 and itself

function sumAllPrimes(num){
    let total = 0;

    // Helper function to check if the number is prime:
    function checkForPrime(n){
        for(let i=2; i<n; i++){
            if(n % i == 0){
                return false;
            }
        }
        return true;
    }

    for(let j=2; j<=num; j++){
        if(checkForPrime(j)){
            total += j;
        }
    }
    return total;
}

console.log(sumAllPrimes(10));
// sumAllPrimes();