# Runs: 4
# R = 0.25

from scipy.stats import mannwhitneyu

# Veri kümeleri
A = [0.0040857, 0.0031189, 0.0031169, 0.0028766, 0.0030866, 0.0028734, 0.0032435, 0.0031782, 0.0032045, 0.0031646]
B = [0.0020949, 0.0023687, 0.0020721, 0.0019259, 0.0019855, 0.0019139, 0.0021185, 0.0021416, 0.0021333, 0.0020727]

# Mann-Whitney U testi
U, p_value = mannwhitneyu( A, B, alternative='two-sided' )

# Sonuçları göster
print( f'U Değeri: {U}' )
print( f'P Değeri: {p_value}' )

if (0.05 > p_value):
   print( 'OK' )
else:
   print( 'NOK' )
