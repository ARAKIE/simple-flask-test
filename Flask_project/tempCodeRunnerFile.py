from flask import Flask, render_template

# # إنشاء التطبيق
# skills_app = Flask(__name__)
# my_skills = [("html" ,80) , ("css" ,22) , ("python" ,50) , ("Mysql" ,92) , ("Go" ,50)]

# # الصفحة الرئيسية
# @skills_app.route("/")
# def homepage():
#     return render_template("homepage.html", pagetitle="homepage" , custom_css="home")

# # صفحة about
# @skills_app.route("/about")
# def about():
#     return render_template("about.html", pagetitle="about")


# @skills_app.route("/add")
# def add():
#     return render_template("add.html", pagetitle="add" ,custom_css="add")

# @skills_app.route("/skills")
# def skills():
#     return render_template("skills.html", pagetitle="skills" ,page_head ="my_skills" , description = "this is my skill page" , skills =my_skills,
#      custom_css="skills")


# # تشغيل السيرفر
# if __name__ == "__main__":
#     skills_app.run(debug=True, port=9000)
