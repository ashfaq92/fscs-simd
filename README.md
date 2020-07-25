# FSCS-SIMD

Description will be provided soon


###Version 2.0 Updates

Maximum use of CPU cores with FAISS library which is highly optimized for SIMD.

Other Optimizations 


###Results
**Machine:** Dell Latitude E6430, Intel Core i5-3320M CPU @ 2.60GHz, 2 Cores, 4 Logical Processors, 6GB RAM running on Ubuntu 20.04 LTS 64-bit with Python 3.7 as the development environment. Ubuntu is selected because FAISS setup is easily supported on Linux.

####CPU Core Usage:

#####FSCS-SIMD using NumPy
Although NumPy provided vectorization and parallelization. However, parallelization regarding CPU core usage was not upto the mark. As shown following:

#####FSCS-SIMD using NumPy+FAISS
The below picture shows that all the CPU cores are used to achieve maximum level of parallelization. All 4 CPUs are being used:

#####Results
In this way, we managed to reduce computational efficiency of FSCS further:

