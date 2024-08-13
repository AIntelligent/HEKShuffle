# Runs: 4
# R = 0.25

from scipy.stats import mannwhitneyu

# Veri kümeleri
A = [4004.6000000, 3089.2000000, 3376.2000000, 3107.7000000, 2989.4000000, 3286.6000000, 2846.8000000, 2858.1000000, 2842.9000000, 2886.7000000]
B = [2846.1000000, 2009.1000000, 2532.4000000, 2586.5000000, 2040.6000000, 2524.9000000, 1993.5000000, 1990.9000000, 2025.3000000, 1991.7000000]

# Mann-Whitney U testi
U, p_value = mannwhitneyu( A, B, alternative='two-sided' )

# Sonuçları göster
print( f'U Değeri: {U}' )
print( f'P Değeri: {p_value}' )

if (0.05 > p_value):
   print( 'OK' )
else:
   print( 'NOK' )
