# import api.app as api
# from package.api.startup_requests import get_letters_from_db, get_clusters_from_db
import package.gen.basic as basic
# import package.api.startup_requests as sr
import random

def run():
    items = {'template': 'BvCe',
            'num': 10,
            'is_weighted': True,
            'is_random': False}
    print(basic.generate_from_template(**items))
    # letters = get_clusters_from_db()
    # print(letters['cl'], letters['clf'])
    # print(random.choices(letters['cl'], weights=letters['clf'], k=1)[0])

    # for l in range(len(letters['l'])):
    #     let = letters['l']
    #     freq = letters['lf']
    #     print(let[l], freq[l])

if __name__ == "__main__":
    run()