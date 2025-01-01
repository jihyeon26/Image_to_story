from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_gps_info(image_path):
    # 이미지 로드
    image = Image.open(image_path)

    # EXIF 데이터 추출
    exif_data = image._getexif()

    # EXIF 데이터를 사람이 읽을 수 있도록 디코딩
    exif_info = {}
    if exif_data:
        for tag, value in exif_data.items():
            decoded_tag = TAGS.get(tag, tag)  # 태그 이름 디코딩
            exif_info[decoded_tag] = value

    # GPSInfo 추출
    gps_info = exif_info.get("GPSInfo")

    # GPS 정보 디코딩 및 반환
    if gps_info:
        decoded_gps_info = {}
        for gps_tag, gps_value in gps_info.items():
            decoded_tag = GPSTAGS.get(gps_tag, gps_tag)  # GPS 태그 디코딩
            decoded_gps_info[decoded_tag] = gps_value

        return decoded_gps_info
    else:
        return None
