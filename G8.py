# Runs: 8
# R = 0.125
from scipy.stats import mannwhitneyu

# Veri kümeleri
A = [5538.1000000, 4299.0000000, 2849.2000000, 2836.6000000, 2852.6000000, 2622.0000000, 2889.3000000, 2922.1000000, 2843.2000000, 2862.5000000]
B = [3399.4000000, 2537.2000000, 2294.3000000, 2162.7000000, 2307.1000000, 2121.4000000, 2325.4000000, 2341.8000000, 2293.4000000, 2334.6000000]

# Mann-Whitney U testi
U, p_value = mannwhitneyu( A, B, alternative='two-sided' )

# Sonuçları göster
print( f'U Değeri: {U}' )
print( f'P Değeri: {p_value}' )

if (0.05 > p_value):
   print( 'OK' )
else:
   print( 'NOK' )
