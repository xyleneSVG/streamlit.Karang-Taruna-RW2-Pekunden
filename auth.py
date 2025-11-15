import streamlit as st

def login():
    st.session_state.setdefault("logged_in", False)
    st.session_state.setdefault("login_failed", False)

    if not st.session_state.logged_in:
        st.subheader("🔐 Login Admin")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_btn = st.button("Login")

        if login_btn:
            if (
                username == st.secrets["auth"]["admin_user"]
                and password == st.secrets["auth"]["admin_pass"]
            ):
                st.session_state.logged_in = True
                st.session_state.login_failed = False
                st.success("✅ Login berhasil!")
                st.experimental_rerun()
            else:
                st.session_state.login_failed = True
                st.error("❌ Username atau password salah")
        return False
    return True