from datetime import datetime

def get_current_datetime():
    now = datetime.now()
    formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date_time

if __name__ == "__main__":
    print("Current Date and Time:", get_current_datetime())
