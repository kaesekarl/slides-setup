import argparse
import json
import os
import shutil
import subprocess

# Use argparse to define and parse command-line arguments
parser = argparse.ArgumentParser(
    description="Slice animations from a presentation JSON file."
)
parser.add_argument(
    "root_dir",
    type=str,
    help="The root directory of the project containing the 'how2it' folder.",
)
args = parser.parse_args()

# Construct the paths based on the provided root directory
root_dir = args.root_dir
presentation_dir = os.path.join(root_dir, "presentation")
output_dir = os.path.join(root_dir, "sliced_animations")

# Location of json files
json_files = [f for f in os.listdir(presentation_dir) if f.endswith(".json")]
print(f"Processing JSON files: {json_files}")

# Clear out the output directory
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

for json_file in json_files:
    json_path = os.path.join(presentation_dir, json_file)

    # Load the JSON file
    with open(json_path, "r") as f:
        data = json.load(f)
        print(f"Loaded data from {json_path}")

    # Process each slide
    for slide in data["slides"]:
        slide_number = slide["number"]
        start_animation = slide["start_animation"]
        end_animation = slide["end_animation"]

        # Get the relevant MP4 files for this slide
        slide_files = data["files"][start_animation:end_animation]

        # Create a temporary text file for FFmpeg input
        input_txt = f"input_slide_{slide_number}.txt"
        with open(input_txt, "w") as f:
            for file in slide_files:
                # The video files are located relative to the presentation directory.
                abs_file_path = os.path.join(root_dir, file.lstrip("./"))
                f.write(f"file '{abs_file_path}'\n")

        # Output file path (inside the output directory)
        output_file_name = f"{json_file.rsplit('.', 1)[0]}_slide{slide_number}.mp4"
        output_file = os.path.join(output_dir, output_file_name)

        # FFmpeg command to concatenate the videos for this slide
        ffmpeg_command = [
            "ffmpeg",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            input_txt,
            "-c",
            "copy",
            output_file,
            "-y",
        ]

        # Run the FFmpeg command
        subprocess.run(ffmpeg_command)

        # Clean up the temporary input file
        os.remove(input_txt)

        print(f"Slide {slide_number} video created: {output_file}")

print("All slide videos created successfully! 🎉")
