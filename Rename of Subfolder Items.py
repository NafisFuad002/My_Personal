import os

# মূল ফোল্ডার যেখানে সাবফোল্ডারগুলো আছে
main_dir = r"D:\CPP Codes\Codeforce\Problemset"

for folder in os.listdir(main_dir):
    folder_path = os.path.join(main_dir, folder)
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            ext = os.path.splitext(file)[1]  # যেমন: .cpp, .exe
            new_file_path = os.path.join(folder_path, folder + ext)
            os.rename(file_path, new_file_path)

print("All files renamed successfully.")
