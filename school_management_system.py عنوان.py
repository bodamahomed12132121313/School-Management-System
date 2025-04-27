import pandas as pd

# قراءة قاعدة بيانات الطلاب
try:
    df = pd.read_csv('students.csv')
except FileNotFoundError:
    df = pd.DataFrame(columns=["الاسم", "السن", "الصف", "الدرجة"])

# إضافة طالب جديد
def add_student():
    name = input("ادخل اسم الطالب: ")
    age = int(input("ادخل سن الطالب: "))
    grade_level = input("ادخل الصف الدراسي: ")
    grade = float(input("ادخل الدرجة: "))
    new_student = {"الاسم": name, "السن": age, "الصف": grade_level, "الدرجة": grade}
    global df
    df = pd.concat([df, pd.DataFrame([new_student])], ignore_index=True)
    print(f"✅ تم إضافة الطالب {name} بنجاح!\n")

# عرض كل الطلاب
def view_students():
    print("\n📚 الطلاب المسجلين:")
    print(df)

# حذف طالب
def delete_student():
    name = input("ادخل اسم الطالب لحذفه: ")
    global df
    df = df[df["الاسم"] != name]
    print(f"🗑️ تم حذف الطالب {name} بنجاح!\n")

# تعديل درجة طالب
def edit_student_grade():
    name = input("ادخل اسم الطالب لتعديل درجته: ")
    if name in df["الاسم"].values:
        new_grade = float(input("ادخل الدرجة الجديدة: "))
        df.loc[df["الاسم"] == name, "الدرجة"] = new_grade
        print(f"✅ تم تعديل درجة {name} بنجاح!\n")
    else:
        print("❌ الطالب غير موجود.")

# فلترة الطلاب حسب الصف
def filter_by_grade_level():
    grade_level = input("ادخل الصف الدراسي لعرض الطلاب: ")
    filtered_df = df[df["الصف"] == grade_level]
    print(filtered_df)

# أعلى وأقل درجة
def show_top_bottom_students():
    if not df.empty:
        top_student = df[df["الدرجة"] == df["الدرجة"].max()]
        bottom_student = df[df["الدرجة"] == df["الدرجة"].min()]
        print("\n🏆 الطالب صاحب أعلى درجة:")
        print(top_student)
        print("\n🎯 الطالب صاحب أقل درجة:")
        print(bottom_student)
    else:
        print("🚫 لا توجد بيانات طلاب.")

# متوسط الدرجات
def show_average_grade():
    if not df.empty:
        average = df["الدرجة"].mean()
        print(f"\n📊 المتوسط العام للدرجات: {average:.2f}%")
    else:
        print("🚫 لا توجد بيانات لحساب المتوسط.")

# حفظ التغييرات
def save_changes():
    df.to_csv('students.csv', index=False, encoding='utf-8')
    print("💾 تم حفظ التغييرات!")

# القائمة الرئيسية
def main_menu():
    while True:
        print("\n🎯 نظام إدارة المدرسة - بوسيف")
        print("1️⃣ إضافة طالب")
        print("2️⃣ عرض كل الطلاب")
        print("3️⃣ حذف طالب")
        print("4️⃣ تعديل درجة طالب")
        print("5️⃣ فلترة الطلاب حسب الصف")
        print("6️⃣ عرض أعلى وأقل طالب")
        print("7️⃣ عرض المتوسط العام")
        print("8️⃣ حفظ التغييرات")
        print("9️⃣ خروج")

        choice = input("اختار عملية: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            edit_student_grade()
        elif choice == "5":
            filter_by_grade_level()
        elif choice == "6":
            show_top_bottom_students()
        elif choice == "7":
            show_average_grade()
        elif choice == "8":
            save_changes()
        elif choice == "9":
            save_changes()
            print("👋 مع السلامة يا بوسيف القائد!!")
            break
        else:
            print("❗️ خيار خاطئ. حاول تاني.")

# تشغيل البرنامج
if __name__ == "__main__":
    main_menu()