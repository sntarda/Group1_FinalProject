def main(st, iframe_style):
    iframe_style = {iframe_style}
    
    st.title("Enrollment Demographics")
    st.write("\n\n")
        
    # Figure 1
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[1]. CLASSROOMS DEMOGRAPHICS BY AGE AND GENDER</h4>
    """, unsafe_allow_html=True)
    st.subheader("* Two Consecutive School Years (Aug 2022 - May 2024)")
    # Use the st.write() function to display the iframe
    st.write(f'<iframe title="Program Age Group" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiZDUyNDIwZjQtMDkwYS00ZDQ0LWExZDYtZDFjZmVkNzJmODQzIiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html = True)
    st.subheader("Figure 1: Table Matrix (PowerBI)")
    st.write("\n\n")
    st.subheader("Analysis")
    multi = '''
    In the enrollment demographics section, we provide multiple visualizations detailing classroom compositions, student numbers, enrollment per class, and the diversity of cities.
    
    As you already know about montessori schools, it is based on the idea that children are naturally curious and eager to learn and the provided environment allows them to explore and 
    learn at their own pace. This means that our classrooms often comprise students of mixed ages, as depicted in the chart. Here, you can see the distribution of female and male students 
    in each class, along with their ages and the total number of students in each class.
    
    Moreover, school administrators can use this data to identify students who are performing exceptionally well and have been promoted to the next class ahead of their designated age 
    (or vice versa). This information can also shed light on classes where there's a higher proportion of students advancing early. This could be attributed to the effectiveness of the teachers assigned to those classes, suggesting they are doing an excellent job mentoring their students.
   
    By analyzing this data, administrators gain insights into the dynamics of each class and can make informed decisions to support student growth and success.
        '''
    st.markdown(multi, unsafe_allow_html=True)
    

    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 2
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[2]. ACTIVE STUDENTS DEMOGRAPHICS BY CITY</h4>
    """, unsafe_allow_html=True)
    # Correctly embedding the Tableau visualization
    st.write(f'<iframe src="https://prod-useast-b.online.tableau.com/t/samirtarda707500432c/views/StudentsDemographics/Sheet1?:embed=y&:display_count=yes&:showVizHome=no" width="1024" height="825"></iframe>', unsafe_allow_html=True)
    st.subheader("Figure 2: Heatmap (Tableau)")
    st.write("\n\n")
    st.subheader("Analysis")
    multi = '''
    Active student distribution by city.
    The graph above provides a straightforward and easily interpretable view of the distribution of active students by city. School administrators can utilize this graph for various 
    important purposes, such as marketing and ensuring accessibility of the school to students from different cities.
    
    For example, if a city like Carrollton has a high enrollment of 1400 students instead of just 14, the school administration might consider arranging transportation systems 
    to make the school more accessible to these students and their parents.
    
    Additionally, this data can help administrators address low enrollment in certain cities by identifying potential causes and adjusting their marketing and discount campaigns accordingly. 
    
    By reallocating resources to cities with higher enrollment, they can effectively target areas with greater potential for growth.
        '''
    st.markdown(multi, unsafe_allow_html=True)
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 3
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[3]. ACTIVE STUDENTS DEMOGRAPHICS BY CITY</h4>
    """, unsafe_allow_html=True)
    # Correctly embedding the Tableau visualization
    st.write(f'<iframe title="Top Cities for School Enrollment (Heatmap)" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=4ec16432-4288-4f32-8aeb-bbdcb9237ab1&autoAuth=true&ctid=70de1992-07c6-480f-a318-a1afcba03983" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html = True)
    st.subheader("Figure 3: Filled Heatmap (PowerBI)")
    st.write("\n\n")
    st.subheader("Analysis")
    st.write("Analyze here")
    multi = '''
    Same as Figure (2)
    '''
    st.markdown(multi, unsafe_allow_html=True)


