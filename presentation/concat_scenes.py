import json
import subprocess
import os

# Output directory for sliced animations
output_dir = "sliced_animations"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the JSON file
with open("presentation/Scene3.json", "r") as f:
    data = json.load(f)

# Extract the list of MP4 files
mp4_files = data["files"]

# Process each slide
for slide in data["slides"]:
    slide_number = slide["number"]
    start_animation = slide["start_animation"]
    end_animation = slide["end_animation"]

    # Get the relevant MP4 files for this slide
    slide_files = mp4_files[start_animation:end_animation]

    # Create a text file for FFmpeg input
    input_txt = f"input_slide_{slide_number}.txt"
    with open(input_txt, "w") as f:
        for file in slide_files:
            f.write(f"file '{file}'\n")

    # Output file path (inside the output directory)
    output_file = os.path.join(output_dir, f"slide_{slide_number}.mp4")

    # FFmpeg command to concatenate the videos for this slide
    ffmpeg_command = [
        "ffmpeg",
        "-f", "concat",          # Use the concat demuxer
        "-safe", "0",            # Allow unsafe file paths
        "-i", input_txt,         # Input file list
        "-c", "copy",            # Copy codec (no re-encoding)
        output_file              # Output file
    ]

    # Run the FFmpeg command
    subprocess.run(ffmpeg_command)

    # Clean up the temporary input file
    subprocess.run(["rm", input_txt])

    print(f"Slide {slide_number} video created: {output_file}")

print("All slide videos created successfully!")
