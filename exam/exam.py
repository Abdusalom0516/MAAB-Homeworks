import ast
import pandas as pd
import re
import json

from models.profile_model import Profile

print("------- Step 1 -------")

# Step 1.
# Reading csv file using pandas
df = pd.read_csv("super_dirty_students.csv")

# Data Info
df_info = df.info()
print(df_info)

# Top 10 values
# print(df.head(10))
print("-"*50)

df_columns = df.columns
df_data_per_column = df.count()
missing_values_count_per_column = df.isna().sum()
df_columns = df.columns

# Column Names
print(df_columns)
print("-"*50)

# Data Count Per Columns
print(df_data_per_column)
print("-"*50)

# Misson Values Count Per Column
print(missing_values_count_per_column)
print("-"*50)

# Convertion columns from object to string and numeric type
numeric_converted = df.apply(lambda col: pd.to_numeric(col, errors="coerce"))
numeric_ratio = numeric_converted.notna().mean().sort_values(ascending=False)

numeric_columns = numeric_ratio[numeric_ratio >= 0.6].index.tolist()
string_columns = numeric_ratio[numeric_ratio < 0.6].index.tolist()

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

for column in string_columns:
    df[column] = df[column].astype("string")

print(df.info())


print("------- Step 2 -------")
# Step 2.
# Har bir string columnning bo‘sh joylarini olib tashlash (strip).
df = df.apply(lambda col: col.str.strip() if col.dtype == "string" else col)

# Bo‘sh stringlarni NaN yoki Null bilan almashtirish.
df = df.replace("", "Null")


print("------- Step 3 -------")
# Step 3
df["money_spent"] = df["money_spent"].str.replace(r"[^\d.]", "", regex=True)

units = {
    "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5,
    "six":6, "seven":7, "eight":8, "nine":9
}

tens = {
    "ten":10, "twenty":20, "thirty":30, "forty":40,
    "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90
}


def words_to_number(text):
    if pd.isna(text):
        return pd.NA

    text = str(text).lower().strip()

    if re.fullmatch(r"\d+(\.\d+)?", text):
        if  float(text).is_integer():
            return int(float(text))
        return float(text)

    text = re.sub(r"[^\w\s]", "", text)

    parts = text.split()

    total = 0
    for word in parts:
        if word in tens:
            total += tens[word]
        elif word in units:
            total += units[word]
        else:
            return pd.NA

    return total if total != 0 else pd.NA

df["age"] = df["age"].astype("string").str.strip().str.lower()
df["score"] = df["score"].astype("string").str.strip().str.lower()

df["age"] = df["age"].apply(words_to_number)
df["score"] = df["score"].apply(words_to_number)

df["date_of_join"] = df["date_of_join"].astype("object")
df["event_time"] = df["event_time"].astype("object")

# True False Series
not_normal_date_time_series = df["date_of_join"].astype("string").str.fullmatch(r"\d+")

df.loc[not_normal_date_time_series, "date_of_join"] = pd.to_datetime(
    df.loc[not_normal_date_time_series, "date_of_join"], # Converting to data_time where the values of series is true and using that seriees index
    unit="s",
    errors="coerce"
)

df.loc[~not_normal_date_time_series, "date_of_join"] = pd.to_datetime(
    df.loc[~not_normal_date_time_series, "date_of_join"], # Converting to data_time where the values of series is false and using that seriees index
    errors="coerce"
)

# Date columnlarni pandas datetime formatiga o‘tkazish.
not_normal_date_time_series = df["event_time"].astype("string").str.fullmatch(r"\d+")

df.loc[not_normal_date_time_series, "event_time"] = pd.to_datetime(
    df.loc[not_normal_date_time_series, "event_time"], # Converting to data_time where the values of series is true and using that seriees index
    unit="s",
    errors="coerce"
)

df.loc[~not_normal_date_time_series, "event_time"] = pd.to_datetime(
    df.loc[~not_normal_date_time_series, "event_time"], # Converting to data_time where the values of series is false and using that seriees index
    errors="coerce"
)

print(df.head(1).to_string())

df["attendance"] = df["attendance"].astype("string").str.replace(r"[^\d.]", "", regex=True)
df["attendance"] = pd.to_numeric(df["attendance"], errors="coerce")


print("------- Step 4 -------")
# Step 4: Email va phone validation
# Emaillarni kichik harflarga o‘tkazish va noto‘g‘ri formatdagi emaillarni aniqlash.
df["email"] = df["email"].str.lower()
valid_emails = df["email"].str.fullmatch(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    na=False # Will be automaticly False if na
)

df.loc[~valid_emails & df["email"].notna(), "email"] = "invalid_email"

print(df.head(1).to_string())


# Telefon raqamlarni tozalash va yagona standart formatga keltirish (masalan: +998...).

df["phone"] = df["phone"].replace(r"\D", "", regex=True)

def normalize_uz_phone(num):
    if pd.isna(num) or num == "":
        return pd.NA

    if num.startswith("998"):
        local = num[3:]
    elif num.startswith("00"):
        local = num[2:]
    elif len(num) >= 9:
        local = num[-9:]
    else:
        return pd.NA

    if len(local) != 9:
        return pd.NA

    return "+998" + local

df["phone"] = df["phone"].apply(normalize_uz_phone)
print(df.head(1).to_string())


print("------- Step 5 -------")
# Step 5: JSON parsing
# JSON columnlarini ochish (profile_json).
# JSON ichidagi ma’lumotlarni alohida columnlarga ajratish: hobbies, skills, family, devices.
# JSON ichidagi array yoki nested objectlarni tekshirish va flatten qilish.

def extract_hobbies(profile_text):
    if pd.isna(profile_text):
        return pd.NA

    try:
        data = ast.literal_eval(profile_text) # Here I converting json into usable data

        profile = Profile.from_dict(data) # Here I am converting data into profile class

        return profile.hobbies

    except (ValueError, SyntaxError, KeyError, TypeError):
        return pd.NA


def extract_skills(profile_text):
    if pd.isna(profile_text):
        return pd.NA

    try:
        data = ast.literal_eval(profile_text) # Here I converting json into usable data

        profile = Profile.from_dict(data) # Here I am converting data into profile class

        return profile.skills.to_dict()

    except (ValueError, SyntaxError, KeyError, TypeError):
        return pd.NA

def extract_family(profile_text):
    if pd.isna(profile_text):
        return pd.NA

    try:
        data = ast.literal_eval(profile_text) # Here I converting json into usable data

        profile = Profile.from_dict(data) # Here I am converting data into profile class

        return profile.family.to_dict()

    except (ValueError, SyntaxError, KeyError, TypeError):
        return pd.NA

def extract_devices(profile_text):
    if pd.isna(profile_text):
        return pd.NA

    try:
        data = ast.literal_eval(profile_text) # Here I converting json into usable data

        profile = Profile.from_dict(data) # Here I am converting data into profile class

        return [d.to_dict() for d in profile.devices]

    except (ValueError, SyntaxError, KeyError, TypeError):
        return pd.NA

df["hobbies"] = df["profile_json"].apply(extract_hobbies)
df["skills"] = df["profile_json"].apply(extract_skills)
df["family"] = df["profile_json"].apply(extract_family)
df["devices"] = df["profile_json"].apply(extract_devices)

print(df.head(1).to_string())

# {
# 'hobbies': ['gun', 'nice'],
# 'skills': {'tech': {'python': 2, 'excel': 5, 'sql': 1}, 'soft': ['with', 'onto']},
# 'family': {'siblings': 4, 'income': {'father': 1198, 'mother': 1089}},
# 'devices': [{'type': 'laptop', 'brand': 'HP', 'year': 2021}, {'type': 'phone', 'brand': 'Xiaomi', 'year': 2021}]
# }

df["siblings"] = df["family"].apply(
    lambda value: value["siblings"] if isinstance(value, dict) else pd.NA
)

df["father_income"] = df["family"].apply(
    lambda value: value.get("income", {})["father"] if isinstance(value, dict) else pd.NA
)

df["mother_income"] = df["family"].apply(
    lambda value: value.get("income", {})["mother"] if isinstance(value, dict) else pd.NA
)

df["soft_skills"] = df["skills"].apply(
    lambda value: value["soft"] if isinstance(value, dict) else pd.NA
)

df["python_skill"] = df["skills"].apply(
    lambda value: value.get("tech", {}).get("python") if isinstance(value, dict) else pd.NA
)

df["excel_skill"] = df["skills"].apply(
    lambda value: value.get("tech", {}).get("excel") if isinstance(value, dict) else pd.NA
)

df["sql_skill"] = df["skills"].apply(
    lambda value: value.get("tech", {}).get("sql") if isinstance(value, dict) else pd.NA
)

print(df.head(1).to_string())


print("------- Step 6 -------")
# Step 6: Address parsing
# Address columnni alohida qism va key-larga ajratish: shahar, tuman, pochta kodi.
# Raw address columnni saqlab, yangi columnlar hosil qilish (addr_city, addr_district, addr_postal).

df["address_raw"] = df["address_raw"].replace("BROKEN,ADDRESS,DATA,,,", pd.NA)

def extract_postal(raw_address):
    if not isinstance(raw_address, str):
        return pd.NA

    splitted_address = raw_address.split(", ")
    if "," not in raw_address:
        splitted_address = raw_address.split(" ")
    for elem in splitted_address:
        if re.match(r"^\d{6}$", elem):
            return elem
    return pd.NA

def extract_district(raw_address):
    if not isinstance(raw_address, str):
        return pd.NA

    splitted_address = raw_address.split(", ")
    if "," not in raw_address:
        splitted_address = raw_address.split(" ")
    for elem in splitted_address:
        if re.match(r"[A-Za-z\s]+district$", elem):
            return elem
    return pd.NA


def extract_city(raw_address):
    if not isinstance(raw_address, str):
        return pd.NA

    splitted_address = raw_address.split(", ")
    if "," not in raw_address:
        splitted_address = raw_address.split(" ")
    for elem in splitted_address:
        if re.match(r"^[A-Z]{1}[a-z]+$", elem):
            return elem
    return pd.NA

df["addr_postal"] = df["address_raw"].apply(extract_postal)
df["addr_district"] = df["address_raw"].apply(extract_district)
df["addr_city"] = df["address_raw"].apply(extract_city)

print(df.head(1).to_string())


print("------- Step 7 -------")
# Step 7: Duplicate va missing data tekshirish
# Duplicate rowsni aniqlash va o‘chirish.
# Muhim columnlarda missing values mavjudligini aniqlash va qaror qabul qilish (fillna yoki dropna).

df = df.drop(["profile_json", "skills", "family", "devices"], axis=1) # Those columsn are unnecessayr

df["hobbies"] = df["hobbies"].apply(lambda x: ", ".join(x) if isinstance(x, list) else x) # Here I had to convert list into string
df["soft_skills"] = df["soft_skills"].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)

df = df.drop_duplicates() # Removing duplicates with this method

df = df.dropna(subset=["student_id"])


important_cols = [
    "student_id",
    "course",
    "status",
    "date_of_join"
]



print("------- Step 8 -------")
# Step 8: Data normalization
# Gender columnini standard formatga keltirish: Male / Female / Unknown.
# Course columnlarini yagona nomga keltirish: Data Science / Python / Other.
# Status columnlarini standart formatga keltirish (lower-case yoki uniform).

def gender_fix(gender):
    if not isinstance(gender, str):
        return "Unknown"

    gender = gender.lower()

    if "f" in gender:
        return "Female"
    elif "male" in gender or "m":
        return "Male"
    else:
        return "Unknown"


df["gender"] = df["gender"].apply(gender_fix)


def status_fix(status):
    if not isinstance(status, str):
        return pd.NA
    else:
        return status.lower()

df["status"] = df["status"].apply(status_fix)

def fix_course(course):
    if not isinstance(course, str):
        return "Other"

    course = course.lower()

    if "data" in course or "science" in course:
        return "Data Science"
    elif "python" in course or "py" in course:
        return "Python"
    else:
        return "Other"

df["course"] = df["course"].apply(fix_course)

print(df["course"].head(10).to_string())


print("------- Step 9 -------")
# Step 9: Final type conversion va export
# Barcha columnlarning to‘g‘ri type da ekanligini tekshirish: string, int, float, datetime.
# Sanalarni yagona formatga keltirish (YYYY-MM-DD HH:MM:SS).
# Tozalangan data CSV faylga saqlash (super_dirty_students_cleaned.csv).

numeric_cols = [
    "age", "gpa", "money_spent", "score", "addr_postal",
    "siblings", "father_income", "mother_income",
    "python_skill", "excel_skill", "sql_skill"
]

df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

string_cols = [
    "name", "gender", "phone", "email",
    "course", "status", "remarks",
    "addr_district", "addr_city"
]

df[string_cols] = df[string_cols].astype("string")

date_cols = ["date_of_join", "event_time"]

df[date_cols] = df[date_cols].apply(pd.to_datetime, errors="coerce")

df.to_csv("super_dirty_students_cleaned.csv")


print("------- Step 10 -------")
# Step 10: QA checks
# Original va cleaned row sonini solishtirish.
# Missing email va phone sonini tekshirish.
# Numeric columnlar (GPA, attendance, score) qiymatlari to‘g‘ri diapazonda ekanligini tekshirish.
# Duplicate rowlar yo‘qligini tasdiqlash.

original_df = pd.read_csv("super_dirty_students.csv")
original_rows = original_df.shape[0]
cleaned_rows = df.shape[0]

print("Original rows:", original_rows)
print("Cleaned rows :", cleaned_rows)
print("Removed rows :", original_rows - cleaned_rows)

print("Missing emails:", df["email"].isna().sum())
print("Missing phones:", df["phone"].isna().sum())
print("Invalid emails", df[df["email"] == "invalid_email"]["email"].count())

invalid_gpa = df[(df["gpa"] < 0) | (df["gpa"] > 4)]
print("Invalid GPA rows:", len(invalid_gpa))

invalid_score = df[(df["score"] < 0) | (df["score"] > 100)]
print("Invalid Score rows:", len(invalid_score))

invalid_attendance = df[(df["attendance"] < 0) | (df["attendance"] > 100)]
print("Invalid Attendance rows:", len(invalid_attendance))

duplicates = df.duplicated().sum()
print("Duplicate rows:", duplicates)
