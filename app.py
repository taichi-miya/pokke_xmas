import streamlit as st
from PIL import Image

# アプリのタイトル
st.title("写真データ処理アプリ")

# ファイルアップロード機能
uploaded_file = st.file_uploader("画像ファイルをアップロードしてください", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # アップロードされた画像を開く
    image = Image.open(uploaded_file)

    # アップロードされた画像を表示
    st.image(image, caption="アップロードされた画像", use_column_width=True)

    # 画像のサイズを表示
    st.write(f"画像サイズ: {image.size[0]} x {image.size[1]}")

    # 画像をグレースケールに変換する例
    if st.button("グレースケールに変換"):
        gray_image = image.convert("L")
        st.image(gray_image, caption="グレースケール画像", use_column_width=True)

    # 画像をダウンロードリンクとして提供する例
    st.download_button(
        label="画像をダウンロード",
        data=uploaded_file.getvalue(),
        file_name="processed_image.png",
        mime="image/png"
    )