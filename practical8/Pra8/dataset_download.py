from bing_image_downloader import downloader

# Create TRAIN dataset
downloader.download("fresh apple fruit", limit=60, output_dir='dataset/train', adult_filter_off=True)
downloader.download("fresh banana fruit", limit=60, output_dir='dataset/train', adult_filter_off=True)
downloader.download("fresh orange fruit", limit=60, output_dir='dataset/train', adult_filter_off=True)

# Create VALIDATION dataset
downloader.download("fresh apple fruit", limit=20, output_dir='dataset/val', adult_filter_off=True)
downloader.download("fresh banana fruit", limit=20, output_dir='dataset/val', adult_filter_off=True)
downloader.download("fresh orange fruit", limit=20, output_dir='dataset/val', adult_filter_off=True)