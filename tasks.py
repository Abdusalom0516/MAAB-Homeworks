# Step 1: Data bilan tanishish
# CSV faylni ochib, birinchi 10 qatorni ko‘rish.
# Column nomlari va sonini tekshirish.
# Har bir columndagi missing values sonini aniqlash.
# Data turlari (string, numeric, date, json) haqida tushuncha hosil qilish.

# Step 2: Oddiy string tozalash
# Har bir string columnning bo‘sh joylarini olib tashlash (strip).
# Bo‘sh stringlarni NaN yoki Null bilan almashtirish.

# Step 3: Raqam va sanalarni tozalash
# Age, score, GPA, attendance, money_spent kabi numeric columnlarni tozalash va int yoki float formatiga
# keltirish.
# Date columnlarni pandas datetime formatiga o‘tkazish.

# Step 4: Email va phone validation
# Emaillarni kichik harflarga o‘tkazish va noto‘g‘ri formatdagi emaillarni aniqlash.
# Telefon raqamlarni tozalash va yagona standart formatga keltirish (masalan: +998...).

# Step 5: JSON parsing
# JSON columnlarini ochish (profile_json).
# JSON ichidagi ma’lumotlarni alohida columnlarga ajratish: hobbies, skills, family, devices.
# JSON ichidagi array yoki nested objectlarni tekshirish va flatten qilish.

# Step 6: Address parsing
# Address columnni alohida qism va key-larga ajratish: shahar, tuman, pochta kodi.
# Raw address columnni saqlab, yangi columnlar hosil qilish (addr_city, addr_district, addr_postal).

# Step 7: Duplicate va missing data tekshirish
# Duplicate rowsni aniqlash va o‘chirish.
# Muhim columnlarda missing values mavjudligini aniqlash va qaror qabul qilish (fillna yoki dropna).

# Step 8: Data normalization
# Gender columnini standard formatga keltirish: Male / Female / Unknown.
# Course columnlarini yagona nomga keltirish: Data Science / Python / Other.
# Status columnlarini standart formatga keltirish (lower-case yoki uniform).

# Step 9: Final type conversion va export
# Barcha columnlarning to‘g‘ri type da ekanligini tekshirish: string, int, float, datetime.
# Sanalarni yagona formatga keltirish (YYYY-MM-DD HH:MM:SS).
# Tozalangan data CSV faylga saqlash (super_dirty_students_cleaned.csv).

# Step 10: QA checks
# Original va cleaned row sonini solishtirish.
# Missing email va phone sonini tekshirish.
# Numeric columnlar (GPA, attendance, score) qiymatlari to‘g‘ri diapazonda ekanligini tekshirish.
# Duplicate rowlar yo‘qligini tasdiqlash.