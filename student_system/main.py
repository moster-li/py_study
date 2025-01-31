import json
import os
import logging
import sys

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 文件路径
INFO_FILE = "D:\\py_project\\student_system\\info"
STUDENTS_FILE = "D:\\py_project\\student_system\\students.json"
ADMIN_ACCOUNT = "230341320"
ADMIN_PASSWORD = "230341320"

class Student:
    def __init__(self, name, number, sex, age):
        self.name = name
        self.number = number
        self.sex = sex
        self.age = age

    def to_dict(self):
        return {
            "name": self.name,
            "number": self.number,
            "sex": self.sex,
            "age": self.age
        }

def users(user_info):
    user_name, user_password = user_info
    dictionary = {user_name: user_password}

    try:
        with open(INFO_FILE, 'a+', encoding='utf-8') as file_object:
            file_object.seek(0)
            lines = file_object.readlines()
            account_exists = False
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                try:
                    line_dict = json.loads(line)
                    if user_name in line_dict:
                        account_exists = True
                        stored_password = line_dict[user_name]
                        if stored_password == user_password:
                            logging.info("账号和密码匹配")
                            return True
                        else:
                            logging.error("密码错误")
                            return False
                except json.JSONDecodeError:
                    logging.error("文件中存在无效的 JSON 数据")

            if not account_exists:
                # 需要管理员验证
                admin_user = input("需要管理员权限创建新账号，请输入管理员账号：")
                admin_pass = input("请输入管理员密码：")
                if admin_user == ADMIN_ACCOUNT and admin_pass == ADMIN_PASSWORD:
                    file_object.write(json.dumps(dictionary) + '\n')
                    logging.info("新账号创建成功")
                    return True
                else:
                    logging.error("管理员验证失败")
                    return False
    except FileNotFoundError:
        logging.error("存储账号信息的文件未找到")
        return False

def log_in():
    user_input = input("请输入账号：")
    password_input = input("请输入密码：")
    return user_input, password_input

class StudentMassageSystem:
    def __init__(self):
        self.students = self.load_students()

    def load_students(self):
        try:
            if os.path.exists(STUDENTS_FILE):
                with open(STUDENTS_FILE, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    return [Student(**student) for student in data]
            return []
        except json.JSONDecodeError:
            logging.error("学生信息文件存在无效的 JSON 数据")
            return []

    def save_students(self):
        student_dicts = [student.to_dict() for student in self.students]
        with open(STUDENTS_FILE, 'w', encoding='utf-8') as file:
            json.dump(student_dicts, file, ensure_ascii=False, indent=4)

    def add_info(self):
        name = input("请输入学生姓名：")
        number = input("请输入学生学号：")
        sex = input("请输入学生性别：")
        age = int(input("请输入学生年龄："))
        student = Student(name, number, sex, age)
        self.students.append(student)
        self.save_students()
        logging.info("学生信息添加成功")

    def delete_info(self):
        number = input("请输入要删除的学生学号：")
        for student in self.students:
            if student.number == number:
                self.students.remove(student)
                self.save_students()
                logging.info("学生信息删除成功")
                return
        logging.warning("未找到该学号的学生信息")

    def search_info(self):
        number = input("请输入要查询的学生学号：")
        for student in self.students:
            if student.number == number:
                print(f"姓名：{student.name}，学号：{student.number}，性别：{student.sex}，年龄：{student.age}")
                return
        logging.warning("未找到该学号的学生信息")

    def change_info(self):
        number = input("请输入要修改的学生学号：")
        for student in self.students:
            if student.number == number:
                name = input(f"请输入新的姓名（原姓名：{student.name}），不修改请直接回车：")
                if name:
                    student.name = name
                sex = input(f"请输入新的性别（原性别：{student.sex}），不修改请直接回车：")
                if sex:
                    student.sex = sex
                age_str = input(f"请输入新的年龄（原年龄：{student.age}），不修改请直接回车：")
                if age_str:
                    student.age = int(age_str)
                self.save_students()
                logging.info("学生信息修改成功")
                return
        logging.warning("未找到该学号的学生信息")

    def run(self):
        while True:
            user_choice = input("请输入操作功能：\n1--添加\n2--删除\n3--修改\n4--查询\n5--退出\n")
            if user_choice == "5":
                break
            choice_map = {
                "1": self.add_info,
                "2": self.delete_info,
                "3": self.change_info,
                "4": self.search_info
            }
            if user_choice in choice_map:
                choice_map[user_choice]()
            else:
                logging.warning("无效的选择，请重新输入。")

if __name__ == "__main__":
    if not users(log_in()):
        logging.error("认证失败，程序终止")
        sys.exit(1)
    system = StudentMassageSystem()
    system.run()