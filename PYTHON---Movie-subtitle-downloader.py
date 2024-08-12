import pysubdownloader as psd

def download_subtitle(movie_name):
    try:
        # Create a subtitle downloader object
        downloader = psd.SubtitleDownloader()
        
        # Search and download the subtitle
        subtitles = downloader.search_subtitles(movie_name)
        if subtitles:
            subtitle = subtitles[0]
            downloader.download_subtitle(subtitle)
            print(f"Subtitle downloaded successfully for: {movie_name} 🎉")
        else:
            print(f"No subtitles found for: {movie_name} 😞")
    except Exception as e:
        print(f"An error occurred: {e} 🚨")

if __name__ == "__main__":
    movie_name = input("Enter the name of the movie: ")
    download_subtitle(movie_name)
