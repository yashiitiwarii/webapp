import streamlit as st

st.header("CAL GPA")

def grades(score):
    if score >= 90:
        grade = 10
    elif score >= 75:
        grade = 9
    elif score >= 65:
        grade = 8
    elif score >= 55:
        grade = 7
    elif score >= 50:
        grade = 6
    elif score >= 45:
        grade = 5
    elif score >= 40:
        grade = 4
    else:
        grade = 0 

    return grade 


def cal_fun(semester):
    theorypapers = {}
    practicals = {}
    GPA = 0
    flag = 0
    creditpoints= 0
    col1, col2 = st.columns(2)

    if semester == 1:
        theorypapers = {"APPLIED MATHEMATICS": 4, "APPLIED PHYSICS": 3, "ELECTRICAL SCIENCE":3, "APPLIED CHEMISTRY": 3, "MANUFACTURING PROCESS": 4,"COMMUNICATION SKILLS":3}
        practicals = {"PHYSICS": 1, "APPLIED CHEMISTRY": 1, "ENGINEERING GRAPHICS": 2, "ELECTRICAL SCIENCE": 1}
        creditpoints = 25
    elif semester == 2:
        theorypapers = {"APPLIED CHEMISTRY OR C PROGRAMMING": 3, "ELECTRICAL SCIENCE": 3, "APPLIED MATHEMATICS": 4, "APPLIED PHYSICS": 3, "COMMUNICATION SKILLS": 3, "ENGINEERING MECHANICS": 3}
        practicals = {"APPLIED CHEMISTRY OR C PROGRAMMING": 1, "ENGINEERING GRAPHICS": 1, "ELECTRICAL SCIENCE": 1, "WORKSHOP PRACTICE": 2}
        creditpoints = 25
    elif semester == 3:
        theorypapers = {"COMPUTATIONAL METHODS": 4, "PROGRAMME CORE THEORY PAPERS": 16, "ELEMENTS OF INDIAN HISTORY FOR ENGINEERS": 2}
        practicals = {"COMPUTATIONAL METHODS LAB": 1, "PROGRAMME CORE LAB PAPERS": 3}
        creditpoints = 26
    elif semester == 4:
        theorypapers = {"PROBABILITY, STATISTICS AND LINEAR PROGRAMMING": 4, "PROGRAMME CORE THEORY PAPERS": 16, "TECHNICAL WRITING": 2}
        practicals = {"PROGRAMME CORE LAB PAPERS": 3}
        creditpoints = 26
    elif semester == 5:
        theorypapers = {"PROGRAMME CORE THEORY PAPERS": 20, "ECONOMICS FOR ENGINEERS": 2}
        practicals = {"PROGRAMME CORE LAB PAPERS": 3, "SUMMER TRAINING REPORT": 1}
        creditpoints = 26
    elif semester == 6:
        theorypapers = {"PROGRAMME CORE ELECTIVE PAPERS": 12, "EMERGING AREA/ OPEN AREA ELECTIVE PAPERS": 8, "PRINCIPLES OF MANAGEMENT FOR ENGINEERS": 4}
        practicals = {"NSS/ TECHNICAL SOCIETY/ TECHNICAL CLUBS": 2}
        creditpoints = 26 
    elif semester == 7:
        theorypapers = {"PROGRAMME CORE ELECTIVE PAPERS": 8, "EMERGING AREA /OPEN AREA":12, "PRINCIPLES OF ENTREPRENEURSHIP MINDSET": 2}
        practicals = {"MINOR PROJECT": 3, "SUMMER TRAINING REPORT": 1}
        creditpoints = 26
    elif semester == 8:
        practicals = {"MAJOR PROJECT": 14, "MAJOR PROJECT VIVA VOCE": 4, "PROJECT PROGRESS EVALUATION": 2, "INTERNSHIP REPORT": 14, "INTERNSHIP VIVA VOCE": 4, "INTERNSHIP PROGRESS EVALUATION": 2}
        creditpoints = 20

    with col1:
        with st.expander("Theory Subjects"):
            for subject in theorypapers:
                score = st.number_input("{}:".format( subject ), 0, 100)
                if score == 0 :
                    flag = 1
                num = grades(score)
                GPA += num * theorypapers[subject]

    with col2:
        with st.expander("Practical Subjects"):
            for lab in practicals:
                score1 = st.number_input("{}:".format( lab ), 0, 100)
                if score == 0 :
                    flag = 1
                num1 = grades(score1)
                GPA += num * practicals[lab]

    if flag:
        st.warning("You haven't entered the marks of all subjects!")

    GPA = GPA / credits
    return GPA            

st.markdown("<h1 style='text-align: center; color: red;'>CalcGPA</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; '>Semester GPA Calculator of B.Tech(COMPUTER SCIENCE AND ENGINEERING)</h3>", unsafe_allow_html=True)

  

with st.container():
    name = st.text_input("ENTER YOUR NAME")

    if name:
        st.write("Hello {}!".format(name))
        sem = st.number_input("ENTER YOUR SEMESTER", 0, 8)

        if sem:
            st.write("")
            st.write("")
            st.markdown("<h3 style='text-align: center; '>Enter Marks!</h3>", unsafe_allow_html=True)

            GPA = cal_fun(sem)

            st.write("")
            st.write("")

            cl1, cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9 = st.columns(9) #just for formatting XD
            with cl5:
                ans = st.button("Submit")


            if ans:
                msg = "Your GPA: {}".format(str(round(GPA,2)))
                st.markdown(f"<h3 style='text-align: center; '>{msg}</h3>", unsafe_allow_html=True)
                if GPA >= 8.0 :
                    st.balloons()
                    st.balloons()
                    st.balloons()


