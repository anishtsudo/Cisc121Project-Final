# Cisc121 Project - Bubble Sort 

**Demo Screenshots**

**Image 1: Input numbers**
<img width="1617" height="664" alt="image" src="https://github.com/user-attachments/assets/23f288be-c641-430a-b5d9-84fe1a3f8c63" />
**Image 2: Running Bubble Sort in steps**
<img width="1136" height="679" alt="image" src="https://github.com/user-attachments/assets/14e74d2f-644c-43bd-bb31-68381e3c8312" />
**Image 3: Final and sorted result**
<img width="1111" height="531" alt="image" src="https://github.com/user-attachments/assets/b8bcba97-7963-403e-b260-31b6307ab929" />


**Problem Breakdown**

The goal is to build a tool that takes a list of numbers, performs bubble sort, and shows each step of the sorting process visually


**Computational Thinking**

Decomposition: Parse the user’s list of numbers, implement bubble sort, Capture each comparison state, Display results step-by-step in the UI

Pattern Recognition: Bubble sort repeatedly compares adjacent elements, If one is larger than the next → swap, Each pass pushes the largest remaining element to the end, Detect patterns like: no swaps → the list is already sorted

Abstraction: Ignore unnecessary details (e.g., machine-level operations) Focus only on: Current index Elements being compared Whether a swap happened The updated state of the list

Algorithm Design: Loop through the list multiple times Compare each adjacent pair Swap when needed Stop early if no swaps occurred Record each state so Streamlit can visualize the steps


**Steps to run**
1. Open hugging face and go to "App" section
2. Enter Numbers one by one spaced with a comma (eg. 6,7,1,2,3,)
3. Click "Run Bubble Sort"
4. Scroll and see the passes and final product


**Hugging Face link:**
https://huggingface.co/spaces/anishkatarina0202/runplease

**Author & Acknowledgment**
This project was created by Anish Kataria and was made using Streamlit and Python 









