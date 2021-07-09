getnPrimes :: Integral a => Int -> [a]
getnPrimes n = take n [i | i <- [2..], isPrime i == True]

sum_primes n = sum(getnPrimes n)

main = print(sum_primes 8)