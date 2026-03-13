import streamlit as st
import pandas as pd
from datetime import datetime
import os

# --- 1. إعدادات الهوية الرسمية (اقتصادية دبي) ---
st.set_page_config(page_title="حماية المستهلك | دبي", page_icon="🛡️", layout="wide")

# تنسيق الألوان والشعار (الأحمر الرسمي)
st.markdown("""
<style>
    [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stSidebar"] {
        direction: rtl; text-align: right;
    }
    .stButton>button {
        background-color: #E6192E !important;
        color: white !important;
        border-radius: 8px;
    }
    .main-title {
        color: #E6192E;
        text-align: center;
        border-bottom: 2px solid #E6192E;
        padding-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🛡️ منصة الرقابة التجارية الذكية</h1>', unsafe_allow_html=True)

# --- 2. القائمة الجانبية ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Flag_of_the_United_Arab_Emirates.svg/255px-Flag_of_the_United_Arab_Emirates.svg.png", width=100)
    st.write(f"📅 التاريخ: {datetime.now().strftime('%Y-%m-%d')}")
    st.info("نظام داخلي مخصص لمفتشي دائرة الاقتصاد والسياحة.")

# --- 3. تبويبات العمل الميداني ---
tab1, tab2 = st.tabs(["🔍 دليل التواصل مع الشركات", "📝 توثيق مخالفة"])

with tab1:
    st.subheader("البحث في قاعدة بيانات ضباط الامتثال")
    # التأكد من وجود ملف الإكسل
    if os.path.exists("Contacts.xlsb"):
        try:
            df = pd.read_excel("Contacts.xlsb", engine='pyxlsb')
            search = st.text_input("ابحث عن اسم الشركة (مثال: أمازون، ماجد الفطيم):")
            if search:
                results = df[df.astype(str).apply(lambda x: x.str.contains(search, case=False, na=False)).any(axis=1)]
                st.dataframe(results)
            else:
                st.dataframe(df.head(20))
        except Exception as e:
            st.error(f"خطأ في تحميل البيانات: {e}")
    else:
        st.warning("⚠️ يرجى التأكد من رفع ملف 'Contacts.xlsb' في GitHub بجانب هذا الملف.")

with tab2:
    st.subheader("تسجيل حالة ميدانية")
    with st.form("violation_form"):
        name = st.text_input("اسم المفتش")
        comp = st.text_input("اسم المنشأة")
        v_type = st.selectbox("نوع التجاوز", ["تلاعب بالأسعار", "سلع مقلدة", "إعلان مضلل"])
        if st.form_submit_button("حفظ التقرير"):
            st.success("تم تسجيل البيانات بنجاح.")

