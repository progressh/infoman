
str = """{ date:260407,
phone:,
tag:doctor+appointment+eye,
name:,
place:,
location:lexington,
event_date:260422,
}"""

curly_level = 0
str_start = 0
pos = 0
dic ={}
for char in str:
    if char == '{':
        curly_level += 1
    elif char == '}':
        curly_level -= 1
    elif char == ',':
        sub_str = str[str_start:pos]
        sep_pos = sub_str.find(":")
        dic[sub_str[:sep_pos]] = sub_str[sep_pos+1:]
        str_start = 0
    elif str_start == 0 and char!= '\n':
        str_start = pos
    pos += 1
print("h")
print (dic)
