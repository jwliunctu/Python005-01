#!/usr/bin/env python
#
# 背景：在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫、狗四个类。
#
# 这个类可以使用如下形式为动物园增加一只猫：
#
# if __name__ == '__main__':
#     # 实例化动物园
#     z = Zoo('时间动物园')
#     # 实例化一只猫，属性包括名字、类型、体型、性格
#     cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
#     # 增加一只猫到动物园
#     z.add_animal(cat1)
#     # 动物园是否有猫这种动物
#     have_cat = hasattr(z, 'Cat')
#
# 具体要求：
#   定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
#   动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
#   猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
#   动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。


class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        # 同一隻動物不能重複添加
        for a in self.animals:
            if animal is a:
                print(f'[!] 無法加入 {animal} ：已存在動物園')
                return False
        self.animals.append(animal) # 加入動物
        print(f'[+] {animal} 已成功加入動物園')

    # 檢查動物是否存在
    def check_animal_type(self, type_name):
        for a in self.animals:
            if type_name == type(a).__name__:
                print(f'[+] 在動物園中發現 {type_name}')
                return True
        print(f'[!] 在動物園中未發現 {type_name}')
        return False


def hasattr(zoo, type_name):
    return zoo.check_animal_type(type_name)

class Animal():
    def __init__(self, diet, body_type, character):
        self.diet = diet
        self.body_type = body_type
        self.character = character

    # 是否為凶猛动物
    @property
    def is_fierce(self):
        return self.body_type in ['中', '大'] and self.diet == '食肉' and self.character == '兇猛'


class Cat(Animal):
    voice = '喵' #叫聲
    pet = True # 適合作為寵物
    def __init__(self, name, diet, body_type, character):
        super().__init__(diet, body_type, character)
        self.name = name


class Tiger(Animal):
    voice = '吼'
    pet = False
    def __init__(self, name, diet, body_type, character):
        super().__init__(diet, body_type, character)
        self.name = name


if __name__ == '__main__':
    # 實例化動物園
    z = Zoo('時間動物園')

    # 實例化一隻貓，屬性包括名字、類型、體型、性格
    cat1 = Cat('大花貓 1', '食肉', '小', '溫順')

    # 增加一隻貓到動物園
    z.add_animal(cat1)

    # 增加一隻老虎到動物園
    tiger1 = Tiger('老虎 1', '食肉', '中', '兇猛')
    z.add_animal(tiger1)

    # 貓無法重複添加
    z.add_animal(cat1)

    # 檢查動物園是否有指定類型的動物
    hasattr(z, 'Cat')
    hasattr(z, 'Elephant')

    #動物列表
    print('[+] 已加入動物園的動物有：')
    for i in z.animals:
        print(type(i))