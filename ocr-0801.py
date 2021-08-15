print("Hello world_0815!")
import streamlit as st
import json, os, requests,io
import pandas as pd
from PIL import Image, ImageFont, ImageDraw
import pprint
#
sub_key = "36346aa482da4cf0aa867dde1f3fe681"
ocr_api_url = "https://cog-com-v-0724.cognitiveservices.azure.com/vision/v3.2/ocr"

st.title('画像の文字起こしアプリ')
st.write('アップロードされた画像の文字を認識し表示するアプリです。')

uploaded_file = st.file_uploader("choose an Image...")

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    with io.BytesIO()as output:
        img.save(output,format='JPEG')
        binary_img = output.getvalue()
        
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': sub_key
        }
    params = {
        'language': 'ja'
        }
    res = requests.post(ocr_api_url,params=params,headers=headers,data=binary_img)
    data = res.json()
    mylist = []
    #pprint.pprint(data['regions'][0]['lines'])
    for i in data['regions'][0]['lines']:
        for j in i['words']:
            k = j['text']
#            print(j['text'],end="")
            mylist.append(k)
#    mylist2 = join(mylist)
    st.subheader('↓認識した文字↓')
    st.write("".join(mylist))
#    df = pd.DataFrame(data['regions'][0]['lines'])
#    st.write(df.words)
    #print(data)
#    results = res.json()
#    print(results)

    st.image(img,caption='uploded image',use_column_width=True)
