# default dict


from collections import defaultdict

dd = defaultdict(list)

dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr Sniffles')

if __name__ == '__main__':
    print(dd['dogs'])
    print(dd['cats'])
