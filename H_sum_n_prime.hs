

getnPrimes :: Integral a => Int -> [a]
getnPrimes n = take n [i | i <- [2..], isPrime i]

sum_primes n = sum(getnPrimes n)

main = print(sum_primes 8)