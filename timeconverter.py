def convert_to_24_hour(s):

    if "a.m." in s:
        s= s.replace(' a.m.','')
        s=s.replace(':','')
        print(s)
        return s

    else:
        s= s.replace(' p.m.','')
        s=s.replace(':','')
        s=int(s)
        s +=1200
        s = str(s)
        print(s)
        return s
if __name__ == '__main__':
    s=convert_to_24_hour('11:00 a.m.')
    print(s)
    s = print(convert_to_24_hour('1:32 p.m.'))
    print(s)
