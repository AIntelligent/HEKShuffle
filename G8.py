# Runs: 8
# R = 0.125
from scipy.stats import mannwhitneyu

# Veri kümeleri
A = [0.0032510, 0.0031165, 0.0029407, 0.0029475, 0.0029289, 0.0028779, 0.0029410, 0.0029305, 0.0029004, 0.0046911]
B = [0.0043227, 0.0024219, 0.0023629, 0.0022926, 0.0022216, 0.0024345, 0.0023033, 0.0022199, 0.0022211, 0.0022207]

# Mann-Whitney U testi
U, p_value = mannwhitneyu( A, B, alternative='two-sided' )

# Sonuçları göster
print( f'U Değeri: {U}' )
print( f'P Değeri: {p_value}' )

if (0.05 > p_value):
   print( 'OK' )
else:
   print( 'NOK' )
