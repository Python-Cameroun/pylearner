from pathlib import Path
from hashlib import md5
from datetime import datetime
from pprint import pprint
import json


class CourseIndexGenerator:
    """This class build course index (index.json) for each course 
    in a specific folder."""
    
    base_folder = "E:\cours\Python"
    
    def __init__(self, *args, base_folder=None, **kwargs):
        self.base_folder = base_folder if base_folder != None\
            else CourseIndexGenerator.base_folder
        self.course_folders = {}
        self.current_path:Path = None
    
    def load_courses_folder(self):
        """This method loads all the courses path in the base folder"""
        bf = Path(self.base_folder)
        for x in bf.iterdir():
            if x.is_dir():
                self.course_folders[x.name] = {
                    "parts":[],
                    "chapters": [],
                    "full_path":x,
                    "name": x.name,
                    "date": str(datetime.today()),
                }
                
        return self.course_folders
    
    def build_all_courses(self):
        """This method build all the index (dictionary) of all the courses"""
        for key, value in self.course_folders.items():
            self.course_folders[key].update(self.build_course(value['full_path']))
    
    def build_course(self, path:Path):
        """This method build the index (dictionary) for only one course"""
        chapters = []
        parts = []
        self.current_path = path
        all_files = [x for x in path.iterdir() if x.name[0].isnumeric()]
        all_files = sorted(all_files, key=self.get_number)
        
        for x in all_files:
            if x.is_file():
                chapters.append(self.build_chapter(x))
            elif x.is_dir():
                parts.append(self.build_part(x))
        res = {'name':path.name, 'date':str(datetime.today()),
               'chapters':chapters, 'parts':parts,
               'full_path':path}
        return res
            
    def build_chapter(self, path:Path):
        """Build chapter with the path of the video"""
        with path.open('rb') as fp:
            #signa = md5(fp.read()).hexdigest()
            signa = ''
        name = path.name[3:]
        filepath = str(path).replace(str(self.current_path), '')
        number = self.get_number(path.name)
        return {'name':name, 'hash':signa, 'number':number, 'file':filepath}
    
    def build_part(self, path:Path):
        """Build a part from the path of the part's folder"""
        chapters = []
        all_files = [x for x in path.iterdir() if x.name[0].isnumeric()]
        all_files = sorted(all_files, key=self.get_number)
        
        for x in all_files:
            if x.is_file():
                chapters.append(self.build_chapter(x))
        name = path.name[3:]
        number = self.get_number(path.name)
        return {'name':name, 'number':number, 'chapters':chapters}
    
    def save_all(self):
        """Save the index (index.json) for all the courses."""
        for key in self.course_folders:
            self.save(key)
    
    def save(self, course_name):
        """Save the index for one course"""
        path = self.course_folders[course_name]['full_path']
        to_save = self.course_folders[course_name]
        del to_save['full_path']
        
        index = path / "index.json"
        with index.open("w") as fp:
            json.dump(to_save, fp, indent=4)
    
    def get_number(self, name:str):
        """Convenience method to get the number index of a chapter or part"""
        if isinstance(name, Path):
            name = name.name
        pos = name.find('.')
        return int(name[0:pos])
    
    
class CourseInderLoader:
    
    def __init__(self, index_file):
        with open(index_file) as fp:
            self.index:dict = json.load(fp)
            
    def name(self):
        return self.index['name']
            
    def get_parts(self):
        return self.index['parts']
    
    def get_chapters(self, part_name=None):
        if part_name is None:
            return self.index['chapters']
        else:
            for part in self.index['parts']:
                if part['name'] == part_name:
                    return part['chapters']
    
    
if __name__ == "__main__":
    gen = CourseIndexGenerator()
    gen.load_courses_folder()
    gen.build_all_courses()
    gen.save_all()
    
    loader = CourseInderLoader("E:\cours\Python\L'essentiel de Python 3/index.json")
    print(loader.name())
    pprint(loader.get_parts())
    print("==============")
    names = [part['name'] for part in loader.get_parts()]
    print(names)
    print(loader.get_chapters())
    for name in names:
        pprint(loader.get_chapters(name))
