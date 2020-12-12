# import api.app as api
import package.gen.basic as basic

def run():
    print(basic.generate('cvcvcv', 5, True))
    print(basic.generate('cvvcv', 5))
    print(basic.completely_random(5, True))

if __name__ == "__main__":
    run()