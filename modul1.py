from coffee import greather_than
from fifi import concatenate_list

def main():
    gt = greather_than(4, 6)
    print('modul1 {}'.format(gt))
    l1 = []
    l2 = [6, 7]
    print('modul1 {}'.format(concatenate_list(l1,l2)))

if __name__ == '__main__':
    main()

