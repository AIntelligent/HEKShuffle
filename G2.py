# Runs: 2
# R = 0.5

from scipy.stats import mannwhitneyu

# Veri kümeleri
A = [0.0031553, 0.0031815, 0.0031124, 0.0029904, 0.0029213, 0.0033500, 0.0030946, 0.0028759, 0.0031586, 0.0028739]
B = [0.0014084, 0.0014285, 0.0013923, 0.0012862, 0.0013294, 0.0012860, 0.0013181, 0.0012873, 0.0012878, 0.0012855]

# Mann-Whitney U testi
U, p_value = mannwhitneyu( A, B, alternative='two-sided' )

# Sonuçları göster
print( f'U Değeri: {U}' )
print( f'P Değeri: {p_value}' )

if (0.05 > p_value):
   print( 'OK' )
else:
   print( 'NOK' )
