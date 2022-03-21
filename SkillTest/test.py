import json

with open('db/exams.json', 'r') as users_file:
    data = json.load(users_file)


def iterate_multidimensional(my_dict, cond):
    for k,v in my_dict.items():
        if(isinstance(v,dict)):
            print(k+":")
            iterate_multidimensional(v,cond)
            continue
        if k == cond:
            print(k+" : "+str(v))


def iterate_json(my_dict,cond):
    for k,v in my_dict.items():
        if(isinstance(v,dict)):
            # print(k+":")
            iterate_multidimensional(v,cond)
            continue
        print(k+" : "+str(v))

iterate_json(data,cond='options')