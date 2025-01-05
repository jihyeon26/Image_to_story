from geopy.geocoders import Nominatim

def convert_to_decimal(ref, values):
    """
    GPS 데이터를 소수점 좌표로 변환합니다.

    Args:
        ref (str): 방향(위도: N/S, 경도: E/W)
        values (tuple): GPS 값 (도, 분, 초)

    Returns:
        float: 소수점 형식의 좌표
    """
    degrees, minutes, seconds = values
    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)

    # Ref에 따라 음수로 변환
    if ref in ['S', 'W']:
        decimal = -decimal

    return decimal

def get_location_from_gps_data(gps_data):
    """
    GPS 데이터를 입력받아 주소를 반환합니다.

    Args:
        gps_data (dict): GPS 데이터 딕셔너리

    Returns:
        str: 주소 정보
    """
    try:
        # 위도와 경도를 소수점 좌표로 변환
        latitude = convert_to_decimal(gps_data["GPSLatitudeRef"], gps_data["GPSLatitude"])
        longitude = convert_to_decimal(gps_data["GPSLongitudeRef"], gps_data["GPSLongitude"])

        # Nominatim 지오코더 초기화
        geolocator = Nominatim(user_agent="gps_locator")
        
        # 위도와 경도를 이용해 주소 검색
        location = geolocator.reverse((latitude, longitude))

        if location:
            return location.address
        else:
            return "주소 정보를 찾을 수 없습니다."
    except Exception as e:
        return f"오류 발생: {e}"