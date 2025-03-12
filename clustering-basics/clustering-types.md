# Clustering Overview

## 1️⃣ Types of Clustering
- **Flat (Partition-based) Clustering**  
- **Hierarchical Clustering**  

---

## 2️⃣ Flat (Partition-based) Clustering  
### ➜ Directly divides data into `k` clusters, no hierarchy.  

### 🔹 Common Algorithms:
- **K-Means** (Centroid-based, iterative)  
- **K-Medoids (PAM)** (Like K-Means but uses actual data points as centers)  
- **Gaussian Mixture Models (GMM)** (Soft clustering using probability distributions)  
- **DBSCAN** (Density-based, detects outliers, does not require `k`)  
- **OPTICS** (Improved DBSCAN for varying densities)  
- **Mean-Shift** (Finds dense areas using kernel density estimation)  
- **Affinity Propagation** (Message-passing between points, no `k` needed)  
- **Spectral Clustering** (Graph-based, useful for complex shapes)  

---

## 3️⃣ Hierarchical Clustering  
### ➜ Creates a tree-like structure (dendrogram).  

### 🔹 Types:
- **Agglomerative (Bottom-up merging)**  
- **Divisive (Top-down splitting)**  

### 🔹 Agglomerative Clustering Methods (Ways to Merge Clusters):
- **Single Linkage** (Min distance between clusters)  
- **Complete Linkage** (Max distance between clusters)  
- **Average Linkage** (Mean distance)  
- **Centroid Linkage** (Distance between centroids)  
- **Median Linkage** (Like centroid but uses median)  
- **Ward’s Method** (Minimizes variance)  

### 🔹 Distance Metrics (Ways to Calculate Distance):  
- **Euclidean Distance**  
- **Manhattan Distance**  
- **Maximum (Chebyshev) Distance**  
- **Mahalanobis Distance**  
- **Cosine Similarity (for text data)**  

---

## 4️⃣ Supervised vs. Unsupervised Learning  
- **Clustering is always Unsupervised Learning** 🚀  
- Supervised Learning (Classification & Regression) deals with labeled data.  

---

### **🎯 TL;DR**
- If it's **flat clustering** → Think **K-Means, GMM, DBSCAN, etc.**  
- If it's **hierarchical** → Think **Agglomerative & Divisive**  
- If it's **density-based** → Think **DBSCAN, OPTICS**  
- If it's **graph-based** → Think **Spectral Clustering**  

Now you can categorize any clustering method you come across! 💡✨  
