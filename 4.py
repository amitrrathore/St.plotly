import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def line_plot(x1, y1, label):
        
        plt.plot(x1, y1, linewidth=1, marker='s', label=i)
        plt.legend()
        st.pyplot(fig)
st.write("""
# File Picker
""")
uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for file in uploaded_file:
        if file is not None:
                bytes_data = file.getvalue()
                data = file.getvalue().decode('utf-8').splitlines()         
                st.session_state["preview"] = ''






        df = pd.read_csv(file, sep="\t",header = None,names=range(82))
                        # print(df)
        df.columns=["Sample_Name","Sample_ID","Sample Type","Sample Comment","Set Number","Acquisition Method","Acquisition Date","Rack Type","Rack Position",
                        "Vial Position",
                        "Plate Type",
                        "Plate Position",
                        "File Name",
                        "Dilution Factor",
                        "Weight To Volume Ratio",
                        "Analyte Peak Name",
                        "Analyte Units",
                        "Analyte Peak Area (counts)",
                        "Analyte Peak Height (cps)",
                        "Analyte Concentration (ng/mL)",
                        "Analyte Retention Time (min)",
                        "Analyte Expected RT (min)",
                        "Analyte RT Window (sec)",
                        "Analyte Centroid Location (min)",
                        "Analyte Start Scan",
                        "Analyte Start Time (min)",
                        "Analyte Stop Scan",
                        "Analyte Stop Time (min)",
                        "Analyte Integration Type",
                        "Analyte Signal To Noise",
                        "Analyte Peak Width (min)",
                        "IS Peak Name",
                        "IS Units",
                        "IS Peak Area (counts)",
                        "IS Peak Height (cps)",
                        "IS Concentration (ng/mL)",
                        "IS Retention Time (min)",
                        "IS Expected RT (min)",
                        "IS RT Window (sec)",
                        "IS Centroid Location (min)",
                        "IS Start Scan",
                        "IS Start Time (min)",
                        "IS Stop Scan",
                        "IS Stop Time (min)",
                        "IS Integration Type",
                        "IS Signal To Noise",
                        "IS Peak Width (min)",
                        "Area Ratio",
                        "Relative Retention Time",
                        "Area Ratio",
                        "Calculated_Concentration",
                        "Accuracy (%)",
                        "Response Factor",
                        "Record Modified",
                        "Use Record",
                        "Standard Query Status",
                        "Analyte Mass Ranges (Da)",
                        "IS Mass Ranges (Da)",
                        "Sample Annotation",
                        "Height Ratio",
                        "Analyte Channel",
                        "IS Channel",
                        "Disposition",
                        "Analyte Annotation",
                        "Analyte Wavelength Ranges (nm)",
                        "Analyte Peak Area for DAD (mAU x min)",
                        "Analyte Peak Height for DAD (mAU)",
                        "IS Wavelength Ranges (nm)",
                        "IS Peak Area for DAD (mAU x min)",
                        "IS Peak Height for DAD (mAU)",
                        "Calculated Concentration for DAD (ng/mL)",
                        "Analyte Peak Width at 50% Height (min)",
                        "IS Peak Width at 50% Height (min)",
                        "Analyte Slope of Baseline (%/min)",
                        "IS Slope of Baseline (%/min)",
                        "Analyte Processing Alg.",
                        "IS Processing Alg.",
                        "Analyte Peak Asymmetry",
                        "IS Peak Asymmetry",
                        "Analyte Integration Quality",
                        "IS Integration Quality","NA"]
                        # print(df)


        df=df.dropna(subset=['Acquisition Date']).reset_index(drop=True)
        df=df.replace(to_replace=["No Peak","< 0"],
                                value=int(0))
        df.drop(df[df['Sample_Name'] == 'Sample_Name'].index, inplace = True)

        df = df.loc[:, ['Sample Comment','Sample_Name','Sample_ID','Calculated_Concentration','Sample Type','Sample Annotation']]
        df.drop(df[df['Sample Type'] != 'Unknown'].index, inplace = True)
                        # Sorting by column 'Country'

                        # df=df.sort_values('Sample ID',ascending=True)
                        # df=df.sort_values('Sample Name',ascending=True)
                        #df['Calculated_Concentration']=df.Calculated_Concentration.apply(np.float16) df=df.sort_values('Sample ID',ascending=True)
        df['Calculated_Concentration']=df.Calculated_Concentration.apply(np.float16)
        df['Sample_Name']=df.Sample_Name.apply(np.float16)
        df=df.sort_values(by=['Sample_ID','Sample_Name'],ascending=[True,True])
        df=df.drop(['Sample Type','Sample Annotation'],axis=1)
                        # df1=df.drop('Sample Name','Sample Type','sample Annotation',axis=1,3,3)

        list1=[]
        list2=[]
        list1=list(df['Sample_ID'])
        for i in list1:
                                if i not in list2:
                                        list2.append(i)
                                        x=len(list2)
                                if x==1 :
                                        a=list2[0]
                                if x==2:
                                        a=list2[0]
                                        b=list2[1]
                                if x==3:
                                        a=list2[0]
                                        b=list2[1]
                                        c=list2[2]
                                if x==4:
                                        a=list2[0]
                                        b=list2[1]
                                        c=list2[2]
                                        d=list2[3]
                                if x==5:
                                        a=list2[0]
                                        b=list2[1]
                                        c=list2[2]
                                        d=list2[3]
                                        e=list2[4]
                                if x==6:
                                        a=list2[0]
                                        b=list2[1]
                                        c=list2[2]
                                        d=list2[3]
                                        e=list2[4]
                                        f=list2[5]
                                # x1=df["Sample Comment"]
                                # y1=df["Calculated_Concentration"]
                                # fig, ax = plt.subplots()
        for i in list2:
                                fig1, ax = plt.subplots()
                                conc=df.loc[df["Sample_ID"]==i]
                                x1=conc['Sample Comment']
                                y1=conc['Calculated_Concentration']
                                label='i'
                                plt.plot(x1, y1, linewidth=1, marker='s', label=i)
                                plt.xticks(x1,labels=x1,rotation='vertical')
                                ax.xaxis.set_tick_params(labelsize=7)
                                plt.legend()
                                st.pyplot(fig1)


        fig, ax = plt.subplots()
        for i in list2:
                                conc=df.loc[df["Sample_ID"]==i]
                                x1=conc['Sample Comment']
                                y1=conc['Calculated_Concentration']
                                label='i'
                                
                                plt.plot(x1, y1, linewidth=1, marker='s', label=i)
                                plt.xticks(x1,labels=x1,rotation='vertical')
                                ax.xaxis.set_tick_params(labelsize=7)
                                plt.legend()
                                

        st.pyplot(fig)
                        
                                # ax.plot(x1, y1, label=i)
                                # line_plot(x1, y1, label)
                                
                        # ax.legend()
                        # st.pyplot(fig)
                        # line_plot(x1, y1, label)


                        

                        # st.pyplot(fig)
                        #  plt.plot(x1,y2)
                        # plt.legend()
                        # # plt.savefig('my_plot.png')
                        # plt.show()

