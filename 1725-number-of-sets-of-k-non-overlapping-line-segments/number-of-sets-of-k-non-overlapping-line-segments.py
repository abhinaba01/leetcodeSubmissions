class Solution:
    def numberOfSets(self, n: int, k: int) -> int:


        MOD = 10**9 + 7
        
        # We need to calculate C(n + k - 1, 2 * k)
        total_points = n + k - 1
        endpoints_needed = 2 * k
        
        # If we need more endpoints than available points, 0 ways
        if endpoints_needed > total_points:
            return 0
            
        # Calculate combination using modular inverse to avoid huge numbers
        numerator = 1
        denominator = 1
        
        for i in range(endpoints_needed):
            numerator = (numerator * (total_points - i)) % MOD
            denominator = (denominator * (i + 1)) % MOD
            
        # Fermat's Little Theorem for modular inverse: a^(-1) ≡ a^(MOD-2) mod MOD
        return (numerator * pow(denominator, MOD - 2, MOD)) % MOD

        


        
        