import streamlit as st
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
from datetime import datetime

# Set page config
st.set_page_config(page_title="Data Analyst Portfolio", layout="wide")

# Custom CSS (place in a separate CSS file)
def local_css(url):
    response = requests.get(url)
    if response.status_code == 200:
        st.markdown(f'<style>{response.text}</style>', unsafe_allow_html=True)
    else:
        st.error("Failed to load CSS from GitHub.")

# Ganti dengan URL raw file CSS Anda di GitHub
css_url = "https://raw.githubusercontent.com/yeheskieltame/Portofolio/refs/heads/main/data-analyst/style.css"
local_css(css_url)


# Load Lottie animations (place JSON files in a dedicated folder)
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_contact = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_u25cckyh.json")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Certifications", "Contact"])

# Home Page
def create_home_page():
    # Two-column layout
    left_column, right_column = st.columns(2)

    with left_column:
        # Add a profile picture from a URL
        st.image("https://github.com/yeheskieltame/Portofolio/blob/main/img/117884201-3.png?raw=true", width=400, caption="Yeheskiel Yunus Tame")
        st.markdown(
            "<p style='text-align: left; font-size: 20px;'>Hello! I'm <span style='color: #3498db; font-weight: bold;'>Yeheskiel Yunus Tame</span>, a passionate Data Analyst with expertise in:</p>",
            unsafe_allow_html=True)

        st.markdown("""
        - 📊 Data Visualization
        - 📈 Statistical Analysis
        - 🤖 Machine Learning
        - 💻 Python Programming
        - 🗄️ SQL and Database Management
        """)

        st.markdown(
            "<p style='text-align: left; font-size: 18px;'>I turn complex data into actionable insights, helping businesses make informed decisions.</p>",
            unsafe_allow_html=True)

        st.markdown("---")

        st.markdown("<h3 style='text-align: left; color: #3498db;'>Quick Stats</h3>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        col1.metric("Projects Completed", "20+")
        col2.metric("Years of Experience", "5")
        col3.metric("Happy Clients", "15")

    with right_column:
        st.markdown("<h1 style='text-align: left; color: #3498db;'>Welcome to My Data Analyst Portfolio</h1>",
                    unsafe_allow_html=True)

        st_lottie(lottie_coding, height=300, key="coding")

        st.markdown("---")

        st.markdown("<h3 style='text-align: left; color: #3498db;'>Latest Achievement</h3>", unsafe_allow_html=True)
        st.info("🏆 Recently completed the 'Linear Algebra for Machine Learning and Data Science' course by DeepLearning.AI")

        st.markdown("---")

        st.markdown("<h3 style='text-align: left; color: #3498db;'>Featured Skill</h3>", unsafe_allow_html=True)
        st.progress(90)
        st.markdown("<p style='text-align: center;'>Python Proficiency: 90%</p>", unsafe_allow_html=True)

if page == "Home":
    create_home_page()

# (Rest of the code remains the same for other pages)
# Projects Page
elif page == "Projects":
    st.markdown("<h1 style='text-align: center; color: #3498db;'>Data Visualization Projects</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px; margin-bottom: 30px;'>Explore my recent data visualization and analysis projects.</p>", unsafe_allow_html=True)

    # List of projects
    projects = [
        {
            "title": "Data Analytics Project: Bike Sharing Dataset",
            "description": (
                "This **data analysis project** focuses on a **bike-sharing dataset**, aiming to understand "
                "rental patterns based on **days and times**. Here are the key steps taken in the analysis:\n\n"
                "**Business Questions**: Two primary questions were identified: (a) Is there a significant difference "
                "in bike rentals between **holidays** and **weekdays**, as well as between **weekends** and regular weekdays? "
                "(b) At what times do bike rentals **peak**?\n\n"
                "**Data Collection**: Two datasets were downloaded and loaded: one containing daily rental information "
                "(**day.csv**) and another with hourly data (**hour.csv**).\n\n"
                "**Data Assessment**: The structure and summary statistics of both datasets were examined to ensure "
                "there were no significant missing values.\n\n"
                "**Data Cleaning**: The data was cleaned to ensure it was ready for further analysis, which involved "
                "removing or addressing any missing values.\n\n"
                "**Exploratory Data Analysis (EDA)**:\n\n"
                "- Calculated and compared bike rental counts on **holidays** versus **weekdays** and between **weekends** "
                "and regular weekdays.\n"
                "- Utilized visualizations such as **boxplots** and **lineplots** to clarify findings.\n\n"
                "**Advanced Analysis**: Identified the **top three days** with the highest rental counts and the best contiguous "
                "hours for rentals to optimize rental strategies.\n\n"
                "**Conclusion**:\n\n"
                "- **Weekdays** tend to show higher average rentals compared to **holidays**.\n"
                "- Peak rentals occur in the **late afternoon**, particularly between **5 PM and 7 PM**.\n\n"
                "This analysis provides valuable insights for **marketing strategies** and **operational decisions** in bike-sharing services."
            ),
            "project": "https://github.com/yeheskieltame/Project-Data-Analist.git",
            "dashboard": "https://zsoeyhh3bvdl7bwvenk5ma.streamlit.app/",
            "icon": "fas fa-cogs",
            "visual_type": "image",
            "visual_data": {
                "url":"https://github.com/yeheskieltame/Project-Data-Analist/blob/main/Data/download.png?raw=true"
            }
        }
    ]

    # Display projects in a grid
    for project in projects:
        st.markdown(f"""
        <div class="project-card">
            <div class="project-header">
                <i class="{project['icon']} fa-2x" style="color: #3498db;"></i>
                <h3>{project['title']}</h3>
            </div>
            <p>{project['description']}</p>
        """, unsafe_allow_html=True)

        # Display visual based on type
        if project['visual_type'] == 'plotly':
            fig = px.bar(x=project['visual_data']['x'], y=project['visual_data']['y']) if project['visual_data']['type'] == 'bar' else px.scatter(x=project['visual_data']['x'], y=project['visual_data']['y'])
            fig.update_layout(height=300, margin=dict(l=20, r=20, t=30, b=20))
            st.plotly_chart(fig, use_container_width=True)
        elif project['visual_type'] == 'lottie':
            st_lottie(load_lottieurl(project['visual_data']), height=200)
        elif project['visual_type'] == 'image':
            st.image(project['visual_data']['url'], use_column_width=True)  # Ini benar

    st.markdown(f"""
            <a href="{project['project']}" target="_blank" class="project-link">View Project <i class="fas fa-external-link-alt"></i></a> </div><a href="{project['dashboard']}" target="_blank" class="project-link">View Dashboard <i class="fas fa-external-link-alt"></i></a></div>
        """, unsafe_allow_html=True)

# Skills Page
elif page == "Skills":
    st.title("My Skills")

    st.markdown(
        "<p style='text-align: center; font-size: 20px; margin-bottom: 30px;'>Here are some of the skills I’ve honed over the years</p>",
        unsafe_allow_html=True)

    skills = {
        'Python': 100,
        'SQL': 90,
        'Data Visualization': 90,
        'Statistical Analysis': 87,
        'Machine Learning': 90,
        'Git': 100,
        'Laravel': 80,
        'Web Development': 70
    }

    # Customizing the skill display
    for skill, proficiency in skills.items():
        col1, col2 = st.columns([1, 4])
        with col1:
            st.markdown(f"<h4 style='color: #3498db;'><i class='fas fa-check-circle'></i> {skill}</h4>",
                        unsafe_allow_html=True)
        with col2:
            st.progress(proficiency / 100)

    st.markdown("---")

    st.markdown("<h3 style='text-align: center; color: #3498db;'>Proficiency Breakdown</h3>", unsafe_allow_html=True)

    # Skill categories and percentages
    skill_categories = {
        "Programming": 85,
        "Machine Learning": 90,
        "Data Analytics": 95,
        "Database Management": 70
    }

    fig = px.pie(
        names=list(skill_categories.keys()),
        values=list(skill_categories.values()),
        title="Skill Distribution"
    )
    fig.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=2)))
    st.plotly_chart(fig)


# Certifications Page
elif page == "Certifications":
    st.markdown("<h1 style='text-align: center; color: #3498db;'>Certifications & Licenses</h1>",
                unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; font-size: 20px; margin-bottom: 30px;'>Continuous learning and professional development</p>",
        unsafe_allow_html=True)

    certifications = [
        {
            "name": "Linear Algebra for Machine Learning and Data Science",
            "issuer": "DeepLearning.AI",
            "issue_date": "Oct 2024",
            "expiration_date": None,
            "credential_id": "X1AKSP4V28QN",
            "credential_url": "https://www.coursera.org/account/accomplishments/verify/X1AKSP4V28QN",
            "image_url": "https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/http://coursera-university-assets.s3.amazonaws.com/b4/5cb90bb92f420b99bf323a0356f451/Icon.png?auto=format%2Ccompress&dpr=2&w=80&h=80"
        },
        {
            "name": "Belajar Analisis Data dengan Python",
            "issuer": "Dicoding Indonesia",
            "issue_date": "Sep 2024",
            "expiration_date": "Sep 2027",
            "credential_id": "1OP84LG61ZQK",
            "credential_url": "https://www.dicoding.com/certificates/1OP84LG61ZQK",
            "image_url": "https://dicoding-web-img.sgp1.cdn.digitaloceanspaces.com/original/academy/dos:belajar_analisis_data_dengan_python_logo_271222164447.jpg"
        },
        {
            "name": "Belajar Dasar Git dengan GitHub",
            "issuer": "Dicoding Indonesia",
            "issue_date": "Sep 2024",
            "expiration_date": "Sep 2027",
            "credential_id": "JMZV3KO5JPN9",
            "credential_url": "https://www.dicoding.com/certificates/JMZV3KO5JPN9",
            "image_url": "https://d17ivq9b7rppb3.cloudfront.net/original/academy/belajar_dasar_git_dengan_github_logo_050721150715.jpg"
        },
        {
            "name": "Using Python to Interact with the Operating System",
            "issuer": "Google",
            "issue_date": "Sep 2024",
            "expiration_date": None,
            "credential_id": "5D7M81TJ3QZ2",
            "credential_url": "https://www.coursera.org/account/accomplishments/verify/5D7M81TJ3QZ2",
            "image_url": "https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/http://coursera-university-assets.s3.amazonaws.com/4a/cb36835ae3421187080898a7ecc11d/Google-G_360x360.png?auto=format%2Ccompress&dpr=2&w=80&h=80"
        },
        {
            "name": "Using Python to Interact with the Operating System",
            "issuer": "Google",
            "issue_date": "Sep 2024",
            "expiration_date": None,
            "credential_id": "S6KHEU5OCWWS",
            "credential_url": "https://www.coursera.org/account/accomplishments/verify/S6KHEU5OCWWS",
            "image_url": "https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/http://coursera-university-assets.s3.amazonaws.com/4a/cb36835ae3421187080898a7ecc11d/Google-G_360x360.png?auto=format%2Ccompress&dpr=2&w=80&h=80"
        },
        {
            "name": "Memulai Dasar Pemrograman untuk Menjadi Pengembang Software",
            "issuer": "Dicoding Indonesia",
            "issue_date": "Sep 2024",
            "expiration_date": "Sep 2027",
            "credential_id": "81P2N05WNXOY",
            "credential_url": "https://www.dicoding.com/certificates/81P2N05WNXOY",
            "image_url": "https://d17ivq9b7rppb3.cloudfront.net/original/academy/pengenalan_ke_dasar_pemrograman_basic_programming_101_logo_230421132319.jpg"
        },
        {
            "name": "Pengenalan ke Logika Pemrograman (Programming Logic 101)",
            "issuer": "Dicoding Indonesia",
            "issue_date": "Sep 2024",
            "expiration_date": "Sep 2027",
            "credential_id": "JLX17OVD6X72",
            "credential_url": "https://www.dicoding.com/certificates/JLX17OVD6X72",
            "image_url": "https://d17ivq9b7rppb3.cloudfront.net/original/academy/pengenalan_ke_logika_pemrograman_programming_logic_101_logo_230421133238.jpg"
        },
        {
            "name": "Laravel Web Development",
            "issuer": "SanberCode",
            "issue_date": "Aug 2023",
            "expiration_date": None,
            "credential_id": "-",
            "credential_url": "https://sanbercode.com/certificate/in/c352b903-be13-445f-9aa7-3bc77f2ba2f3",
            "image_url": "https://media.licdn.com/dms/image/v2/C4D0BAQH3ULtAlMdUWQ/company-logo_100_100/company-logo_100_100/0/1630558036477?e=1736380800&v=beta&t=cPTM6l6F9il002BEeVxXkt3cuyG3PKfGru0Z6K6tVA0"
        },
        # Add more certifications as needed
    ]

    for cert in certifications:
        col1, col2 = st.columns([1, 3])

        with col1:
            st.image(cert["image_url"], width=100)

        with col2:
            st.markdown(f"<h3 style='margin-bottom: 0;'>{cert['name']}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin-bottom: 5px;'><strong>{cert['issuer']}</strong></p>", unsafe_allow_html=True)

            issue_date = datetime.strptime(cert['issue_date'], "%b %Y")
            if cert['expiration_date']:
                expiration_date = datetime.strptime(cert['expiration_date'], "%b %Y")
                st.markdown(
                    f"<p style='margin-bottom: 5px;'>Issued {issue_date.strftime('%b %Y')} · Expires {expiration_date.strftime('%b %Y')}</p>",
                    unsafe_allow_html=True)
            else:
                st.markdown(
                    f"<p style='margin-bottom: 5px;'>Issued {issue_date.strftime('%b %Y')} · No Expiration Date</p>",
                    unsafe_allow_html=True)

            st.markdown(f"<p style='margin-bottom: 5px;'>Credential ID: {cert['credential_id']}</p>",
                        unsafe_allow_html=True)
            st.markdown(
                f"<a href='{cert['credential_url']}' target='_blank' class='credential-link'>Show credential <i class='fas fa-external-link-alt'></i></a>",
                unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)
# Contact Page
elif page == "Contact":
    st.markdown("<h1 style='text-align: center; color: #3498db;'>Get in Touch</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; font-size: 20px;'>I'd love to hear from you! Whether you have a question or just want to say hi, feel free to drop me a message.</p>",
        unsafe_allow_html=True)

    # Two-column layout
    col1, col2 = st.columns(2)

    with col1:
        st_lottie(lottie_contact, height=300, key="contact")

    with col2:
        st.markdown("<h3 style='color: #3498db;'>Contact Information</h3>", unsafe_allow_html=True)

        # Contact information with icons
        st.markdown("""
        <div class="contact-info">
            <p><i class="fas fa-envelope"></i> Email: yeheskielyunustame13@gmail.com</p>
            <p><i class="fab fa-linkedin"></i> LinkedIn: <a href="https://www.linkedin.com/in/yeheskiel/" target="_blank">MY LinkedIn Profile</a></p>
            <p><i class="fab fa-github"></i> GitHub: <a href="https://github.com/yeheskieltame" target="_blank">MY GitHub Profile</a></p>
            <p><i class="fas fa-map-marker-alt"></i> Location: Yogyakarta, Indonesia</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center; color: #3498db; margin-top: 2rem;'>Send Me a Message</h3>",
                unsafe_allow_html=True)

    # Contact Form
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Send Message")

    if submit_button:
        st.success("Thanks for your message! I'll get back to you soon.")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("© 2024 Yeheskiel Yunus Tame. All rights reserved.")
