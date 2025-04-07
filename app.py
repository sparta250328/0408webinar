# simple_attendance_report.py
import streamlit as st
import pandas as pd
import io
import random

# サンプル従業員のリスト
employees = ["佐藤 ルタン", "鈴木 ルタ子", "田中 ルタ郎", "山田 ルタ郎", "高橋 ルタ美"]

# 日付の範囲（10日間）
dates = pd.date_range("2025-03-01", periods=10, freq="D")

# 勤怠データの生成
data = []
for name in employees:
    for date in dates:
        start_time = random.choice(["08:55", "09:00", "09:05", "09:10"])
        end_time = random.choice(["17:45", "18:00", "18:15", "18:30", "19:00"])
        remarks = random.choice(["", "", ""])
        data.append({
            "日付": date,
            "氏名": name,
            "出勤時刻": start_time,
            "退勤時刻": end_time,
            "勤務区分": "出勤",
            "備考": remarks
        })

# DataFrameに変換
df = pd.DataFrame(data)

# タイトル
st.title("SpartaHR")
menu = st.sidebar.radio("メニューを選択", ["勤怠管理", "組織管理", "社員検索", "設定"])

if menu == "勤怠管理":
    st.header("従業員の勤怠データ")
    # 表の表示
    st.dataframe(df, use_container_width=True)

    # CSVデータの準備とダウンロードボタン（Shift-JIS対応）
    csv_buffer = io.BytesIO()
    df.to_csv(csv_buffer, index=False, encoding="shift_jis")
    csv_buffer.seek(0)

    st.download_button(
        label="\U0001F4E5 CSVダウンロード（Shift-JIS）",
        data=csv_buffer,
        file_name="attendance_report.csv",
        mime="text/csv"
    )

elif menu == "組織管理":
    st.header("組織管理")
    st.write("組織管理の機能はまだ実装されていません。")

elif menu == "社員検索":
    st.header("社員検索")
    st.text_input("社員コードを入力してください", "")
    if st.button("検索"):
        # 検索結果の表示（ダミー）
        st.write("氏名: 佐藤 太郎")
        st.write("部署: 開発部")
        st.write("役職: エンジニア")
        st.write("グレード：4")
        st.write("入社日: 2023-01-01")

elif menu == "設定":
    st.header("設定")
    st.write("設定の機能はまだ実装されていません。")
