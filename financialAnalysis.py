import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


def read_original_data():
    # dataset file path
    file_path = 'students_info.csv'
    data = pd.read_csv(file_path)
    return data

def stat_summary_data(data):
    data = read_original_data()
    # Define the columns you're interested in
    columns = ['Billing Amount', 'Original Charge', 'Discount Amount', 'Status']
    if columns:  
        # Select only these columns
        df = data.loc[:, columns]     
    return df

def new_func():
    return "Active"

def confusion_matrix_data(data):
    data = read_original_data()
    columns = ['Billing Amount', 'Original Charge', 'Discount Amount', 'Program', 'Date']
    df = data[columns].copy()
    
    df['Program'] = df['Program'].astype('category')
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date')

    for column in ['Billing Amount', 'Original Charge', 'Discount Amount',]:
        df[column] = pd.to_numeric(df[column].replace('[\$,]', '', regex=True).replace('', 'NaN'), errors='coerce')
    
    return df
def pairplot_data(data):
    data = read_original_data()
    # Define the columns you're interested in
    columns = ['Billing Amount', 'Discount Amount', 'Program']
    if columns:  
        # Select only these columns
        df = data.loc[:, columns]     
    return df

def main(st, iframe_style):
    iframe_style = {iframe_style}
    
    # Figure 1
    st.title("Financial Analysis")
    st.write("\n\n")
    
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[1]. HISTORY OF Tuition CHARGES: Original Vs. Actual</h4>
    """, unsafe_allow_html=True)
    st.subheader("* Two Consecutive School Years (Aug 2022 - May 2024)")
    # Use the st.write() function to display the iframe
    st.write(f'<iframe title="Total Revenue over 2 years" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiYjYxNTE4YWUtM2E0ZC00ODMyLThiMmMtZWUyYTE1YjExMGZhIiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)  
    st.subheader("Figure 1: Line Chart (PowerBI)")
    st.write("\n\n")
    st.subheader("Analysis")
    multi = '''
    The line graph tracks the history of monthly tuition charges over two consecutive school years (August 2022 - May 2024), comparing the original charges against the actual billing amounts 
    after discounts. There are three lines: the "Sum of Billing Amount," "Sum of Original Charge," and "Sum of Discount Amount," each representing the aggregated financial figures over time.
    
    - <strong>IMPORTANCE:</strong>
    It highlights the school’s financial trends and the impact of discounts on the overall revenue. From my experience working at this school for so many years, this is one of the
    most frequently asked for financial reports by ownership. Continuous checking and updating of this information on monthly basis is crucial to the school's financial health. 

    From the graph we can see the consistent gap between the original tuition charges and the actual billed amounts, indicating a steady application of discounts. 
    The "Sum of Discount Amount" remains relatively flat, suggesting a uniform discount strategy across the different discount types. 
    
    We notice a steep dip around Jun and July 2023 in both billed and original amounts. For the school's owners this could be interpreted as a large increase in student withdrawals,
    which raises their concern regarding the coverage of school's expenses during these months. However, from my experience, this is a normal and consistent trend during the summer time for 
    which may correlate with seasonal enrollment changes due to family travels. For the business owner, understanding these trends are crucial for financial planning, resource allocation,
    and re-evaluation of the current discounting strategy. Potential adjustments to tuition or discount policies may be considered to conpensate for revenue loss, especially during the 
    mid-year dips.  
    '''
    st.markdown(multi, unsafe_allow_html=True)
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 2
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[2]. HISTORY OF Tuition CHARGES By Qurater</h4>
    """, unsafe_allow_html=True)
    # Use the st.write() function to display the iframe
    st.write(f'<iframe title="Revenue by Querter" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiOWYxZDI5ZmUtMGIzZi00NmQwLWFjZTMtZTdmZDllZjM3NWY0IiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)  
    st.subheader("Figure 2: Line & Clustered Column Chart (PowerBI)")
    st.write("\n\n")
    st.subheader("Analysis")
    multi = '''
    Similar to Figure (1), this clusterd chart displays the same type of information in a different view by quarter. The main reason We included this graph is because we believe it provides 
    better visualization for the school's onwers to compare total revenues and understand the school's financial standing throughout the year. 
        '''
    st.markdown(multi, unsafe_allow_html=True)
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 3
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[3]. PROGRAM CONTRIBUTION TO REVENUE BY Schedule</h4>
    """, unsafe_allow_html=True)
    st.write("FD: Full Day (7:00 AM - 6:00 PM), SD: School Days (8:30 AM - 2:45 PM), HD: Half Days (8:30 AM - 12:00 PM)")
    # Use the st.write() function to display the iframe
    st.write(f'<iframe title="Program Schedules Revenue Contribution" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiNDkxYjVmNjQtYjRjYS00MDgyLWE1YmYtMDBlYzc2YTA0MTg1IiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)  
    st.subheader("Figure 3: Ribbon Chart (PowerBI)")
    st.write("\n\n")
    st.subheader("Analysis")
    multi = '''
    Figure (3) expands on the information provided by the earlier graphs by adding Programs and Schedules as color marks, enabling the comparison of programs and schedules contributions 
    to revenue. 
        '''
    st.markdown(multi, unsafe_allow_html=True)
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 4
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[4]. DISCOUNT DISTRIBUTION Over Two School Years</h4>
    """, unsafe_allow_html=True)
    st.subheader("* Two Consecutive School Years (Aug 2022 - May 2024)")
    # Use the st.write() function to display the iframe
    st.write(f'<iframe title="Discount Amount by Discount Type" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiNGUxODNiMGUtNzk4ZS00YjM4LTlhYzktYjllYjRhOTAwNmNhIiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)  
    st.subheader("Figure 4: Treemap (PowerBI)")
    st.write("\n\n")
    st.subheader("Analysis")
    multi = '''
    Figure (4) provides business owners with a closer look at the different discounts categories offered to families and deepening thier understanding of the gap difference between original 
    charges and billed amount. For example, by looking at the graph, we can see that Employee discount and Friends & Family discount show to be the highest discount rates offered both totalling
    to about $332K over two years. This is a huge amount and may need to be reevaluated. For example, the dataset shows that employees get a 100% discount on their children's tuition. While this 
    may help with the school's turnover rate by taking care of staff and showing them apprecaition, it is highly recommended that the school consisder an alternative offer, perhapse reducing the percetage 
    discount rate to compensate for some of the huge amout of employee discount. 
    
    Additionally, as much as it is important to revisit the discounting strategy and assess its sustainability as they significantly reduce revenue, business owners should know that discounts do also affect 
    student retention rate. Therefore, a well structured strategies that can balance between attractiveness to prospective and current families, and the financial viability of the institution, 
    are crucial for long-term success.
        '''
    st.markdown(multi, unsafe_allow_html=True)
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 5
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[5]. DISCOUNT DISTRIBUTION For Active Enrollments</h4>
    """, unsafe_allow_html=True)
    st.subheader("* Two Consecutive School Years (Aug 2022 - May 2024)")
    # Use the st.write() function to display the iframe
    st.write(f'<iframe width="1024" height="612" src="https://lookerstudio.google.com/embed/reporting/3716267f-7edf-4b56-9f90-1ddb3630af02/page/z3GyD" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>', unsafe_allow_html=True)  
    st.subheader("Figure 5: BUBBLE CHART (Google Looker Studio)")
    st.write("\n\n")
    st.subheader("Analysis")
    multi = '''
    The chart illustrates the number of students receiving each type of discount and the cumulative amount of each. For example, consider the orange bubble, which represents sibling discounts. 
    Around 350 students receive this discount, indicating that their siblings are also enrolled in the school. The total discount for this category accumulates to approximately $1000. Similarly, 
    each bubble represents a different discount category, with the size of the bubble indicating the total discount offered for that category.

    This graph provides valuable information for financial administrators or school representatives. They can quickly assess whether adjustments are needed in their discount campaigns based on 
    this data.
        '''
    st.markdown(multi, unsafe_allow_html=True)
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 6
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[6]. ORIGINAL CHARGE VS. BILLED AMOUNT For Active Enrollments</h4>
    """, unsafe_allow_html=True)
    st.write(f'<iframe src="https://vizhub.com/uzairnaeem015/2bc9ce8310ac4095964fee8c7d1714c4?mode=embed&embed=branded" width="1024" height="612" scrolling="no" frameborder="no"></iframe>', unsafe_allow_html=True)

    st.subheader("Figure 6: SCATTER PLOT (D3.js)")
    st.write("\n\n")
    st.subheader("Analysis")
    multi = '''
    The scatter plot with bubble chart above depicts the relationship between the original charge amount and the billing amount (the cost of student enrollment per month after applying discounts) for active students only.
    
    On the x-axis, we have the billing amount, while the y-axis represents the charge amount. The range starts from 0 and goes up to 1400, which is the maximum charge amount per month for student enrollment. 
    Different colors represent the program, with circle size indicating the applied discounted amount. Additionally, hovering over specific values provides additional information.
    
    This scatter plot aids in understanding the relationship between billing and charge amounts based on discounts. We observe that values in orange and red (representing Primary and Lower Elementary programs) 
    are more prevalent than any other program, as indicated by their larger bubble sizes. Consequently, one can quickly deduce that more discounts are offered under these programs than others. School administrators 
    can use this graph to identify which discount types to offer more of, or perhaps to consider discontinuing specific discounts if they've been offered to too many students already.
    
    Another valuable aspect of this data is its ability to highlight discount trends or outliers. For instance, we notice a reading indicating a discount of 1045, significantly reducing the billing amount to just 110. 
    This could be due to an accidental or incorrect discount entry in our system. Having these graphs helps us quickly identify and track such issues, ensuring our balance sheets remain accurate and minimizing the need 
    for extensive error searches. This way, we can easily assess the data and detect outliers.   
        '''
    st.markdown(multi, unsafe_allow_html=True)
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")  
    
    # Figure 7
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[7]. TUITION STAT SUMMARY For Active Enrollments</h4>
    """, unsafe_allow_html=True)
    
    # load dataset
    df = stat_summary_data(data=any)

    # Proceed with using df only after verifying the needed columns are present
    if 'Status' in df.columns:
        active_df = df[df['Status'] == 'Active']
        st.write("Data Overview for Active Enrollments:")
        st.write(active_df.describe().round(2))  # Show statistical summary for active enrollments
        st.subheader("Figure 7: Description Summary Table (Python)")
        st.write("\n\n")
    else:
        st.error("Required columns are missing from the data.")

    if __name__ == "__main__":
        main()
        
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 8
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[8]. AVERAGE PROGRAM BILLING BY MONTH</h4>
    """, unsafe_allow_html=True)
    
    df = confusion_matrix_data(data=any)
    
    heatmap_data = df.pivot_table(index='Program', columns='Date', values='Billing Amount', aggfunc='mean')
    fig, ax = plt.subplots(figsize=(10.24, 6.12))  # You create a Matplotlib figure and axis
    sns.heatmap(heatmap_data, annot=True, fmt=".0f", linewidths=.5, cmap="YlGnBu", ax=ax)
    # Format the dates on the x-axis to be month abbreviations
    ax.set_xticklabels([pd.to_datetime(date).strftime('%b %Y') for date in heatmap_data.columns])
    # Set labels and title
    ax.set_title("Average Program Billing Amount By Month")
    ax.set_xlabel("Date")
    ax.set_ylabel("Program")
    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45)
    # Ensure the plot is tight and nothing is cut off
    plt.tight_layout()
    # Display the plot in the Streamlit app
    st.pyplot(fig)

    st.subheader("Figure 8: Confusion Matrix (Seaborn)")
    st.write("\n\n")

    # Figure 9
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[9]. AVERAGE PROGRAM BILLING BY MONTH with Central Tendency</h4>
    """, unsafe_allow_html=True)

    df = read_original_data()
    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

    # Group by 'Program' and 'Date', then calculate the mean of 'Billing Amount'
    monthly_billing = df.groupby(['Program', pd.Grouper(key='Date', freq='M')])['Billing Amount'].mean().reset_index()

    # Create an interactive line plot using Plotly Express
    fig = px.line(monthly_billing, x='Date', y='Billing Amount', color='Program', 
                title='Program Billing Amount Over Months',
                labels={'Billing Amount': 'Average Billing Amount ($)', 'Date': 'Date'},
                markers=True)

    # Enhance the layout
    fig.update_layout(xaxis_title='Date',
                    yaxis_title='Average Billing Amount ($)',
                    xaxis_tickangle=-45,
                    xaxis=dict(tickformat='%b %Y'))  # Format x-axis tick labels to show abbreviated month and year

    # Show the plot in Streamlit
    st.plotly_chart(fig)
    st.subheader("Figure 9: Line Charge with Central Tendency Mark (Plotly Express)")
    st.write("\n\n")

    # Figure 10
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>[10]. BILLING-DISCOUNT DISTRIBUTION BY PROGRAM</h4>
    """, unsafe_allow_html=True)
    
    df = pairplot_data(data=any)
    # Assuming 'Program' is a categorical column and you want to color by it
    # Generate an interactive pairplot using Plotly Express
    fig = px.scatter_matrix(df,
                            dimensions=df.select_dtypes(include=['float', 'int']).columns,
                            color="Program",  # assuming 'Program' is a column in your DataFrame
                            height=1000, width=1000)
    


    fig.update_traces(diagonal_visible=True)  # Remove the histograms on the diagonal
    st.plotly_chart(fig)
    
    st.subheader("Figure 10: Interactive Pairplot (Ploty Express)")

    
