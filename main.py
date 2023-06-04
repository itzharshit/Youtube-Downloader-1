import random
import streamlit as st
from pytube import YouTube, Playlist, Channel

# Function for some random animations
def random_celeb():
    return random.choice([st.balloons()])

import os

# Function to download YouTube single videos
def video(url):
    video_caller = YouTube(url)
    st.info(video_caller.title, icon="ℹ️")
    video_file = video_caller.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if video_file is not None:
        video_file.download(filename='video')
        st.success('Done!')
        file_path = os.path.join(os.getcwd(), 'video.mp4')
        print("File path:", file_path)  # Debug print statement
        with open(file_path, 'rb') as file:
            st.download_button('Download Video', file)

# Function for downloading YouTube playlist
def playlist(url):
    playlist_obj = Playlist(url)
    st.info('Number of videos in playlist: %s' % len(playlist_obj.video_urls), icon="ℹ️")
    for video in playlist_obj.videos:
        x = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if x is not None:
            x.download(filename='video')
            st.success('Done!')
            file_path = os.path.join(os.getcwd(), 'video.mp4')
            print("File path:", file_path)  # Debug print statement
            with open(file_path, 'rb') as file:
                st.download_button('Download Video', file)

# Function for downloading YouTube channel
def channel(url):
    channel_videos = Channel(url)
    st.info(f'Downloading videos by: {channel_videos.channel_name}', icon="ℹ️")
    for video in channel_videos.videos:
        z = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if z is not None:
            z.download(filename='video')
    st.success('Done!')
    file_path = os.path.join(os.getcwd(), 'video.mp4')
    print("File path:", file_path)  # Debug print statement
    with open(file_path, 'rb') as file:
        st.download_button('Download Channel', file)





# Integration of all above-defined functions
st.title("YouTube Downloader")
url = st.text_input(label="Paste your YouTube URL")
if st.button("Download"):
    if url:
        try:
            with st.spinner("Loading..."):
                if 'playlist' in url:
                    playlist(url)
                elif '@' in url:
                    channel(url)
                else:
                    video(url)
            random_celeb()
        except Exception as e:
            st.error(e)

