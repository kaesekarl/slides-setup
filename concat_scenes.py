import json
import subprocess
import os
import shutil

# Output directory for sliced animations
output_dir = "sliced_animations"

# Location of json files
location_json_files = "presentation"
json_files = [f for f in os.listdir(location_json_files) if f.endswith(".json")]
json_files = [f"{ f }" for f in json_files]
print(json_files)

# Clear out the output directory
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
    os.makedirs(output_dir)

for json_file in json_files:

    # Load the JSON file
    with open(f"presentation/{json_file}", "r") as f:
        data = json.load(f)
        print(data)

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
        output_file_name = f"{json_file.rsplit('.', 1)[0]}_slide{slide_number}.mp4"
        output_file = os.path.join(output_dir, output_file_name)

        # FFmpeg command to concatenate the videos for this slide
        ffmpeg_command = [
            "ffmpeg",
            "-f", "concat",          # Use the concat demuxer
            "-safe", "0",            # Allow unsafe file paths
            "-i", input_txt,         # Input file list
            "-c", "copy",            # Copy codec (no re-encoding)
            output_file,             # Output file
            "-y"
        ]

        # Run the FFmpeg command
        subprocess.run(ffmpeg_command)

        # Clean up the temporary input file
        subprocess.run(["rm", input_txt])

        print(f"Slide {slide_number} video created: {output_file}")

print("All slide videos created successfully!")
