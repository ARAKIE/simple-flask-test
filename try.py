 #  اي حاجه في بايثون هيا عباره عن  object 
 # بيتكون من 
 # attributes  المغلومات 
 #Methods  الخصاءص االحاجه اللي بيقوم بيها 
 # يعني العربيه عباره عن  object gdih
 #Attributes  مودلها لونها سعرها
 #Methods  انها بتمشي تقف 
 

#class is a template for creating object [Blueprint]
#هو التيمبلت اللي بنشيء منه الاوبجكت بتاعي
# في اي كلاس لازم اعمل  define ب __init__
#
# __init__ تهيء الداتا بتاعتي للاوبكت اللي هنشءه
# #__init__ ب لازم يكون فيها argument اسمه  self
#مش شرط يبقي اسمه self  ممكن اي ارجيومنت من عندك عادي
# self للدلالة على أن المتغير أو الدالة تخص الكائن وليس ثابتًا عامً

# Polymorphism  متعدده الاوجه 
# نفس الميثود في مكان بتعمل حاجه وفي مكان تاني بتعمل حاجه اخري بس هسا نفس الميثود

#ُEncapsulation  نظام التغليف  بيعمل ريستريكت للاكسيس الخاص بالبيانات بتاعتي المتخزنه في ال Attirbutes & Method الموجوده في الكلاس بتاعي
# 3 حالات لظهور البيانت بتاعتي ال  puplic and protected and privat 
# معظم الشغل كان   piblic  واقدر اعدل عليه 

#
# Abstract
# 
# هو كلاس لا يمكن إنشاء كائن منه مباشرة، وإنما يتم استخدامه كـ قالب (Template) تُرث منه كلاسـات أخرى وتقوم بتطبيق وظائف معينة.

# ✅ يعني:

# هو كلاس يقول للكلاسات الأخرى:

# "لو عايز ترث مني، لازم تنفذ الدوال اللي أنا محددها كـ abstract"


# class Member:
#     def __init__(self): # السطر ده اسمه  constructor
        
        
#         pass


from abc import ABCMeta ,abstractmethod

class programming (metaclass = ABCMeta):
    
    @abstractmethod  # خاصه بازل كلاس بس
    def has_oop(self):
        pass
    
class Python(programming):
    def has_oop(self):
        return "yes"
    
class pascale(programming):
    def has_oop(self):
        return "no"
    
    
    
    
    
one = pascale()
print(one.has_oop())

   

      
