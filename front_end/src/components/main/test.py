with open('C:\\Users\\Administrator\\Desktop\\Study\\vue\\Sample\\blivedm-dev\\blivedm-dev\\room_id.txt', 'r') as f:
    room_id = f.read()
    f.close()
print(room_id)
f = open('C:\\Users\\Administrator\\Desktop\\Study\\vue\\Sample\\blivedm-dev\\blivedm-dev\\room_id.txt', 'a',encoding="utf-8")
f.write('\n' + f'123456')
f.close()