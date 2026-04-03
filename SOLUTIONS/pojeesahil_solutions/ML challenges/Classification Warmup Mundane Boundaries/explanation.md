## My Approach 
First, I tried to visualize the data using matplotlib and making scatter plot
It almost look like it could be divided by single boundary and looking at dataset I got to know result was binary, so first i decided to go with **log Regression**(binary linear classifier), implementing it got me 95% accuracy then i notice that scatterplot is not exactly linear, there are some curves too so i decided to go with non linear classifier, random forest classifier gave 96% accuracy while SVC gave me 98% accuracy so i settled down with **SVC**.
<img width="800" height="600" alt="datapic1" src="https://github.com/user-attachments/assets/3de53f6a-00a6-470e-8c40-3a363deb3358" />


**Accuracy Score: 0.98**

---
### Classification Report:
---

| Class | Precision | Recall | F1-Score | Support |
| :--- | :--- | :--- | :--- | :--- |
| **0** | 0.97 | 1.00 | 0.98 | 57 |
| **1** | 1.00 | 0.95 | 0.98 | 43 |
| **Accuracy** | | | **0.98** | **100** |
| **Macro Avg** | 0.98 | 0.98 | 0.98 | 100 |
| **Weighted Avg** | 0.98 | 0.98 | 0.98 | 100 |


         
