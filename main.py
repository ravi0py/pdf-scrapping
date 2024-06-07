import streamlit as st
from pdf_processing import extract_text_from_pdf, categorize_text, convert_categories_to_csv

def main():
    st.title("PDF Text Extraction and Categorization")

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    
    if uploaded_file is not None:
        with open("uploaded_file.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("File uploaded successfully!")
        
        if st.button("Process PDF"):
            with st.spinner("Extracting and categorizing text..."):
                text = extract_text_from_pdf("uploaded_file.pdf")
                categories = categorize_text(text)
                
                st.subheader("Categorized Text")
                for category, lines in categories.items():
                    st.markdown(f"### {category.capitalize()}")
                    st.write("\n".join(lines[:10]))  # Display first 10 lines for each category
                
                csv = convert_categories_to_csv(categories)
                
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name='categorized_text.csv',
                    mime='text/csv',
                )
                st.success("Text categorized and ready for download!")

if __name__ == "__main__":
    main()
