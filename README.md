# FSCS-SIMD
Code for our paper:
[FSCS-SIMD: An efficient implementation of Fixed-Size-Candidate-Set adaptive random testing using SIMD instructions (Research Paper)](https://ieeexplore.ieee.org/document/9251093), Accepted in [The 31st International Symposium on Software Reliability Engineering (ISSRE 2020)](https://ieeexplore.ieee.org/xpl/conhome/9250925/proceeding)

DOI: [10.1109/ISSRE5003.2020.00034](https://doi.org/10.1109/ISSRE5003.2020.00034)
 
Description: A method to enhance the efficiency of FSCS-ART throught SIMD and Parallelization.

### Abstract:
The Fixed-Size-Candidate-Set (FSCS) version of Adaptive Random Testing (ART) attempts to enhance the fault detection effectiveness of Random Testing (RT) by generating new test cases that are far away from previously executed test cases. Despite its simplicity and good fault-detection effectiveness, FSCS suffers from a very high time cost mainly due to its Single-Instruction-Single-Data (SISD) mechanism for its distance calculation process. To overcome this drawback, in this paper, we propose a novel and efficient implementation of FSCS, namely Fixed-Sized-Candidate-Set using Single-Instruction-Multiple-Data (FSCS-SIMD), which employs SIMD instruction architecture for simultaneous distance calculations of multiple test cases in a many-to-many style. Compared with the original FSCS, our proposed method loads a batch of multiple test cases from the candidate test case set and executed test case set in one CPU execution cycle. After that, a single distance calculation instruction is given to the whole batch for the calculation of all pairwise distances. We conducted a series of simulations and empirical studies to evaluate testing effectiveness and efficiency of our proposed method against FSCS. Our results show that, on average, FSCS-SIMD reduces test case generation overhead of FSCS up to 90%, while maintaining the comparable fault detection effectiveness.


### Version 2.0 Updates

+ Maximum use of CPU cores with [FAISS](https://github.com/facebookresearch/faiss) library which is [highly optimized for SIMD](https://speakerdeck.com/matsui_528/cvpr20-tutorial-billion-scale-approximate-nearest-neighbor-search?slide=13). FAISS also has GPU version for further speed-up. However, we have used CPU-only version to keep the validity of comparisons. 

+ Further optimizations in code: FSCS original version, Random test case generator

### Evaluation
**Machine:** Dell Latitude E6430, Intel Core i5-3320M CPU @ 2.60GHz, 2 Cores, 4 Logical Processors, 6GB RAM running on Ubuntu 20.04 LTS 64-bit with Python 3.7 as the development environment. Ubuntu is selected because FAISS setup is easily supported on Linux.

#### CPU Core Usage:

##### FSCS-SIMD using NumPy
Although NumPy provided vectorization and parallelization ([link](https://stackoverflow.com/questions/44944367/are-numpys-basic-operations-vectorized-i-e-do-they-use-simd-operations)). However, parallelization regarding CPU core usage was not upto the mark. As shown following most of the processing was sitting on a single CPU core:
![alt text](results/FSCS-SIMD(NumPy).png "Title")

##### FSCS-SIMD using NumPy+FAISS
The below picture shows that all the CPU cores are used to achieve maximum level of parallelization. All 4 CPUs are being used:
![alt text](results/FSCS-SIMD(NumPy+FAISS).png "Title")

#### Results
In this way, we managed to reduce computational overhead of FSCS further:
![alt text](results/results.png "Title")


