import pandas as pd
import re

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

# Date columnlarni pandas datetime formatiga o‘tkazish.

print(df.head(1).to_string())


