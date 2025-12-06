# Cisc121 Project - Bubble Sort 

**Demo Screenshots**

**Image 1: Input numbers**
<img width="1617" height="664" alt="image" src="https://github.com/user-attachments/assets/23f288be-c641-430a-b5d9-84fe1a3f8c63" />
**Image 2: Running Bubble Sort in steps**
<img width="1136" height="679" alt="image" src="https://github.com/user-attachments/assets/14e74d2f-644c-43bd-bb31-68381e3c8312" />
**Image 3: Final and sorted result**
<img width="1111" height="531" alt="image" src="https://github.com/user-attachments/assets/b8bcba97-7963-403e-b260-31b6307ab929" />

**Edge Cases**

**1. Empty Input**
<img width="915" height="422" alt="image" src="https://github.com/user-attachments/assets/167573a8-08a1-411d-b5b9-bba732fe76c0" />

**2. Single Input**
<img width="996" height="574" alt="image" src="https://github.com/user-attachments/assets/50f03fd0-b0aa-48ac-955c-bdc94e60a377" />

**3. Negative Numbers**
<img width="920" height="485" alt="image" src="https://github.com/user-attachments/assets/ac33ee95-52ba-4e17-a036-8c303b716582" />

**4. Reverse Ordered List**
<img width="896" height="222" alt="image" src="https://github.com/user-attachments/assets/4c9a0464-943b-46d3-89c2-1e6365f87a39" />
<img width="943" height="490" alt="image" src="https://github.com/user-attachments/assets/e2fee9bc-563d-4a8f-8eb5-4b9b3b4aad4a" />




**Problem Breakdown**

The goal is to build a tool that takes a list of numbers, performs bubble sort, and shows each step of the sorting process visually


**Computational Thinking**

Decomposition: Parse the user’s list of numbers, implement bubble sort, Capture each comparison state, Display results step-by-step in the UI

Pattern Recognition: Bubble sort repeatedly compares adjacent elements, If one is larger than the next → swap, each pass pushes the largest remaining element to the end. Detect patterns like: no swaps → the list is already sorted

Abstraction: Ignore unnecessary details (e.g., machine-level operations) Focus only on: Current index, elements being compared, whether a swap happened, the updated state of the list

Algorithm Design: Loop through the list multiple times, compare each adjacent pair, swap when needed, stop early if no swaps occurred, record each state so Streamlit can visualize the steps


**Steps to run**
1. Open hugging face and go to "App" section
2. Enter Numbers one by one spaced with a comma (eg. 6,7,6,7,1,2,3,)
3. Click "Run Bubble Sort"
4. Scroll and see the passes and final product


**Hugging Face link:**
https://huggingface.co/spaces/anishkatarina0202/runplease

**Author & Acknowledgment**
This project was created by Anish Kataria and was made using Streamlit and Python 









