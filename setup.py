from setuptools import setup, find_packages

# this is will let ur whole project to be installed as a package and u can import it in other files 
# يسمح لك تحويل مشروعك إلى Python package قابلة للتثبيت بحيث تثبته بـ pip وتثبت معه المتطلبات تلقائيًا.


# يعني ثبت المشروع نفسه (اللي أنت فيه) كـ package بحيث أي تعديل بالكود ينعكس مباشرة بدون إعادة تثبيت.
HYPEN_DASHES = '-e .'

#فايدته يجيب المكتبات من requirements.txt ويشيل -e . لأنها تسبب مشاكل داخل setup.py
def get_requirements(file_path):
    with open(file_path) as f:
        requirements = f.read().splitlines()
    return [req for req in requirements if req != HYPEN_DASHES]


setup( 
    name='mlpro',
    version='0.0.1',
    author="Omar" ,
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')      

)