# import api.app as api
import package.gen.basic as basic

def run():
    items = {'template': 'cVccvcV',
            'num': 10,
            'is_weighted': True,
            'is_random': False}
    print(basic.generate_from_template(**items))

if __name__ == "__main__":
    run()