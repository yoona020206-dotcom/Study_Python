import streamlit as st

import pandas as pd # 데이터 분석용 
import numpy as np # 데이터 분석용 

# random.randint(0, 100) : 0부터 100까지의 정수 중 랜덤으로 하나 선택
df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": [
            "https://roadmap.streamlit.app", 
            "https://extras.streamlit.app", 
            "https://issues.streamlit.app"
        ],
        "stars": [
            np.random.randint(0, 1000) for _ in range(3)
        ],
        "views_history": [
            [
                np.random.randint(0, 5000) for _ in range(30)
            ] for _ in range(3)
        ]
    }
)
st.title("DataFrame :innocent:")
st.dataframe(
    df,
    column_config={
        "name": "App name",
        "url": st.column_config.LinkColumn("App URL"),
        "stars": st.column_config.NumberColumn(
            "GitHub Stars", format="%d 🌠"),
        "views_history": st.column_config.LineChartColumn(
            "Views history", y_min=0, y_max=5000)
    },
    hide_index=True,
)


