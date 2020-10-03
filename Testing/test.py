from moviepy.editor import VideoFileClip, concatenate_videoclips
clip1 = VideoFileClip("Mood - 24kGoldn ft Iann Dior.mp4")
clip2 = VideoFileClip("Mood - 24kGoldn ft Iann Dior.mp3")
final_clip = concatenate_videoclips([clip1,clip2])
final_clip.write_videofile("my_concatenation.mp4")