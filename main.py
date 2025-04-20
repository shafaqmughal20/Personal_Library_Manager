import streamlit as st
import json
import time
import random

def load_library():
    try:
        with open('library.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library():
    with open('library.json', 'w') as file:
        json.dump(library, file, indent=4)

library = load_library()

# Custom Styling with Animated Gradient
st.markdown(
    """
    <style>
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        body {
            background: linear-gradient(-45deg, #1e1e1e, #b00020, #3a3a3a, #ff1744);
            background-size: 400% 400%;
            animation: gradientBG 10s ease infinite;
            color: white;
            shadow: large black;
            font-family: 'Arial', sans-serif;
        }
        .stTextInput, .stButton {
            border-radius: 10px;
            background-color: #333;
            color: white;
            padding: 10px;
            transition: 0.3s;
        }
        .stTextInput:focus, .stButton:hover {
            background-color: #b00020;
            color: white;
        }
        .stSidebar {
            background-color: #222;
            color: white;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #ff1744;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('📖 Personal Library Manager')
st.subheader('Manage your personal library in style!')

menu = st.sidebar.selectbox('Select an option:', [
    'Add Book',
    'Remove Book',
    'Update Book',
    'View All Books',
    'Save',
    'Exit'
])

def success(message):
    with st.spinner('Processing...'):
        time.sleep(random.uniform(1, 2))
    st.success(message, icon="✅")

if menu == 'Add Book':
    st.subheader('📚 Add a New Book')
    book_name = st.text_input('Book Name')
    author = st.text_input('Author')
    genre = st.text_input('Genre')
    if st.button('➕ Add Book', use_container_width=True):
        if book_name and author and genre:
            library.append({'Book Name': book_name, 'Author': author, 'Genre': genre})
            save_library()
            success('Book added successfully!')
            st.rerun()
        else:
            st.warning('Please fill all fields!')

elif menu == 'Remove Book':
    st.subheader('🗑 Remove a Book')
    book_name = st.text_input('Book Name')
    if st.button('❌ Remove Book', use_container_width=True):
        for book in library:
            if book['Book Name'] == book_name:
                library.remove(book)
                save_library()
                success('Book removed successfully!')
                st.rerun()
                break
        else:
            st.warning('Book not found!')

elif menu == 'Update Book':
    st.subheader('✏️ Update Book Information')
    book_name = st.text_input('Book Name')
    new_author = st.text_input('New Author')
    new_genre = st.text_input('New Genre')
    if st.button('🔄 Update Book', use_container_width=True):
        for book in library:
            if book['Book Name'] == book_name:
                book['Author'] = new_author or book['Author']
                book['Genre'] = new_genre or book['Genre']
                save_library()
                success('Book updated successfully!')
                st.rerun()
                break
        else:
            st.warning('Book not found!')

elif menu == 'View All Books':
    st.subheader('📖 Your Book Collection')
    if library:
        for book in library:
            st.markdown(f"**📕 {book['Book Name']}**")
            st.write(f"👨‍💼 Author: {book['Author']}")
            st.write(f"📌 Genre: {book['Genre']}")
            st.write('---')
    else:
        st.warning('No books found!')

elif menu == 'Save':
    if st.button('💾 Save Library', use_container_width=True):
        save_library()
        success('Library saved successfully!')

elif menu == 'Exit':
    st.warning('Application will close after saving...')
    if st.button('🚪 Exit', use_container_width=True):
        save_library()
        success('Library saved! Exiting...')
        st.stop()
