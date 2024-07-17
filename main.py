    import streamlit as st

    # 코드스니펫 - 제목 
    st.title('[스파르타] Streamlit Style Cheatsheet')

    # 코드스니펫 - 입력
    keyword = st.text_input("키워드를 입력하세요.")

    # 코드스니펫 - 버튼
    st.button('그냥 버튼')
    if st.button('노크하기'):
        st.write('여기 사람 있어요')