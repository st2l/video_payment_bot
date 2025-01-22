from asgiref.sync import sync_to_async
from robot.models import Video
from random import randint


async def send_video():
    all_videos = await sync_to_async(Video.objects.all, thread_sensitive=True)()
    all_vids = []
    async for vid in all_videos:
        all_vids.append(vid.video)
        print(str(vid.video))
    video = all_vids[randint(0, len(all_videos) - 1)]
    return video
