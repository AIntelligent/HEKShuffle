# Performance Analysis of Fisher-Yates and HEK Shuffle Algorithms

For the analysis of the two algorithms, a non-random sequence adapted for the "Runs Test" consisting of 200,000 data points was used. Both sequences consist of 2, 4, and 8 Runs, and each Run is placed sequentially. The initial patterns of the sequences are as follows:

Let N denote the sequence size.

  	Runs 2: {0..0(N/2),1..1(N/2)}
  	Runs 4: {0..0(N/4),1..1(N/4),....,0..0(N/4),1..1(N/4)}
  	Runs 8: {0..0(N/8),1..1(N/8),....,0..0(N/8),1..1(N/8)}

The "Runs Test" was used for randomness analysis, and the "Mann-Whitney U Test" was used to compare performance data. The graphs related to the results are provided below:

# Fisher-Yates ve HEK karıştırma algoritmalarının performans analizi.

İki algoritmanın analizi için 200.000 veriden oluşan "Runs Test" için uyarlanmış rastgele olmayan dizi kullanılmıştır. 
İki dizi de 2, 4 ve 8 Runs'tan oluşmakta ve her iki Run ardışık olarak yerleştirilmektedir. Dizilerin başlangıç desenleri
aşağıdadır:
	
N dizi boyutun göstermek üzere.
 
	Runs 2: {0..0(N/2),1..1(N/2)}
	Runs 4: {0..0(N/4),1..1(N/4),....,0..0(N/4),1..1(N/4)}
	Runs 8: {0..0(N/8),1..1(N/8),....,0..0(N/8),1..1(N/8)}
	
şeklindedir. Rastgelelik analizi için "Runs Test" ve performans verilerinin karşılaştırılması için "Mann-Whitney U Test" 
kullanılmıştır. Aşağıda sonuçlarla ilgili grafikler verilmiştir:

![FYHEK2](https://github.com/AIntelligent/MSDOS/blob/67b94596f017f2fb15260b0b2d160adae3821ca3/ANTI-CCC/screenshots/ANTI-CCC_1.PNG)
