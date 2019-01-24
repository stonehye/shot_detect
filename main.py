from __future__ import division
from detector import extract_shots_with_pyscenedetect
import glob

_FOLDER = "video"
pyscenedetect_threshold = 30

video_set = "./{}/*.mp4".format(_FOLDER)
cnt = 1
for video_path in glob.glob(video_set):
	print("Current Video: {}".format(video_path))
	psd_predictions = extract_shots_with_pyscenedetect(video_path, threshold=pyscenedetect_threshold, min_scene_length=15)
