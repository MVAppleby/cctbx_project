from __future__ import division
import iotbx.ncs
import iotbx.ncs as ncs
from iotbx import pdb

pdb_str_1="""\
ATOM      1  N   GLU A   3     189.385 151.249 151.584  1.00100.71           N
ATOM      2  CA  GLU A   3     190.604 152.017 151.807  1.00100.71           C
ATOM      3  C   GLU A   3     191.582 151.843 150.650  1.00100.71           C
ATOM      4  O   GLU A   3     191.527 150.846 149.929  1.00100.71           O
ATOM      5  CB  GLU A   3     191.266 151.602 153.123  1.00 81.32           C
ATOM      6  N   LYS A   4     192.471 152.820 150.489  1.00113.71           N
ATOM      7  CA  LYS A   4     193.464 152.823 149.414  1.00113.71           C
ATOM      8  C   LYS A   4     192.807 152.666 148.045  1.00113.71           C
ATOM      9  O   LYS A   4     191.719 153.194 147.810  1.00113.71           O
ATOM     10  CB  LYS A   4     194.500 151.716 149.633  1.00 74.77           C
ATOM     11  N   ARG A   5     193.479 151.939 147.155  1.00126.03           N
ATOM     12  CA  ARG A   5     192.989 151.690 145.800  1.00126.03           C
ATOM     13  C   ARG A   5     192.651 152.988 145.072  1.00126.03           C
ATOM     14  O   ARG A   5     191.677 153.056 144.321  1.00126.03           O
ATOM     15  CB  ARG A   5     191.763 150.772 145.832  1.00 91.24           C
ATOM     16  N   LEU A   6     193.465 154.014 145.302  1.00134.86           N
ATOM     17  CA  LEU A   6     193.232 155.328 144.718  1.00126.46           C
ATOM     18  C   LEU A   6     193.464 155.328 143.211  1.00118.31           C
ATOM     19  O   LEU A   6     194.543 154.966 142.738  1.00116.86           O
ATOM     20  CB  LEU A   6     194.129 156.372 145.384  1.00128.29           C
ATOM     21  N   SER A   7     192.446 155.734 142.460  1.00127.84           N
ATOM     22  CA  SER A   7     192.556 155.843 141.011  1.00123.16           C
ATOM     23  C   SER A   7     193.118 157.206 140.626  1.00118.42           C
ATOM     24  O   SER A   7     192.423 158.219 140.706  1.00104.49           O
ATOM     25  CB  SER A   7     191.195 155.625 140.347  1.00121.63           C
ATOM     26  OG  SER A   7     190.259 156.601 140.769  1.00106.82           O
ATOM     27  N   ALA A   8     194.380 157.227 140.210  1.00118.32           N
ATOM     28  CA  ALA A   8     195.053 158.483 139.901  1.00111.32           C
ATOM     29  C   ALA A   8     195.632 158.502 138.491  1.00106.60           C
ATOM     30  O   ALA A   8     195.140 159.230 137.629  1.00102.40           O
ATOM     31  CB  ALA A   8     196.149 158.752 140.922  1.00102.52           C
ATOM     32  N   LYS A   9     196.672 157.693 138.277  1.00107.25           N
ATOM     33  CA  LYS A   9     197.479 157.673 137.046  1.00101.87           C
ATOM     34  C   LYS A   9     197.684 159.066 136.442  1.00 99.64           C
ATOM     35  O   LYS A   9     197.682 159.240 135.222  1.00 96.65           O
ATOM     36  CB  LYS A   9     196.865 156.721 136.003  1.00116.20           C
ATOM     37  CG  LYS A   9     195.479 157.086 135.482  1.00116.20           C
ATOM     38  CD  LYS A   9     195.039 156.146 134.370  1.00116.20           C
ATOM     39  CE  LYS A   9     194.946 154.712 134.860  1.00116.20           C
ATOM     40  NZ  LYS A   9     194.513 153.782 133.781  1.00116.20           N
ATOM     41  N   LYS A  10     197.886 160.050 137.313  1.00105.36           N
ATOM     42  CA  LYS A  10     198.013 161.443 136.902  1.00 98.00           C
ATOM     43  C   LYS A  10     199.366 161.728 136.262  1.00100.41           C
ATOM     44  O   LYS A  10     200.353 161.046 136.539  1.00103.97           O
ATOM     45  CB  LYS A  10     197.802 162.367 138.102  1.00106.11           C
ATOM     46  CG  LYS A  10     198.764 162.114 139.252  1.00113.17           C
ATOM     47  CD  LYS A  10     198.481 163.034 140.428  1.00110.08           C
ATOM     48  CE  LYS A  10     199.445 162.775 141.574  1.00119.94           C
ATOM     49  NZ  LYS A  10     199.358 161.373 142.069  1.00128.24           N
TER
ATOM     50  N   GLU B   3     159.932 134.609 151.533  1.00114.47           N
ATOM     51  CA  GLU B   3     161.039 133.685 151.754  1.00114.47           C
ATOM     52  C   GLU B   3     161.174 132.703 150.594  1.00114.47           C
ATOM     53  O   GLU B   3     160.207 132.450 149.874  1.00114.47           O
ATOM     54  CB  GLU B   3     160.850 132.926 153.068  1.00 84.70           C
ATOM     55  N   LYS B   4     162.377 132.158 150.430  1.00120.40           N
ATOM     56  CA  LYS B   4     162.683 131.217 149.354  1.00120.40           C
ATOM     57  C   LYS B   4     162.331 131.796 147.986  1.00120.40           C
ATOM     58  O   LYS B   4     162.498 132.994 147.754  1.00120.40           O
ATOM     59  CB  LYS B   4     161.949 129.891 149.570  1.00 79.41           C
ATOM     60  N   ARG B   5     161.843 130.935 147.095  1.00131.79           N
ATOM     61  CA  ARG B   5     161.454 131.328 145.741  1.00131.79           C
ATOM     62  C   ARG B   5     162.586 132.049 145.013  1.00131.79           C
ATOM     63  O   ARG B   5     162.351 132.998 144.265  1.00131.79           O
ATOM     64  CB  ARG B   5     160.204 132.212 145.776  1.00 94.80           C
ATOM     65  N   LEU B   6     163.811 131.590 145.241  1.00136.38           N
ATOM     66  CA  LEU B   6     164.990 132.218 144.659  1.00127.98           C
ATOM     67  C   LEU B   6     165.062 131.999 143.151  1.00119.83           C
ATOM     68  O   LEU B   6     165.053 130.863 142.677  1.00118.38           O
ATOM     69  CB  LEU B   6     166.259 131.684 145.325  1.00129.41           C
ATOM     70  N   SER B   7     165.131 133.095 142.403  1.00127.99           N
ATOM     71  CA  SER B   7     165.270 133.027 140.954  1.00123.31           C
ATOM     72  C   SER B   7     166.741 132.912 140.572  1.00118.57           C
ATOM     73  O   SER B   7     167.493 133.882 140.667  1.00104.64           O
ATOM     74  CB  SER B   7     164.644 134.257 140.292  1.00117.80           C
ATOM     75  OG  SER B   7     165.285 135.447 140.717  1.00102.99           O
ATOM     76  N   ALA B   8     167.147 131.722 140.141  1.00124.82           N
ATOM     77  CA  ALA B   8     168.549 131.469 139.833  1.00117.82           C
ATOM     78  C   ALA B   8     168.746 130.925 138.421  1.00113.10           C
ATOM     79  O   ALA B   8     169.288 131.619 137.560  1.00108.90           O
ATOM     80  CB  ALA B   8     169.143 130.509 140.852  1.00108.04           C
ATOM     81  N   LYS B   9     168.295 129.687 138.206  1.00118.88           N
ATOM     82  CA  LYS B   9     168.523 128.914 136.975  1.00113.50           C
ATOM     83  C   LYS B   9     169.913 129.148 136.371  1.00111.27           C
ATOM     84  O   LYS B   9     170.076 129.209 135.151  1.00108.28           O
ATOM     85  CB  LYS B   9     167.429 129.207 135.932  1.00136.65           C
ATOM     86  CG  LYS B   9     167.347 130.639 135.415  1.00136.65           C
ATOM     87  CD  LYS B   9     166.317 130.771 134.304  1.00136.65           C
ATOM     88  CE  LYS B   9     164.925 130.416 134.796  1.00136.65           C
ATOM     89  NZ  LYS B   9     163.904 130.545 133.719  1.00136.65           N
ATOM     90  N   LYS B  10     170.911 129.255 137.242  1.00117.26           N
ATOM     91  CA  LYS B  10     172.276 129.563 136.831  1.00109.90           C
ATOM     92  C   LYS B  10     172.964 128.366 136.185  1.00112.31           C
ATOM     93  O   LYS B  10     172.620 127.216 136.458  1.00115.87           O
ATOM     94  CB  LYS B  10     173.091 130.044 138.033  1.00114.70           C
ATOM     95  CG  LYS B  10     173.145 129.047 139.180  1.00121.76           C
ATOM     96  CD  LYS B  10     173.936 129.596 140.357  1.00118.67           C
ATOM     97  CE  LYS B  10     173.984 128.597 141.501  1.00128.53           C
ATOM     98  NZ  LYS B  10     172.623 128.251 141.996  1.00136.83           N
TER
ATOM     99  N   GLU C   3     135.020 157.489 151.546  1.00 97.12           N
ATOM    100  CA  GLU C   3     134.486 156.151 151.769  1.00 97.12           C
ATOM    101  C   GLU C   3     133.592 155.717 150.612  1.00 97.12           C
ATOM    102  O   GLU C   3     133.050 156.556 149.891  1.00 97.12           O
ATOM    103  CB  GLU C   3     133.707 156.096 153.084  1.00 78.85           C
ATOM    104  N   LYS C   4     133.446 154.403 150.449  1.00109.02           N
ATOM    105  CA  LYS C   4     132.646 153.820 149.375  1.00109.02           C
ATOM    106  C   LYS C   4     133.085 154.333 148.006  1.00109.02           C
ATOM    107  O   LYS C   4     134.276 154.544 147.772  1.00109.02           O
ATOM    108  CB  LYS C   4     131.157 154.106 149.593  1.00 74.21           C
ATOM    109  N   ARG C   5     132.114 154.528 147.117  1.00123.74           N
ATOM    110  CA  ARG C   5     132.365 155.018 145.760  1.00123.74           C
ATOM    111  C   ARG C   5     133.399 154.165 145.034  1.00123.74           C
ATOM    112  O   ARG C   5     134.229 154.680 144.283  1.00123.74           O
ATOM    113  CB  ARG C   5     132.819 156.480 145.794  1.00 88.74           C
ATOM    114  N   LEU C   6     133.343 152.857 145.263  1.00134.34           N
ATOM    115  CA  LEU C   6     134.303 151.929 144.680  1.00125.94           C
ATOM    116  C   LEU C   6     134.118 151.794 143.172  1.00117.79           C
ATOM    117  O   LEU C   6     133.035 151.448 142.699  1.00116.34           O
ATOM    118  CB  LEU C   6     134.187 150.557 145.347  1.00128.27           C
ATOM    119  N   SER C   7     135.180 152.070 142.425  1.00122.42           N
ATOM    120  CA  SER C   7     135.159 151.916 140.975  1.00117.74           C
ATOM    121  C   SER C   7     135.505 150.483 140.593  1.00113.00           C
ATOM    122  O   SER C   7     136.662 150.071 140.680  1.00 99.07           O
ATOM    123  CB  SER C   7     136.133 152.893 140.314  1.00118.03           C
ATOM    124  OG  SER C   7     137.463 152.652 140.736  1.00103.22           O
ATOM    125  N   ALA C   8     134.499 149.725 140.169  1.00116.62           N
ATOM    126  CA  ALA C   8     134.694 148.314 139.861  1.00109.62           C
ATOM    127  C   ALA C   8     134.235 147.958 138.451  1.00104.90           C
ATOM    128  O   ALA C   8     135.061 147.658 137.588  1.00100.70           O
ATOM    129  CB  ALA C   8     133.968 147.451 140.881  1.00105.20           C
ATOM    130  N   LYS C   9     132.918 148.001 138.237  1.00110.41           N
ATOM    131  CA  LYS C   9     132.253 147.544 137.008  1.00105.03           C
ATOM    132  C   LYS C   9     132.904 146.294 136.405  1.00102.80           C
ATOM    133  O   LYS C   9     133.005 146.153 135.186  1.00 99.81           O
ATOM    134  CB  LYS C   9     132.189 148.673 135.963  1.00112.95           C
ATOM    135  CG  LYS C   9     133.525 149.191 135.441  1.00112.95           C
ATOM    136  CD  LYS C   9     133.328 150.209 134.328  1.00112.95           C
ATOM    137  CE  LYS C   9     132.560 151.424 134.819  1.00112.95           C
ATOM    138  NZ  LYS C   9     132.363 152.431 133.739  1.00112.95           N
ATOM    139  N   LYS C  10     133.322 145.383 137.277  1.00110.13           N
ATOM    140  CA  LYS C  10     134.037 144.180 136.866  1.00102.77           C
ATOM    141  C   LYS C  10     133.111 143.155 136.226  1.00105.18           C
ATOM    142  O   LYS C  10     131.911 143.125 136.504  1.00108.74           O
ATOM    143  CB  LYS C  10     134.751 143.556 138.067  1.00111.37           C
ATOM    144  CG  LYS C  10     133.823 143.193 139.216  1.00118.43           C
ATOM    145  CD  LYS C  10     134.592 142.612 140.391  1.00115.34           C
ATOM    146  CE  LYS C  10     133.659 142.253 141.535  1.00125.20           C
ATOM    147  NZ  LYS C  10     132.907 143.438 142.032  1.00133.50           N
TER
ATOM    148  N   GLU D   3     149.071 188.264 151.543  1.00111.15           N
ATOM    149  CA  GLU D   3     147.633 188.359 151.765  1.00111.15           C
ATOM    150  C   GLU D   3     146.945 189.074 150.607  1.00111.15           C
ATOM    151  O   GLU D   3     147.575 189.848 149.885  1.00111.15           O
ATOM    152  CB  GLU D   3     147.340 189.084 153.079  1.00 85.33           C
ATOM    153  N   LYS D   4     145.651 188.806 150.445  1.00121.08           N
ATOM    154  CA  LYS D   4     144.847 189.386 149.369  1.00121.08           C
ATOM    155  C   LYS D   4     145.471 189.125 148.001  1.00121.08           C
ATOM    156  O   LYS D   4     146.041 188.058 147.767  1.00121.08           O
ATOM    157  CB  LYS D   4     144.659 190.890 149.587  1.00 80.08           C
ATOM    158  N   ARG D   5     145.357 190.109 147.110  1.00127.58           N
ATOM    159  CA  ARG D   5     145.900 190.021 145.755  1.00127.58           C
ATOM    160  C   ARG D   5     145.409 188.771 145.027  1.00127.58           C
ATOM    161  O   ARG D   5     146.157 188.143 144.278  1.00127.58           O
ATOM    162  CB  ARG D   5     147.431 190.042 145.788  1.00 92.50           C
ATOM    163  N   LEU D   6     144.148 188.421 145.256  1.00133.20           N
ATOM    164  CA  LEU D   6     143.564 187.219 144.673  1.00124.80           C
ATOM    165  C   LEU D   6     143.376 187.355 143.166  1.00116.65           C
ATOM    166  O   LEU D   6     142.718 188.282 142.693  1.00115.20           O
ATOM    167  CB  LEU D   6     142.224 186.904 145.341  1.00123.11           C
ATOM    168  N   SER D   7     143.963 186.427 142.417  1.00122.44           N
ATOM    169  CA  SER D   7     143.809 186.402 140.968  1.00117.76           C
ATOM    170  C   SER D   7     142.553 185.629 140.584  1.00113.02           C
ATOM    171  O   SER D   7     142.520 184.401 140.668  1.00 99.09           O
ATOM    172  CB  SER D   7     145.040 185.778 140.305  1.00114.82           C
ATOM    173  OG  SER D   7     145.223 184.439 140.728  1.00100.01           O
ATOM    174  N   ALA D   8     141.521 186.352 140.164  1.00110.90           N
ATOM    175  CA  ALA D   8     140.239 185.731 139.856  1.00103.90           C
ATOM    176  C   ALA D   8     139.759 186.055 138.445  1.00 99.18           C
ATOM    177  O   ALA D   8     139.729 185.175 137.584  1.00 94.98           O
ATOM    178  CB  ALA D   8     139.193 186.157 140.876  1.00100.30           C
ATOM    179  N   LYS D   9     139.393 187.321 138.229  1.00101.28           N
ATOM    180  CA  LYS D   9     138.753 187.810 136.999  1.00 95.90           C
ATOM    181  C   LYS D   9     137.768 186.804 136.395  1.00 93.67           C
ATOM    182  O   LYS D   9     137.670 186.658 135.176  1.00 90.68           O
ATOM    183  CB  LYS D   9     139.808 188.219 135.955  1.00108.30           C
ATOM    184  CG  LYS D   9     140.718 187.109 135.437  1.00108.30           C
ATOM    185  CD  LYS D   9     141.626 187.610 134.325  1.00108.30           C
ATOM    186  CE  LYS D   9     142.544 188.716 134.815  1.00108.30           C
ATOM    187  NZ  LYS D   9     143.443 189.213 133.736  1.00108.30           N
ATOM    188  N   LYS D  10     137.023 186.128 137.267  1.00 96.18           N
ATOM    189  CA  LYS D  10     136.102 185.076 136.857  1.00 88.82           C
ATOM    190  C   LYS D  10     134.841 185.639 136.213  1.00 91.23           C
ATOM    191  O   LYS D  10     134.442 186.771 136.486  1.00 94.79           O
ATOM    192  CB  LYS D  10     135.729 184.206 138.058  1.00 88.01           C
ATOM    193  CG  LYS D  10     135.099 184.979 139.206  1.00 95.07           C
ATOM    194  CD  LYS D  10     134.786 184.070 140.383  1.00 91.98           C
ATOM    195  CE  LYS D  10     134.160 184.848 141.529  1.00101.84           C
ATOM    196  NZ  LYS D  10     135.058 185.930 142.023  1.00110.14           N
TER
ATOM    197  N   GLU E   3     182.665 184.397 151.568  1.00101.17           N
ATOM    198  CA  GLU E   3     182.312 185.794 151.790  1.00101.17           C
ATOM    199  C   GLU E   3     182.779 186.669 150.633  1.00101.17           C
ATOM    200  O   GLU E   3     183.711 186.309 149.911  1.00101.17           O
ATOM    201  CB  GLU E   3     182.910 186.296 153.105  1.00 79.37           C
ATOM    202  N   LYS E   4     182.124 187.817 150.471  1.00110.10           N
ATOM    203  CA  LYS E   4     182.429 188.761 149.395  1.00110.10           C
ATOM    204  C   LYS E   4     182.375 188.087 148.027  1.00110.10           C
ATOM    205  O   LYS E   4     181.536 187.216 147.793  1.00110.10           O
ATOM    206  CB  LYS E   4     183.802 189.404 149.613  1.00 77.29           C
ATOM    207  N   ARG E   5     183.275 188.499 147.136  1.00120.36           N
ATOM    208  CA  ARG E   5     183.360 187.955 145.781  1.00120.36           C
ATOM    209  C   ARG E   5     182.020 188.037 145.053  1.00120.36           C
ATOM    210  O   ARG E   5     181.654 187.131 144.304  1.00120.36           O
ATOM    211  CB  ARG E   5     183.852 186.505 145.814  1.00 88.94           C
ATOM    212  N   LEU E   6     181.298 189.128 145.281  1.00129.21           N
ATOM    213  CA  LEU E   6     179.976 189.314 144.698  1.00120.81           C
ATOM    214  C   LEU E   6     180.049 189.534 143.190  1.00112.66           C
ATOM    215  O   LEU E   6     180.727 190.446 142.718  1.00111.21           O
ATOM    216  CB  LEU E   6     179.263 190.492 145.364  1.00125.07           C
ATOM    217  N   SER E   7     179.346 188.691 142.442  1.00122.90           N
ATOM    218  CA  SER E   7     179.276 188.827 140.992  1.00118.22           C
ATOM    219  C   SER E   7     178.153 189.782 140.606  1.00113.48           C
ATOM    220  O   SER E   7     176.975 189.433 140.684  1.00 99.55           O
ATOM    221  CB  SER E   7     179.064 187.463 140.330  1.00118.74           C
ATOM    222  OG  SER E   7     177.846 186.876 140.753  1.00103.93           O
ATOM    223  N   ALA E   8     178.522 190.989 140.191  1.00119.02           N
ATOM    224  CA  ALA E   8     177.536 192.016 139.881  1.00112.02           C
ATOM    225  C   ALA E   8     177.696 192.572 138.470  1.00107.30           C
ATOM    226  O   ALA E   8     176.851 192.329 137.609  1.00103.10           O
ATOM    227  CB  ALA E   8     177.617 193.143 140.901  1.00107.03           C
ATOM    228  N   LYS E   9     178.787 193.311 138.255  1.00112.72           N
ATOM    229  CA  LYS E   9     179.055 194.071 137.025  1.00107.34           C
ATOM    230  C   LYS E   9     177.794 194.698 136.420  1.00105.11           C
ATOM    231  O   LYS E   9     177.627 194.746 135.201  1.00102.12           O
ATOM    232  CB  LYS E   9     179.771 193.193 135.981  1.00119.28           C
ATOM    233  CG  LYS E   9     178.996 191.986 135.462  1.00119.28           C
ATOM    234  CD  LYS E   9     179.753 191.277 134.350  1.00119.28           C
ATOM    235  CE  LYS E   9     181.089 190.746 134.841  1.00119.28           C
ATOM    236  NZ  LYS E   9     181.840 190.046 133.762  1.00119.28           N
ATOM    237  N   LYS E  10     176.921 195.194 137.291  1.00111.63           N
ATOM    238  CA  LYS E  10     175.636 195.745 136.880  1.00104.27           C
ATOM    239  C   LYS E  10     175.782 197.120 136.237  1.00106.68           C
ATOM    240  O   LYS E  10     176.736 197.848 136.513  1.00110.24           O
ATOM    241  CB  LYS E  10     174.691 195.831 138.080  1.00108.19           C
ATOM    242  CG  LYS E  10     175.230 196.669 139.229  1.00115.25           C
ATOM    243  CD  LYS E  10     174.268 196.685 140.406  1.00112.16           C
ATOM    244  CE  LYS E  10     174.812 197.522 141.551  1.00122.02           C
ATOM    245  NZ  LYS E  10     176.119 197.005 142.046  1.00130.32           N
TER
HETATM  246 MG    MG A 401     195.263 159.228 130.323  1.00 89.18          MG
HETATM  247 MG    MG A 402     190.491 155.655 128.902  1.00 58.96          MG
TER
HETATM  248 MG    MG B 401     169.312 131.516 130.255  1.00 89.18          MG
HETATM  249 MG    MG B 402     164.437 134.951 128.844  1.00 58.96          MG
TER
HETATM  250 MG    MG C 401     134.961 147.586 130.281  1.00 89.18          MG
HETATM  251 MG    MG C 402     136.700 153.281 128.869  1.00 58.96          MG
TER
HETATM  252 MG    MG E 402     178.823 186.803 128.888  1.00 58.96          MG
TER
HETATM  253 MG    MG D 401     139.639 185.244 130.278  1.00 89.18          MG
TER
HETATM  254 MG    MG E 501     163.180 163.256 210.123  1.00 53.90          MG
TER
HETATM  255 MG    MG D 402     145.597 185.342 128.864  1.00 58.96          MG
TER
HETATM  256 MG    MG E 502     163.175 163.242 206.503  1.00 53.90          MG
HETATM  257 MG    MG E 401     176.892 192.439 130.302  1.00 89.18          MG
HETATM  258 MG    MG E 503     163.118 163.159 156.463  1.00 53.90          MG
TER
"""

def exercise_00():
  """ Verify that strangely broken chain does not lead to crash """
  pdb_inp = iotbx.pdb.input(lines=pdb_str_1,source_info=None)
  hierarchy = pdb_inp.construct_hierarchy()
  ncs_inp = iotbx.ncs.input(hierarchy = hierarchy)
  ncs_groups = ncs_inp.get_ncs_restraints_group_list()
  assert len(ncs_groups) == 1
  assert len(ncs_groups[0].copies) == 3, len(ncs_groups[0].copies)
  assert ncs_groups[0].master_iselection.size() == 51 # all chain
  assert ncs_groups[0].copies[0].iselection.size() == 51 # all chain
  print "OK"

if(__name__=='__main__'):
  exercise_00()
