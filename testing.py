# import api.app as api
import package.gen.basic as basic

def run():
    items = {'template': False,
            'num': 1,
            'is_weighted': True,
            'is_random': True}
    print(basic.generate(**items))

if __name__ == "__main__":
    run()