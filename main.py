from __future__ import division
from detector import extract_shots_with_pyscenedetect
import glob
from utils import video2frames

_FOLDER = "video"
pyscenedetect_threshold = 30

video_set = "./{}/*.mp4".format(_FOLDER)
cnt = 1
video_num = len(glob.glob(video_set))
for video_path in glob.glob(video_set):
	print("------------------- {} / {} -------------------".format(cnt, video_num))
	print("Current Video: {}".format(video_path))
	shot_list = extract_shots_with_pyscenedetect(video_path, threshold=pyscenedetect_threshold, min_scene_length=15)
	# video2frames(video_path, shot_list)
	print("OK")
	cnt+=1
print("Complete!")
