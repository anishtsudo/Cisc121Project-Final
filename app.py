import streamlit as st
from algorithms import bubble_sort_trace

st.set_page_config(page_title="Bubble Sort Visualizer")

st.title("🔵 Bubble Sort Visualizer")

# Input array
user_input = st.text_input(
    "Enter numbers separated by commas:",
    "5, 3, 8, 4, 2"
)

if st.button("Run Bubble Sort"):
    try:
        values = [int(x.strip()) for x in user_input.split(",")]

        states, sorted_values = bubble_sort_trace(values)

        st.subheader("Sorting Steps")

        for state in states:
            st.write(f"Comparing index {state.index_a} and {state.index_b}")
            st.write(f"Swapped: {state.swapped}")
            st.write(list(state.data))
            st.divider()

        st.subheader("Final Sorted Output")
        st.success(sorted_values)

    except:
        st.error("Invalid input. Please enter integers only.")
