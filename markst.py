import streamlit as st

#Grade Criteria
grade_req = {
    "A+ (80-100)": 80,
    "A(75-79)": 75,
    "A-(70-74)": 70,
    "B+(65-69)": 65,
    "B(60-64)": 60,
    "B-(55-59)": 55,
    "C+(50-54)": 50,
    "C(45-49)": 45,
    "D(40-44)": 40
}


#Calculates the minimum marks required out of 100
def calc_func(grade,incourse):
        marks = (grade_req[grade] - incourse)*2
        return marks



st.title("MARK CALCULATOR FOR STUDENTS OF BUP")
st.header("Developed by Farhan Hasan, Undergrad Student, BUP, BICE - 2025")

st.write(
    """
    Enter your current marks and select your target grade.
    The calculator will determine the minimum final exam mark
    required to achieve that grade (Theoretical courses only).
    """
)

st.header("Class Tests")
st.write("Best 3 Class Tests Out of 4")
ct1_total = st.number_input("CT 01 Total Mark", 
                            min_value = 1, 
                            value = 1)

ct1_marks = st.number_input("CT 01 Obtained Mark", min_value = 0.0, 
                            max_value = float(ct1_total), 
                            value = 0.0)


ct2_total = st.number_input("CT 02 Total Mark", 
                            min_value = 1, 
                            value = 1)

ct2_marks = st.number_input("CT 02 Obtained Mark", min_value = 0.0, 
                            max_value = float(ct2_total), 
                            value = 0.0)



ct3_total = st.number_input("CT 03 Total Mark", 
                            min_value = 1, 
                            value = 1)

ct3_marks = st.number_input("CT 03 Obtained Mark", min_value = 0.0, 
                            max_value = float(ct3_total), 
                            value = 0.0)


#CT and Total Marks Calculation
ct_list = [ct1_marks, ct2_marks, ct3_marks]
total_list = [ct1_total, ct2_total, ct3_total]

        
ct_marks = 0
for ct, total in zip(ct_list, total_list):
        converted = (ct/total) * (10/3)
        ct_marks += converted


st.metric("Converted CT Marks", f"{ct_marks:.2f}/10")

#Calculating marks obtained in other criteria
st.header("Attendance")
attendance = 0

a_status = st.selectbox("Attendance Marks Given?", ["Yes", "No"])

if a_status == "Yes":
       attendance = st.number_input("Attendance Marks (out of 10)",
                       min_value = 0.00,
                       max_value = 10.00,
                       value = 0.00,
                       step = 0.01
                       )
else :
        present = st.number_input("Present",
                                min_value = 0,
                                value = 0,
                                step = 1)

        absent = st.number_input("Absent",
                                min_value = 0,
                                value = 0,
                                step = 1)
        total = present + absent

        if total == 0:
                st.error("Invalid Input For Present/Absent")

        else:
                attendance = 10*(present / (total))    

st.metric("Attendance Mark", f"{attendance:.2f}/10")


st.header("Assignment/Presentation/Term-Paper")
assignment = st.number_input("Assignment/Presentation/Term-Paper",
                             min_value = 0.0,
                             max_value = 10.0,
                             value = 0.0)


st.header("Mid-Term")
mid_x = st.number_input("Mid-Term (out of 30)", 
                        min_value = 0.0,
                        max_value = 30.0, 
                        value = 0.0)
mid = mid_x * (20/30)

st.metric("Converted Mid-Term Mark", f"{mid:.2f}/20")

#GPA Validation and Collection
st.header("Target Grade")
grade = st.selectbox("Target Grade", list(grade_req.keys()))


if st.button("Calculate"):
    inc = ct_marks + attendance + assignment + mid
    st.metric("In-Course Mark", f"{inc:.2f}/50")
    marks = calc_func(grade, inc)
     
    if marks > 100:
            st.error(f"{grade} Is No Longer Attainable With Current In-Course Marks")
    elif marks <= 0:
            st.success(f"{grade} Is Already Attained With Current In-Course Marks")

    else:
            st.metric(f"Minimum Marks For {grade}", f"{marks:.2f}/100")



    
    result = []

    for grade in grade_req:

        marks = calc_func(grade, inc)
        
        if marks > 100:
               status =  "No Longer Attainable With Aurrent In-Course Marks"
        
        elif marks <= 0:
                status = "Already Attained With Current In-Course Marks"

        else:
                status = f"{marks:.2f}/100"
        
        result.append(
                {
                       "Grade" : grade,
                       "Marks Required" : status
                }
        )
    st.subheader("Table Of Grades And Minimum Final Marks Required")
    st.table(result)

  

