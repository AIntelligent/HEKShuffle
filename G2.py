# Runs: 2
# R = 0.5

from scipy.stats import mannwhitneyu

# Veri kümeleri
A = [3576.5000000, 2865.0000000, 2624.9000000, 3149.1000000, 2720.5000000, 2624.3000000, 2997.3000000, 2674.2000000, 2893.4000000, 2887.2000000]
B = [1937.7000000, 1357.1000000, 1260.2000000, 1464.1000000, 1255.0000000, 1332.7000000, 1369.0000000, 1417.8000000, 1377.8000000, 1370.3000000]

# Mann-Whitney U testi
U, p_value = mannwhitneyu( A, B, alternative='two-sided' )

# Sonuçları göster
print( f'U Değeri: {U}' )
print( f'P Değeri: {p_value}' )

if (0.05 > p_value):
   print( 'OK' )
else:
   print( 'NOK' )
