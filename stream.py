import streamlit as st 
import matplotlib.pyplot as plt
import json
import streamlit.components.v1 as components
from wordcloud import WordCloud
st.set_page_config(page_title = "Concept Analysis: Biden Is Inaugurated as the 46th U.S. President")
st.title('Concept Analysis: Biden Is Inaugurated as the 46th U.S. President')
components.iframe("https://www.nytimes.com/video/us/politics/100000007558606/biden-inauguration-video.html?smid=url-share", width=800, height=800)


from PIL import Image
with open("concepts.json", 'r', encoding ='utf8') as f:
    collection_of_concepts = json.load(f)
with open("sentiment.json", 'r', encoding ='utf8') as f:
    collection_of_sentiments = json.load(f)
each_event_sent = collection_of_sentiments["each_message_sentiments"]
avg_sent = collection_of_sentiments["average_sentiment"]
event_to_filter = st.slider('hour', 1, len(each_event_sent)-1, len(each_event_sent)-1) 
print(event_to_filter)

fig = plt.figure()
avg_sent_plot_data = [float(value) for value in avg_sent[0:event_to_filter]]
each_sent_plot_data = [float(value) for value in each_event_sent[0:event_to_filter]]
plt.xlabel('Message')
plt.ylabel('Sentiment')
plt.plot([idx for idx, item in enumerate(each_sent_plot_data)], each_sent_plot_data, label='Each message sentiment')
plt.plot([idx for idx, item in enumerate(avg_sent_plot_data)], avg_sent_plot_data, label='Overall Average sentiment')
plt.legend()
st.pyplot(fig)
# fig = plt.figure()
# plt.style.use('ggplot')

# top20_concepts = list(collection_of_concepts.keys())[:20]
# top20_count = list(collection_of_concepts.values())[:20]
# x_pos = [i for i, _ in enumerate(top20_concepts)]

# plt.bar(x_pos, top20_count, color='green')
# plt.ylabel("Occurrences of a concept")
# plt.title("20 most common concepts in documents")

# plt.xticks(x_pos, top20_concepts, rotation='vertical')
# plt.show()
# st.plotly_chart(fig)

classification_word_cloud = WordCloud(width=800, height=600, background_color='white', colormap='tab10').generate_from_frequencies(collection_of_concepts)
# fig, ax = plt.figure(figsize=(15,5))
# # Display the generated image:
# plt.imshow(classification_word_cloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()

# st.pyplot()
st.image(classification_word_cloud.to_array())