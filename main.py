#-*- coding: utf-8 -*-
from __future__ import division
from detector import extract_shots_with_pyscenedetect
import glob
from utils import video2frames
import os

_FOLDER = "video"
pyscenedetect_threshold = 30

video_set = "./{}/*.mp4".format(_FOLDER)

video_num = len(glob.glob(video_set))
print("지정 폴더 내 검색된 파일 개수: {}".format(video_num))
print("")
complete_cnt = 1
for filename in os.listdir(b'./video'):
    print("------------------- {} / {} : {} -------------------".format(complete_cnt, video_num, filename.decode("utf-8")))
    video_path = os.path.join('.', _FOLDER, filename.decode("utf-8"))
    ext = os.path.splitext(video_path)[-1]
    if ext == '.mp4':
        shot_list = extract_shots_with_pyscenedetect(video_path, threshold=pyscenedetect_threshold, min_scene_length=15)
        # video2frames(video_path, shot_list)
        print("OK")
    else:
        print("Not .mp4")
    complete_cnt += 1

# for video_path in glob.glob(video_set):
#     print("------------------- {} / {} -------------------".format(complete_cnt, video_num))
#     print("Current Video: {}".format(video_path))
#     shot_list = extract_shots_with_pyscenedetect(video_path, threshold=pyscenedetect_threshold, min_scene_length=15)
#     # video2frames(video_path, shot_list)
#     print("OK")
#     complete_cnt+=1

print("Complete!")
