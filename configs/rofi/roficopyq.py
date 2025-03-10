#!/usr/bin/env python3

import json
import subprocess as sp

copyq_script_getAll = r"""
var result=[];
for ( var i = 0; i < size(); ++i ) {
    var obj = {};
    obj.row = i;
    obj.mimetypes = str(read("?", i)).split("\n");
    obj.mimetypes.pop();
    obj.text = str(read(i));
    result.push(obj);
}
JSON.stringify(result);
"""

if __name__ == '__main__':
    p = sp.run('copyq -'.split(), input=copyq_script_getAll,
               encoding='utf-8', stdout=sp.PIPE, stderr=sp.PIPE)
    
    if p.returncode != 0:
        print("CopyQ Error:", p.stderr)
        exit(1)

    print("CopyQ Output:", p.stdout) 

    json_arr = json.loads(p.stdout)

    items = []
    for json_obj in json_arr:
        text = json_obj['text']
        text = " ".join(filter(None, text.replace("\n", " ").split(" ")))
        items.append(text)

    title = 'Clipboard'
    rofi = f'rofi -dmenu -i -p {title} -format i'.split()
    rofi_input = '\n'.join(x for x in items)

    print("Rofi Input:", rofi_input)  

    p = sp.run(rofi, input=rofi_input, encoding='utf-8', stdout=sp.PIPE, stderr=sp.PIPE)
    if p.returncode == 0:
        num = p.stdout.strip()
        print("Selected Item:", num) 
        sp.run(f'copyq select({num});'.split(),
               encoding='utf-8', stdout=sp.PIPE, stderr=sp.PIPE)
    else:
        print("Rofi Error:", p.stderr) 
