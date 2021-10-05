# Реализовать функцию int_func(), принимающую слова из маленьких
# латинских букв и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

#Честно говоря. не очень понятно...))) Слишком легко

def int_func(new_string):
    new_string = new_string.title()
    return(new_string)

print(int_func('привет как дела'))