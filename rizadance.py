import subprocess
import sys


def install_moviepy():
    try:
        import moviepy
    except ImportError:
        print("MoviePy не установлен. Установка...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "moviepy"])
        print("Установка завершена.")

def main():
    install_moviepy()
    from moviepy.editor import VideoFileClip, concatenate_videoclips

    
    # или другой абсолютный путь к файлу

    try:
        video = VideoFileClip("dance.gif")
        video = video.resize((150, 100))
        video = video.set_audio(None)
        final_video = concatenate_videoclips([video] * 100)  
        final_video.preview()
    except ValueError as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()
    input("Нажмите Enter, чтобы закрыть...")
