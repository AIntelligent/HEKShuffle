# HEKShuffle
Performance Analysis of Fisher-Yates and HEK Shuffle Algorithms

For the analysis of the two algorithms, a non-random sequence adapted for the "Runs Test" consisting of 200,000 data points was used. Both sequences consist of 2, 4, and 8 Runs, and each Run is placed sequentially. The initial patterns of the sequences are as follows:

Let N denote the sequence size.
Runs 2: {0..0(N/2),1..1(N/2)}
Runs 4: {0..0(N/4),1..1(N/4),....,0..0(N/4),1..1(N/4)}
Runs 8: {0..0(N/8),1..1(N/8),....,0..0(N/8),1..1(N/8)}

The "Runs Test" was used for randomness analysis, and the "Mann-Whitney U Test" was used to compare performance data. The graphs related to the results are provided below:

