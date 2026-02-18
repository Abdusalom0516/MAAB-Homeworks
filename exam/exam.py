import ast
import pandas as pd
import re
import json

from models.profile_model import Profile

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


# Step 2.
# Har bir string columnning bo‘sh joylarini olib tashlash (strip).
df = df.apply(lambda col: col.str.strip() if col.dtype == "string" else col)

# Bo‘sh stringlarni NaN yoki Null bilan almashtirish.
df = df.replace("", "Null")

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


# Step 4: Email va phone validation

# Emaillarni kichik harflarga o‘tkazish va noto‘g‘ri formatdagi emaillarni aniqlash.
df["email"] = df["email"].str.lower()
invalid_emails = df["email"].str.fullmatch(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    na=False
)

df.loc[invalid_emails, "email"] = "invalid_email"

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

# df["father_income"] = df[]
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
    print(splitted_address)
    for elem in splitted_address:
        if re.match(r"^[A-Z]{1}[a-z]+$", elem):
            return elem
    return pd.NA

df["addr_postal"] = df["address_raw"].apply(extract_postal)
df["addr_district"] = df["address_raw"].apply(extract_district)
df["addr_city"] = df["address_raw"].apply(extract_city)

print(df.head(5).to_string())