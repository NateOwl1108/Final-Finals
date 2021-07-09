#include <iostream>

using namespace std;

bool isPrime(int n)
{
    // Corner case
    if (n <= 1)
        return false;
  
    // Check from 2 to n-1
    for (int i = 2; i < n; i++)
        if (n % i == 0)
            return false;
  
    return true;
}

int main() {

    int numprime_needed = 8;
    int num_primes = 0;
    int last_prime = 0;
    int sum = 0;




    while (num_primes < numprime_needed) 
    {

      for(int i = last_prime + 1; i <= 99999; i++) 
      {
        if (isPrime(i) == true)
        {
          last_prime = i;
          num_primes +=1;
          sum += i;
          cout << i << "\n";
          break;
        }
      }
          
        
    }
    cout <<sum;
    return 0;
}